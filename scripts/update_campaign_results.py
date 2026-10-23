#!/usr/bin/env python3
"""
GoPhish Campaign Results Updater
Phishing Simulation and Security Awareness Program

Connects to the local GoPhish REST API, retrieves active and completed campaign metrics,
and updates results/campaign-comparison.csv while preserving existing notes and categorizations.

Security & Safety:
- Never exposes API keys in source code, logs, or CSV output.
- Reads API key strictly from the GOPHISH_API_KEY environment variable.
- Safe TLS handling: Supports verifying against the local GoPhish self-signed certificate.
- Read-only operations against GoPhish: Never launches campaigns or modifies configuration.
"""

import os
import sys
import csv
import json
import ssl
import argparse
from pathlib import Path
import urllib.request
import urllib.error

# Project directory paths
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DEFAULT_CSV_PATH = PROJECT_ROOT / "results" / "campaign-comparison.csv"
DEFAULT_GOPHISH_URL = "https://127.0.0.1:3333"

# Potential paths to local self-signed GoPhish admin certificate
DEFAULT_CERT_CANDIDATES = [
    PROJECT_ROOT / "GoPhish" / "gophish-v0.12.1-windows-64bit" / "gophish_admin.crt",
    PROJECT_ROOT / "gophish" / "gophish_admin.crt",
    SCRIPT_DIR / "gophish_admin.crt"
]

# Standard CSV Headers
CSV_HEADERS = [
    "Campaign_ID",
    "Campaign_Name",
    "Status",
    "Launch_Date",
    "Total_Recipients",
    "Sent",
    "Opened",
    "Open_Rate_%",
    "Clicked",
    "Click_Rate_%",
    "Submitted_Data",
    "Reported",
    "Reporting_Rate_%",
    "Campaign_Type",
    "Notes"
]

def determine_campaign_type_and_note(name: str):
    """
    Categorizes campaigns into baseline, post-training, or technical tracking verification,
    and returns a descriptive default note.
    """
    lower = name.lower()
    if "tracking" in lower or "verification" in lower:
        c_type = "Technical Tracking Verification"
        note = "Technical verification test to validate tracking pixel and redirect handling."
    elif "baseline" in lower or "campaign 1" in lower:
        c_type = "Baseline Assessment"
        note = "Initial baseline measurement before security awareness training."
    elif "post-training" in lower or "campaign 2" in lower:
        c_type = "Post-Training Evaluation"
        note = "Post-awareness training evaluation campaign to measure behavioral improvement."
    else:
        c_type = "Simulation Campaign"
        note = "Security awareness simulation campaign."
    return c_type, note


def create_ssl_context(cert_path=None, insecure=False):
    """
    Creates a secure SSL context for communicating with local GoPhish.
    In GoPhish, auto-generated self-signed certificates have CN=Gophish with no SAN,
    so hostname checking must be configured appropriately.
    """
    if insecure:
        print("[WARNING] TLS verification disabled via --insecure flag. Suitable for local test labs only.")
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

    # Find certificate path
    resolved_cert = None
    if cert_path and Path(cert_path).is_file():
        resolved_cert = Path(cert_path)
    else:
        for candidate in DEFAULT_CERT_CANDIDATES:
            if candidate.is_file():
                resolved_cert = candidate
                break

    if resolved_cert:
        print(f"[INFO] Using local GoPhish certificate for TLS verification: {resolved_cert}")
        ctx = ssl.create_default_context(cafile=str(resolved_cert))
        # GoPhish self-signed certificates lack SubjectAltName for IP 127.0.0.1
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_REQUIRED
        return ctx

    # If no local cert found, attempt standard system root bundle
    ctx = ssl.create_default_context()
    return ctx


def fetch_campaigns(base_url: str, api_key: str, ssl_context: ssl.SSLContext):
    """
    Queries GoPhish GET /api/campaigns/ endpoint and returns the JSON list of campaigns.
    """
    url = f"{base_url.rstrip('/')}/api/campaigns/?api_key={api_key}"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": api_key,
            "User-Agent": "GoPhish-Metrics-Updater/1.0"
        }
    )

    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=10) as resp:
            data = resp.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("[ERROR] GoPhish API Authentication Failed (HTTP 401).")
            print("        Please verify that your GOPHISH_API_KEY environment variable matches your GoPhish User Settings API key.")
        else:
            print(f"[ERROR] HTTP Error from GoPhish API: {e.code} - {e.reason}")
        return None
    except urllib.error.URLError as e:
        reason_str = str(e.reason)
        if "CERTIFICATE_VERIFY_FAILED" in reason_str:
            print("[ERROR] SSL Certificate Verification Failed.")
            print("        GoPhish uses a local self-signed certificate.")
            print("        Options to resolve:")
            print("        1. Provide cert path: python scripts/update_campaign_results.py --cert-path GoPhish/gophish-v0.12.1-windows-64bit/gophish_admin.crt")
            print("        2. Allow local insecure test connection: python scripts/update_campaign_results.py --insecure")
        elif "Connection refused" in reason_str or "WinError 10061" in reason_str:
            print(f"[ERROR] Could not connect to GoPhish at {base_url}.")
            print("        Please verify that gophish.exe is running on port 3333.")
        else:
            print(f"[ERROR] Connection error: {e.reason}")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected error querying GoPhish API: {e}")
        return None



def normalize_text(val) -> str:
    """
    Safely normalizes CSV and API string values.
    Handles None, null-like strings, and whitespace.
    Does NOT convert None into the literal string 'None'.
    """
    if val is None:
        return ""
    s = str(val).strip()
    if s.lower() in ("none", "null"):
        return ""
    return s


def extract_metrics(campaign: dict):
    """
    Safely extracts metrics from a GoPhish campaign object.
    Supports both 'stats' dictionary and direct tallying from 'results'.
    Handles missing or None values safely.
    """
    stats = campaign.get("stats") or {}
    results = campaign.get("results") or []

    if stats and isinstance(stats, dict):
        total = int(stats.get("total") or len(results))
        sent = int(stats.get("sent") or 0)
        opened = int(stats.get("opened") or 0)
        clicked = int(stats.get("clicked") or 0)
        submitted_data = int(stats.get("submitted_data") or 0)
        reported = int(stats.get("reported") or 0)
    else:
        total = len(results)
        sent = sum(1 for r in results if r.get("status") in ["Email Sent", "Email Opened", "Clicked Link", "Submitted Data"])
        opened = sum(1 for r in results if r.get("status") in ["Email Opened", "Clicked Link", "Submitted Data"])
        clicked = sum(1 for r in results if r.get("status") in ["Clicked Link", "Submitted Data"])
        submitted_data = sum(1 for r in results if r.get("status") == "Submitted Data")
        reported = sum(1 for r in results if bool(r.get("reported")))

    # Calculate percentages safely
    open_rate = f"{(opened / sent * 100):.1f}%" if sent > 0 else "0.0%"
    click_rate = f"{(clicked / sent * 100):.1f}%" if sent > 0 else "0.0%"
    reporting_rate = f"{(reported / sent * 100):.1f}%" if sent > 0 else "0.0%"

    return {
        "total": total,
        "sent": sent,
        "opened": opened,
        "open_rate": open_rate,
        "clicked": clicked,
        "click_rate": click_rate,
        "submitted_data": submitted_data,
        "reported": reported,
        "reporting_rate": reporting_rate
    }


def load_existing_csv(csv_path: Path):
    """
    Loads existing CSV rows into memory, normalizing None/missing values and preserving all fields.
    """
    if not csv_path.is_file():
        return []

    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            clean_r = {}
            for k, v in r.items():
                if k is not None:
                    clean_r[k] = normalize_text(v)
            rows.append(clean_r)
    return rows


def update_csv_data(existing_rows: list, campaigns: list):
    """
    Matches GoPhish campaigns to existing CSV rows by Campaign_Name,
    updating metrics while strictly preserving existing user notes.
    Appends any newly discovered campaigns.
    Defensively handles None, missing, or null fields.
    """
    updated_rows = [dict(r) for r in existing_rows]
    matched_campaign_ids = set()
    summary = {
        "updated": [],
        "added": [],
        "unmatched_in_csv": []
    }

    # Match campaigns by name (case-insensitive)
    for c in campaigns:
        c_id = normalize_text(c.get("id"))
        c_name = normalize_text(c.get("name"))
        c_status = normalize_text(c.get("status"))
        c_launch = normalize_text(c.get("launch_date"))

        if not c_name:
            continue

        metrics = extract_metrics(c)
        c_type, default_note = determine_campaign_type_and_note(c_name)

        matched_row = None
        for row in updated_rows:
            row_name = normalize_text(row.get("Campaign_Name"))
            if row_name.lower() == c_name.lower():
                matched_row = row
                break

        if matched_row is not None:
            # Update metrics
            matched_row["Campaign_ID"] = c_id
            matched_row["Status"] = c_status
            matched_row["Launch_Date"] = c_launch if c_launch else normalize_text(matched_row.get("Launch_Date"))
            matched_row["Total_Recipients"] = str(metrics["total"])
            matched_row["Sent"] = str(metrics["sent"])
            matched_row["Opened"] = str(metrics["opened"])
            matched_row["Open_Rate_%"] = metrics["open_rate"]
            matched_row["Clicked"] = str(metrics["clicked"])
            matched_row["Click_Rate_%"] = metrics["click_rate"]
            matched_row["Submitted_Data"] = str(metrics["submitted_data"])
            matched_row["Reported"] = str(metrics["reported"])
            matched_row["Reporting_Rate_%"] = metrics["reporting_rate"]

            existing_type = normalize_text(matched_row.get("Campaign_Type"))
            if existing_type in ("Baseline Assessment", "Post-Training Evaluation", "Technical Tracking Verification", "Simulation Campaign"):
                matched_row["Campaign_Type"] = existing_type
            else:
                matched_row["Campaign_Type"] = c_type

            # Preserve existing note; only fill if blank/None
            existing_note = normalize_text(matched_row.get("Notes"))
            matched_row["Notes"] = existing_note if existing_note else default_note

            summary["updated"].append(c_name)
            matched_campaign_ids.add(c_name.lower())
        else:
            # Add new discovered campaign
            new_row = {
                "Campaign_ID": c_id,
                "Campaign_Name": c_name,
                "Status": c_status,
                "Launch_Date": c_launch,
                "Total_Recipients": str(metrics["total"]),
                "Sent": str(metrics["sent"]),
                "Opened": str(metrics["opened"]),
                "Open_Rate_%": metrics["open_rate"],
                "Clicked": str(metrics["clicked"]),
                "Click_Rate_%": metrics["click_rate"],
                "Submitted_Data": str(metrics["submitted_data"]),
                "Reported": str(metrics["reported"]),
                "Reporting_Rate_%": metrics["reporting_rate"],
                "Campaign_Type": c_type,
                "Notes": default_note
            }
            updated_rows.append(new_row)
            summary["added"].append(c_name)
            matched_campaign_ids.add(c_name.lower())

    # Record existing rows not returned by GoPhish
    for r in existing_rows:
        name = normalize_text(r.get("Campaign_Name"))
        if name and name.lower() not in matched_campaign_ids:
            summary["unmatched_in_csv"].append(name)

    return updated_rows, summary


def save_csv(csv_path: Path, rows: list):
    """
    Saves rows to CSV in UTF-8 format safely using an atomic temporary write.
    Never overwrites the target file with corrupted or incomplete data.
    """
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = csv_path.with_suffix(".tmp")
    try:
        with open(temp_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writeheader()
            for r in rows:
                clean_row = {h: normalize_text(r.get(h)) for h in CSV_HEADERS}
                writer.writerow(clean_row)
        temp_path.replace(csv_path)
    except Exception as e:
        if temp_path.is_file():
            temp_path.unlink()
        raise e


def main():
    parser = argparse.ArgumentParser(
        description="Retrieve GoPhish campaign metrics and update results/campaign-comparison.csv"
    )
    parser.add_argument(
        "--url",
        default=os.environ.get("GOPHISH_URL", DEFAULT_GOPHISH_URL),
        help=f"GoPhish base URL (default: {DEFAULT_GOPHISH_URL})"
    )
    parser.add_argument(
        "--csv",
        default=str(DEFAULT_CSV_PATH),
        help="Path to campaign comparison CSV file"
    )
    parser.add_argument(
        "--cert-path",
        default=os.environ.get("GOPHISH_SSL_CERT", None),
        help="Path to gophish_admin.crt certificate"
    )
    parser.add_argument(
        "--insecure",
        action="store_true",
        default=(os.environ.get("GOPHISH_INSECURE_SKIP_VERIFY", "false").lower() == "true"),
        help="Disable TLS certificate verification (local test labs only)"
    )

    args = parser.parse_args()

    # Step 1: Secure API Key Retrieval
    api_key = os.environ.get("GOPHISH_API_KEY", "").strip()
    if not api_key:
        print("\n" + "="*70)
        print("[ERROR] Missing GOPHISH_API_KEY environment variable.")
        print("="*70)
        print("For security, the API key is not stored in files or source code.")
        print("To configure your key in Windows PowerShell for this session, run:\n")
        print('    $env:GOPHISH_API_KEY = "your_actual_api_key_from_gophish"\n')
        print("Where to find your API key:")
        print("1. Log in to GoPhish: https://127.0.0.1:3333")
        print("2. Navigate to 'User Settings' in the left menu.")
        print("3. Copy the string in the 'API Key' field.")
        print("="*70 + "\n")
        sys.exit(1)

    csv_path = Path(args.csv)

    # Step 2: Establish TLS context
    ssl_context = create_ssl_context(cert_path=args.cert_path, insecure=args.insecure)

    # Step 3: Fetch campaigns from GoPhish API
    print(f"\n[INFO] Connecting to GoPhish API at {args.url}/api/campaigns/ ...")
    campaigns = fetch_campaigns(args.url, api_key, ssl_context)

    if campaigns is None:
        print("[ABORT] Could not retrieve campaign data. Existing CSV was preserved without changes.")
        sys.exit(2)

    print(f"[SUCCESS] Retrieved {len(campaigns)} campaign(s) from GoPhish.")

    # Step 4: Load existing CSV and update rows
    existing_rows = load_existing_csv(csv_path)
    updated_rows, summary = update_csv_data(existing_rows, campaigns)

    # Step 5: Save updated CSV
    save_csv(csv_path, updated_rows)
    print(f"[SUCCESS] Updated CSV written to: {csv_path}\n")

    # Step 6: Display clear summary table (using safe ASCII symbols for Windows console compatibility)
    print("="*70)
    print("CAMPAIGN UPDATE SUMMARY")
    print("="*70)

    if summary["updated"]:
        print(f"Updated Existing Campaigns ({len(summary['updated'])}):")
        for c in summary["updated"]:
            print(f"  [OK] {c}")
    else:
        print("Updated Existing Campaigns: None")

    if summary["added"]:
        print(f"\nNewly Discovered Campaigns Added ({len(summary['added'])}):")
        for c in summary["added"]:
            print(f"  [+] {c}")
    else:
        print("\nNewly Discovered Campaigns: None")

    if summary["unmatched_in_csv"]:
        print(f"\nCampaigns in CSV awaiting test run in GoPhish ({len(summary['unmatched_in_csv'])}):")
        for c in summary["unmatched_in_csv"]:
            print(f"  [-] {c}")

    print("="*70 + "\n")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    main()


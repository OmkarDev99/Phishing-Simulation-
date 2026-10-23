#!/usr/bin/env python3
"""
Unit and Regression Tests for scripts/update_campaign_results.py
Phishing Simulation and Security Awareness Program

Tests:
1. Normalization of None, 'None', 'null', and whitespace strings.
2. Reproduction and regression testing of NoneType handling in CSV rows:
   - Row with 'Notes': None
   - Row with missing 'Notes' key
   - Row with 'Notes': 'None'
   - Row with 'Campaign_Name': None
3. Preservation of existing custom notes.
4. Correct application of default notes when missing.
5. Defensive metric extraction when stats/results contain None or missing values.
6. Safe CSV reading and atomic writing.
"""

import sys
import unittest
import tempfile
from pathlib import Path

# Add project root to sys.path so we can import from scripts
TEST_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = TEST_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.update_campaign_results import (
    normalize_text,
    extract_metrics,
    update_csv_data,
    load_existing_csv,
    save_csv,
    determine_campaign_type_and_note
)


class TestUpdateCampaignResults(unittest.TestCase):

    def test_normalize_text(self):
        """Test safe text normalization against None and null-like strings."""
        self.assertEqual(normalize_text(None), "")
        self.assertEqual(normalize_text("None"), "")
        self.assertEqual(normalize_text("none"), "")
        self.assertEqual(normalize_text("NONE"), "")
        self.assertEqual(normalize_text("null"), "")
        self.assertEqual(normalize_text("NULL"), "")
        self.assertEqual(normalize_text(""), "")
        self.assertEqual(normalize_text("   "), "")
        self.assertEqual(normalize_text("  Valid Text  "), "Valid Text")
        self.assertEqual(normalize_text(123), "123")

    def test_regression_missing_or_none_notes_in_csv(self):
        """
        Regression Test: Reproduce the exact bug where matched_row['Notes'] is None
        or missing entirely, verifying that AttributeError is NOT raised.
        """
        # Row 1: 'Notes' is explicitly None (DictReader default when field is missing)
        # Row 2: 'Notes' key is completely omitted
        # Row 3: 'Notes' is literal string 'None'
        # Row 4: 'Notes' has an existing custom user comment (must be preserved!)
        existing_rows = [
            {
                "Campaign_ID": "1",
                "Campaign_Name": "Campaign 1 - Baseline Test",
                "Status": "Pending",
                "Notes": None  # <-- Bug trigger in previous version
            },
            {
                "Campaign_ID": "2",
                "Campaign_Name": "Campaign 1 - Tracking Test",
                "Status": "Pending"
                # 'Notes' key intentionally omitted
            },
            {
                "Campaign_ID": "3",
                "Campaign_Name": "Campaign 2 - Post-Training Evaluation",
                "Status": "Pending",
                "Notes": "None"  # Literal string 'None' from bad CSV export
            },
            {
                "Campaign_ID": "4",
                "Campaign_Name": "Campaign 3 - Tracking Verification",
                "Status": "Pending",
                "Notes": "Preserve this authentic lab note from examiners"
            }
        ]

        campaigns = [
            {
                "id": 101,
                "name": "Campaign 1 - Baseline Test",
                "status": "Completed",
                "launch_date": "2026-10-23T01:00:00Z",
                "stats": {"total": 5, "sent": 5, "opened": 4, "clicked": 2, "submitted_data": 0, "reported": 1}
            },
            {
                "id": 102,
                "name": "Campaign 1 - Tracking Test",
                "status": "In progress",
                "launch_date": None,  # None launch date test
                "stats": {"total": 2, "sent": 2, "opened": 2, "clicked": 1, "submitted_data": 0, "reported": 0}
            },
            {
                "id": 103,
                "name": "Campaign 2 - Post-Training Evaluation",
                "status": "Completed",
                "launch_date": "2026-10-23T02:00:00Z",
                "stats": {"total": 5, "sent": 5, "opened": 3, "clicked": 1, "submitted_data": 0, "reported": 3}
            },
            {
                "id": 104,
                "name": "Campaign 3 - Tracking Verification",
                "status": "Completed",
                "launch_date": "2026-10-23T02:30:00Z",
                "stats": {"total": 3, "sent": 3, "opened": 3, "clicked": 0, "submitted_data": 0, "reported": 0}
            }
        ]

        # Must execute without throwing AttributeError
        updated_rows, summary = update_csv_data(existing_rows, campaigns)

        # Assert all 4 campaigns were updated
        self.assertEqual(len(summary["updated"]), 4)
        self.assertEqual(len(updated_rows), 4)

        # Row 1 (Notes was None): should receive default baseline note
        _, default_baseline_note = determine_campaign_type_and_note("Campaign 1 - Baseline Test")
        self.assertEqual(updated_rows[0]["Notes"], default_baseline_note)
        self.assertEqual(updated_rows[0]["Sent"], "5")
        self.assertEqual(updated_rows[0]["Open_Rate_%"], "80.0%")
        self.assertEqual(updated_rows[0]["Click_Rate_%"], "40.0%")

        # Row 2 (Notes was omitted): should receive default tracking note
        _, default_tracking_note = determine_campaign_type_and_note("Campaign 1 - Tracking Test")
        self.assertEqual(updated_rows[1]["Notes"], default_tracking_note)
        self.assertEqual(updated_rows[1]["Sent"], "2")
        self.assertEqual(updated_rows[1]["Launch_Date"], "")  # None handled gracefully

        # Row 3 (Notes was 'None'): should receive default post-training note
        _, default_post_note = determine_campaign_type_and_note("Campaign 2 - Post-Training Evaluation")
        self.assertEqual(updated_rows[2]["Notes"], default_post_note)
        self.assertEqual(updated_rows[2]["Reported"], "3")
        self.assertEqual(updated_rows[2]["Reporting_Rate_%"], "60.0%")

        # Row 4 (Notes had custom text): MUST be preserved!
        self.assertEqual(
            updated_rows[3]["Notes"],
            "Preserve this authentic lab note from examiners"
        )

    def test_extract_metrics_safe_against_none(self):
        """Test that extract_metrics handles None values in stats dictionary."""
        campaign_with_nones = {
            "name": "Test Campaign",
            "stats": {
                "total": None,
                "sent": None,
                "opened": None,
                "clicked": None,
                "submitted_data": None,
                "reported": None
            }
        }
        metrics = extract_metrics(campaign_with_nones)
        self.assertEqual(metrics["total"], 0)
        self.assertEqual(metrics["sent"], 0)
        self.assertEqual(metrics["open_rate"], "0.0%")
        self.assertEqual(metrics["click_rate"], "0.0%")

    def test_atomic_save_and_load_csv(self):
        """Test atomic CSV saving and loading with missing/None fields."""
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = Path(tmpdir) / "test_campaigns.csv"

            # Create a CSV with incomplete columns
            with open(csv_path, "w", encoding="utf-8") as f:
                f.write("Campaign_Name,Status\n")
                f.write("Campaign 1 - Baseline Test,Pending\n")

            loaded = load_existing_csv(csv_path)
            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0]["Campaign_Name"], "Campaign 1 - Baseline Test")
            # Missing columns like Notes are not yet in loaded dict, which is safe
            self.assertEqual(loaded[0].get("Notes", ""), "")

            # Update with API data and save
            campaigns = [{
                "id": 1,
                "name": "Campaign 1 - Baseline Test",
                "status": "In progress",
                "stats": {"total": 5, "sent": 5, "opened": 5, "clicked": 2, "submitted_data": 0, "reported": 0}
            }]
            updated, _ = update_csv_data(loaded, campaigns)
            save_csv(csv_path, updated)

            # Re-read saved CSV
            reloaded = load_existing_csv(csv_path)
            self.assertEqual(len(reloaded), 1)
            self.assertEqual(reloaded[0]["Sent"], "5")
            self.assertEqual(reloaded[0]["Open_Rate_%"], "100.0%")
            self.assertTrue(len(reloaded[0]["Notes"]) > 0)


if __name__ == "__main__":
    unittest.main()

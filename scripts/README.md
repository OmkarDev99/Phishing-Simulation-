# GoPhish Campaign Results Updater (`scripts/`)

This directory contains the automation script [`update_campaign_results.py`](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/scripts/update_campaign_results.py) to retrieve simulation metrics directly from your local GoPhish instance and synchronize them into [`results/campaign-comparison.csv`](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/results/campaign-comparison.csv).

---

## 1. Where to Obtain Your GoPhish API Key

For security, the API key is **never** hardcoded into files or tracked in version control. You retrieve it directly from your GoPhish admin portal:

1. Open your web browser and navigate to:  
   👉 **`https://127.0.0.1:3333`**
2. Log in with your GoPhish administrator credentials.
3. In the left-hand navigation sidebar, click on **User Settings**.
4. In the **API Key** section, copy your alphanumeric API key string.

---

## 2. Setting the Environment Variable in Windows PowerShell

Open a PowerShell terminal and set the environment variable for your current terminal session:

```powershell
$env:GOPHISH_API_KEY = "PASTE_YOUR_GOPHISH_API_KEY_HERE"
```

> **Security Note:** This sets the environment variable only in your active PowerShell window. When you close the window, the key is removed from memory.

---

## 3. Dependencies

The script is built entirely using Python's built-in standard library (`urllib`, `ssl`, `json`, `csv`, `pathlib`, `argparse`).  
**No extra pip packages are required.**

Ensure Python 3 (3.8+) is installed and accessible in your PATH:
```powershell
python --version
```

---

## 4. How to Run the Updater

Run the script from your project root directory:

```powershell
cd C:\Users\PC\Desktop\Phishing-Awareness-Project
python scripts\update_campaign_results.py
```

### Optional Command Line Arguments

| Argument | Description | Default |
|---|---|---|
| `--url <URL>` | GoPhish admin base URL | `https://127.0.0.1:3333` |
| `--csv <PATH>` | Target CSV destination path | `results/campaign-comparison.csv` |
| `--cert-path <PATH>` | Path to local `gophish_admin.crt` | Auto-detected in `GoPhish/.../` |
| `--insecure` | Disable TLS certificate verification (local test labs only) | `False` |

Example with explicit cert path:
```powershell
python scripts\update_campaign_results.py --cert-path GoPhish\gophish-v0.12.1-windows-64bit\gophish_admin.crt
```

---

## 5. How to Verify That the CSV Has Been Updated

1. Open [`results/campaign-comparison.csv`](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/results/campaign-comparison.csv) in VS Code, Notepad, or Microsoft Excel.
2. Verify that the rows match your GoPhish campaigns:
   - `Campaign 1 - Baseline Test`
   - `Campaign 1 - Tracking Test`
   - `Campaign 2 - Post-Training Evaluation`
   - `Campaign 3 - Tracking Verification`
3. Check that the columns for `Sent`, `Opened`, `Clicked`, `Open_Rate_%`, `Click_Rate_%`, and `Reported` now reflect the telemetry from your GoPhish dashboard.
4. Any custom user comments written in the `Notes` column are strictly preserved across updates.

---

## 6. Common Errors & Solutions

### 1. `[ERROR] Missing GOPHISH_API_KEY environment variable`
- **Cause:** You ran the script without setting `$env:GOPHISH_API_KEY`.
- **Solution:** Run `$env:GOPHISH_API_KEY = "your_actual_key"` before running the script.

### 2. `[ERROR] GoPhish API Authentication Failed (HTTP 401)`
- **Cause:** The provided API key is invalid or does not match your GoPhish user profile.
- **Solution:** Re-copy the API key from GoPhish -> **User Settings** -> **API Key** and re-set `$env:GOPHISH_API_KEY`.

### 3. `[ERROR] Could not connect to GoPhish at https://127.0.0.1:3333`
- **Cause:** GoPhish is not currently running.
- **Solution:** Open a PowerShell window, navigate to your GoPhish folder, and start it:
  ```powershell
  cd C:\Users\PC\Desktop\Phishing-Awareness-Project\GoPhish\gophish-v0.12.1-windows-64bit
  .\gophish.exe
  ```

### 4. `[ERROR] SSL Certificate Verification Failed`
- **Cause:** GoPhish uses an auto-generated self-signed HTTPS certificate (`gophish_admin.crt`).
- **Solution:** The script automatically detects `GoPhish/gophish-v0.12.1-windows-64bit/gophish_admin.crt`. If you moved the certificate, pass `--cert-path <path>` or use `--insecure` for local testing.

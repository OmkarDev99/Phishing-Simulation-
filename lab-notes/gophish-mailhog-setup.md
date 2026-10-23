# Step 2: GoPhish and MailHog Windows Setup Guide

> **Important Note:** Follow these instructions on your Windows computer. Installation is **not** complete until you have downloaded both applications, launched them, and verified that a test email appears inside the MailHog web interface.

---

## 1. Architecture Overview
To keep this project 100% safe, isolated, and legal, we use a two-component local architecture:

```
[ GoPhish Simulation Engine ]
  - Admin Web UI: https://127.0.0.1:3333
  - Phishing Web Server: http://127.0.0.1:8080
          │
          │ (Sends SMTP mail via port 1025)
          ▼
[ MailHog Local Fake SMTP Server ]
  - SMTP Listening Port: 127.0.0.1:1025 (catches all emails, sends nothing to internet)
  - Webmail Inbox UI: http://127.0.0.1:8025 (where you view delivered emails)
          │
          │ (You open & inspect emails in your browser)
          ▼
[ Local Student / Dummy Recipient ]
```

---

## 2. Official Download Links

| Component | Official GitHub Release Link | Recommended Windows File |
|---|---|---|
| **GoPhish** | [https://github.com/gophish/gophish/releases](https://github.com/gophish/gophish/releases) | `gophish-v0.12.1-windows-64bit.zip` (or latest Windows 64-bit release) |
| **MailHog** | [https://github.com/mailhog/MailHog/releases](https://github.com/mailhog/MailHog/releases) | `MailHog_windows_amd64.exe` |

*(Always download from the official GitHub repositories listed above to ensure binary integrity and security).*

---

## 3. Step-by-Step Installation Instructions

### Step 2.1: Prepare a Local Tools Folder
1. Create a dedicated folder on your computer for running the lab tools (e.g., `C:\CyberLab` or inside a subfolder such as `C:\Users\PC\Desktop\Phishing-Awareness-Project\lab-tools`).
2. Move the downloaded `MailHog_windows_amd64.exe` into that folder and rename it to `MailHog.exe` for simplicity.
3. Unzip the GoPhish archive into a subfolder named `gophish` inside your lab folder.

---

### Step 2.2: Launch MailHog (The Safe Email Trap)
1. Open a **PowerShell** or **Command Prompt** window.
2. Navigate to your lab folder:
   ```powershell
   cd C:\CyberLab
   .\MailHog.exe
   ```
3. You should see console output stating:
   ```text
   [SMTP] Binding to address: 0.0.0.0:1025
   [HTTP] Binding to address: 0.0.0.0:8025
   ```
4. Open your web browser and navigate to:  
   👉 **`http://localhost:8025`** or **`http://127.0.0.1:8025`**  
   You will see the MailHog web interface (an empty inbox ready to receive emails).  
   *Keep this terminal window running in the background!*

---

### Step 2.3: Configure and Launch GoPhish
1. Open the extracted GoPhish folder and find `config.json`.
2. Open `config.json` in Notepad or VS Code to verify the ports:
   ```json
   {
     "admin_server": {
       "listen_url": "127.0.0.1:3333",
       "use_tls": true
     },
     "phish_server": {
       "listen_url": "0.0.0.0:8080",
       "use_tls": false
     },
     "db_name": "sqlite3",
     "db_path": "gophish.db",
     "migrations_prefix": "db/db_"
   }
   ```
   > **Tip:** If port 8080 is already used by another service, change `"listen_url": "0.0.0.0:8080"` to `"0.0.0.0:8088"`.
3. Open a **second** PowerShell window, navigate to the GoPhish folder, and run:
   ```powershell
   cd C:\CyberLab\gophish
   .\gophish.exe
   ```
4. **Locate your initial temporary password:**  
   During the first startup, GoPhish generates a random one-time administrator password and displays it in the terminal console:
   ```text
   Please login with the username admin and the password <temporary_alphanumeric_password>
   ```
   Copy this temporary password to your clipboard.  
   *Keep this second terminal running as well!*

---

### Step 2.4: Log In to the GoPhish Admin Dashboard
1. Open your browser and navigate to:  
   👉 **`https://127.0.0.1:3333`**
2. **Bypass the SSL Warning:**  
   Because GoPhish uses a self-signed HTTPS certificate, your browser (Chrome/Edge/Firefox) will display a security warning (*"Your connection isn't private"* or *"Potential Security Risk Ahead"*).  
   Click **Advanced** -> **Proceed to 127.0.0.1 (unsafe)**. (This is normal and safe for a local offline lab).
3. Log in with:
   - **Username:** `admin`
   - **Password:** `<the temporary password copied from the terminal>`
4. GoPhish will immediately prompt you to set a **New Password**. Enter a memorable lab password (e.g., `LabAdmin2026!`) and submit.
5. Take a screenshot of the main dashboard and save it as `screenshots/03-gophish-login-dashboard.png`.

---

### Step 2.5: Configure the Sending Profile in GoPhish
1. In the GoPhish sidebar menu, click **Sending Profiles**.
2. Click **+ New Profile**.
3. Fill in the fields exactly as follows:
   - **Name:** `MailHog Local SMTP`
   - **Interface Type:** `SMTP`
   - **From:** `IT Security Notification <it-support@lab.local>`
   - **Host:** `127.0.0.1:1025`
   - **Username:** *(leave blank)*
   - **Password:** *(leave blank)*
   - **Ignore Certificate Errors:** `Checked` (Toggle ON)
4. Click **Send Test Email** at the bottom of the modal:
   - **Send Test Email to:** `test-verification@lab.local`
   - Click **Send**.
5. You should receive a green success popup in GoPhish: *"Email Sent Successfully"*.
6. Switch back to your browser tab with MailHog (`http://127.0.0.1:8025`).
7. You should see the test email from `it-support@lab.local` sitting in your MailHog inbox!
8. Click **Save Profile** in GoPhish.
9. Take a screenshot of this configured profile and save as `screenshots/04-sending-profile-mailhog.png`.

---

## 4. Verification Checklist

Do not mark Step 2 complete until each box is checked:
- [ ] MailHog binary downloaded and running on ports 1025 (SMTP) and 8025 (HTTP).
- [ ] MailHog web interface opens at `http://127.0.0.1:8025`.
- [ ] GoPhish binary downloaded and extracted.
- [ ] GoPhish running in terminal and initial admin password retrieved.
- [ ] GoPhish admin portal opens at `https://127.0.0.1:3333` and password changed.
- [ ] Sending Profile created pointing to `127.0.0.1:1025`.
- [ ] Test email sent from GoPhish and successfully received in MailHog inbox.

---

## 5. Troubleshooting Common Windows Issues

| Issue | Cause | Solution |
|---|---|---|
| Port 8080 already in use | Another application (e.g. IIS, Tomcat, proxy) is listening on 8080 | Change `"listen_url": "0.0.0.0:8088"` in GoPhish `config.json` |
| Windows Defender SmartScreen blocks `gophish.exe` or `MailHog.exe` | Windows flags unsigned third-party open-source binaries | Click **More Info** -> **Run Anyway** |
| GoPhish console closes immediately upon launching | Port conflict or corrupt database file | Run `.\gophish.exe` from an existing PowerShell terminal to read the exact error message |
| Test email fails with connection refused | MailHog is not currently running | Ensure the MailHog terminal window remains open and active |

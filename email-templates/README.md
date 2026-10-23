# Email Templates & Landing Page Guide

This folder contains the templates used for the phishing simulation and educational drill.

## File Manifest

| File | Type | Purpose | GoPhish Destination |
|---|---|---|---|
| `it-security-update.html` | HTML Email | Template 1: Simulated IT compliance update (used in Campaign 1 Baseline) | GoPhish -> **Email Templates** -> **+ New Template** (HTML tab) |
| `it-security-update.txt` | Plain Text | Text alternative for Template 1 | GoPhish -> **Email Templates** -> **Text** tab |
| `package-delivery-alert.html` | HTML Email | Template 2: Simulated parcel delivery reschedule (used in Campaign 2 Post-Training) | GoPhish -> **Email Templates** -> **+ New Template** (HTML tab) |
| `package-delivery-alert.txt` | Plain Text | Text alternative for Template 2 | GoPhish -> **Email Templates** -> **Text** tab |
| `landing-page-educational.html` | HTML Webpage | Harmless educational landing page shown when target clicks link | GoPhish -> **Landing Pages** -> **+ New Page** (HTML tab) |

---

## How to Import into GoPhish

### 1. Import Email Template 1 (IT Security Update)
1. In GoPhish admin (`https://127.0.0.1:3333`), click **Email Templates** in the sidebar.
2. Click **+ New Template**.
3. **Name:** `IT Security Update (Campaign 1)`
4. **Subject:** `Urgent: Mandatory IT Security Certificate Validation`
5. Switch to the **HTML** tab. Copy and paste the entire contents of [it-security-update.html](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/email-templates/it-security-update.html).
6. Switch to the **Text** tab. Copy and paste the contents of [it-security-update.txt](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/email-templates/it-security-update.txt).
7. Ensure the checkbox **Add Tracking Image** is checked.
8. Click **Save Template**.

### 2. Import Email Template 2 (Package Delivery Alert)
1. Click **+ New Template**.
2. **Name:** `Package Delivery Alert (Campaign 2)`
3. **Subject:** `Urgent: Attempted Delivery Notice - Action Required`
4. Switch to the **HTML** tab. Copy and paste the entire contents of [package-delivery-alert.html](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/email-templates/package-delivery-alert.html).
5. Switch to the **Text** tab. Copy and paste the contents of [package-delivery-alert.txt](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/email-templates/package-delivery-alert.txt).
6. Ensure **Add Tracking Image** is checked.
7. Click **Save Template**.

### 3. Import the Educational Landing Page
1. In GoPhish admin, click **Landing Pages** in the sidebar.
2. Click **+ New Page**.
3. **Name:** `Harmless Awareness Landing Page`
4. Switch to the **HTML** tab. Copy and paste the entire contents of [landing-page-educational.html](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/email-templates/landing-page-educational.html).
5. **Capture Submitted Data:** Leave **UNCHECKED** (Our template collects no credentials).
6. Click **Save Page**.

> **Lab Safety Note:** Both templates prominently feature a yellow safety banner and use the GoPhish variable `{{.URL}}` which points to your local GoPhish phish server (`http://127.0.0.1:8080`), rendering the educational landing page.

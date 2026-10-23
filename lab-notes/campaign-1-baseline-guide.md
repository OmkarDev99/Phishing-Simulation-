# Step 4: Campaign 1 Baseline Guide (Controlled Test)

---

## 1. Objective of Campaign 1
In cybersecurity, a **baseline simulation** measures the natural vulnerability of an organization's users before conducting any formal awareness training. 

By testing a controlled cohort with simulated phishing emails without prior warning, we establish an authentic starting metric (such as initial open rates and click rates) to evaluate training effectiveness later.

---

## 2. Pre-Requisites Checklist
Before launching Campaign 1, ensure:
- [ ] MailHog is running in a PowerShell window (`http://127.0.0.1:8025`).
- [ ] GoPhish is running in a second PowerShell window (`https://127.0.0.1:3333`).
- [ ] The Sending Profile `MailHog Local SMTP` has been tested and verified.
- [ ] Email Template `IT Security Update (Campaign 1)` has been saved in GoPhish.
- [ ] Landing Page `Harmless Awareness Landing Page` has been saved in GoPhish.

---

## 3. Step-by-Step Execution

### Step 4.1: Create Users & Groups in GoPhish
1. In GoPhish, navigate to **Users & Groups** in the left menu.
2. Click **+ New Group**.
3. Set **Name:** `Lab Test Cohort`.
4. Add 5 dummy student/employee profiles (using safe fictitious emails):

| First Name | Last Name | Email | Position |
|---|---|---|---|
| Alice | Walker | `alice@lab.local` | Research Assistant |
| Bob | Martinez | `bob@lab.local` | Lab Technician |
| Carol | Davis | `carol@lab.local` | Junior Developer |
| David | Kim | `david@lab.local` | Systems Analyst |
| Eve | Johnson | `eve@lab.local` | Network Intern |

5. Click **Save Changes**.

---

### Step 4.2: Create and Launch Campaign 1
1. In GoPhish, navigate to **Campaigns** in the left menu.
2. Click **+ New Campaign**.
3. Fill in the campaign parameters:
   - **Name:** `Campaign 1 - Baseline IT Security Simulation`
   - **Email Template:** Select `IT Security Update (Campaign 1)`
   - **Landing Page:** Select `Harmless Awareness Landing Page`
   - **URL:** `http://127.0.0.1:8080` *(This tells GoPhish where the link points; it must match your phish_server listen_url)*
   - **Launch Date:** Send Immediately
   - **Sending Profile:** Select `MailHog Local SMTP`
   - **Groups:** Select `Lab Test Cohort`
4. Review the summary, then click **Launch Campaign**.
5. Save a screenshot of this setup as `screenshots/07-campaign-1-launch.png`.

---

### Step 4.3: Observe Email Delivery in MailHog
1. Open your browser to the MailHog web interface: `http://127.0.0.1:8025`.
2. Within seconds, all 5 emails will appear in the MailHog inbox:
   - Sender: `IT Security Notification <it-support@lab.local>`
   - Subject: `Urgent: Mandatory IT Security Certificate Validation`
3. Take a screenshot of the MailHog inbox and save as `screenshots/08-mailhog-inbox-received.png`.

---

### Step 4.4: Simulate Harmless User Interactions
In an educational lab where you are pair-programming or testing solo, you act as the dummy recipients to generate realistic baseline interaction data:

1. **Email Opens:**
   - In MailHog, click open the email for `alice@lab.local`, `bob@lab.local`, `carol@lab.local`, and `david@lab.local`. (4 out of 5 opened; leave Eve's unopened).
   - *Because GoPhish embeds a `{{.Tracker}}` 1x1 image, MailHog will render it and GoPhish will immediately log "Email Opened".*

2. **Link Clicks:**
   - Inside Alice's email, click the blue button **"Validate Security Certificate Now"**.
   - Your browser will open the URL `http://127.0.0.1:8080/?rid=...` and display the **Harmless Awareness Landing Page**.
   - Repeat the click for Bob and Carol.
   - Leave David's email opened but *do not click* the link (simulating a cautious user).

---

### Step 4.5: Inspect the GoPhish Campaign Dashboard
1. Switch to your GoPhish browser tab (`https://127.0.0.1:3333`).
2. Go to **Campaigns** and click on `Campaign 1 - Baseline IT Security Simulation`.
3. View the live real-time statistics:
   - **Total Emails Sent:** 5 (100%)
   - **Opened:** 4 (80%)
   - **Clicked Link:** 3 (60%)
   - **Submitted Data:** 0 (0% - intentionally zero because no data capture form exists)
4. Take a screenshot of this results chart and save it as `screenshots/09-campaign-1-results-dashboard.png`.

---

### Step 4.6: Record Data in the Results CSV
1. Open [results/campaign-comparison-template.csv](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/results/campaign-comparison-template.csv).
2. Enter the numbers you recorded during your actual run into the `Campaign_1_Baseline` column.
3. Compute the baseline Click-Through Rate:
   $$\text{Baseline CTR} = \left(\frac{\text{Clicked}}{\text{Delivered}}\right) \times 100$$

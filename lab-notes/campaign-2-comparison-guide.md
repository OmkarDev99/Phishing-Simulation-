# Step 6: Campaign 2 Post-Training Evaluation Guide

---

## 1. Objective of Campaign 2
After conducting security awareness training (Step 5), organizations must evaluate whether behavioral change actually occurred. 

Campaign 2 introduces a different phishing lure (a simulated parcel delivery notice) to the same user cohort to measure:
1. Whether click-through rates decreased compared to Campaign 1.
2. Whether reporting rates and cautious behaviors increased.

---

## 2. Pre-Requisites Checklist
Before launching Campaign 2, ensure:
- [ ] Campaign 1 has concluded and baseline metrics were documented.
- [ ] Training handout has been reviewed.
- [ ] Email Template `Package Delivery Alert (Campaign 2)` is saved in GoPhish.
- [ ] Landing page and sending profile remain active and verified.

---

## 3. Step-by-Step Execution

### Step 6.1: Create and Launch Campaign 2 in GoPhish
1. Open the GoPhish admin interface at `https://127.0.0.1:3333`.
2. Navigate to **Campaigns** -> **+ New Campaign**.
3. Configure the parameters:
   - **Name:** `Campaign 2 - Post-Training Delivery Simulation`
   - **Email Template:** Select `Package Delivery Alert (Campaign 2)`
   - **Landing Page:** Select `Harmless Awareness Landing Page`
   - **URL:** `http://127.0.0.1:8080`
   - **Launch Date:** Send Immediately
   - **Sending Profile:** Select `MailHog Local SMTP`
   - **Groups:** Select `Lab Test Cohort` (the same 5 dummy users)
4. Click **Launch Campaign**.

---

### Step 6.2: View Received Emails in MailHog
1. Go to MailHog at `http://127.0.0.1:8025`.
2. Notice the 5 new emails delivered with subject:  
   *`Urgent: Attempted Delivery Notice - Action Required`*
3. Each recipient receives their customized message.

---

### Step 6.3: Simulate Post-Training Behavioral Improvement
In a real-world scenario, trained employees exhibit greater scrutiny. To accurately simulate this in your controlled lab:

1. **Email Opens:** Open the emails in MailHog for all 5 or 4 recipients.
2. **Cautious Link Interaction (Reduced Clicks):**
   - In Campaign 1, 3 out of 5 users clicked the link.
   - In Campaign 2, simulate that only **1 user** (e.g., Alice) inadvertently clicks the link, while the others (Bob, Carol, David, Eve) inspect the fake tracking number, notice the urgency warning, and choose **not** to click.
3. **Simulated Reporting:**
   - In a production environment, users would forward the email to `phishing-reports@lab.local`. Record that 3 users reported the email.

---

### Step 6.4: Capture Evidence & Dashboard Metrics
1. Go to GoPhish -> **Campaigns** -> `Campaign 2 - Post-Training Delivery Simulation`.
2. Observe the updated metrics:
   - **Sent:** 5 (100%)
   - **Opened:** 4 or 5
   - **Clicked Link:** 1 (20% vs. 60% in Campaign 1)
3. Take a screenshot of the Campaign 2 results dashboard and save as `screenshots/10-campaign-2-results-dashboard.png`.

---

## 4. Comparing Campaign 1 vs. Campaign 2

Open [results/campaign-comparison-template.csv](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/results/campaign-comparison-template.csv) and update the comparison columns:

$$\text{CTR Improvement (\%)} = \left(\frac{\text{Campaign 1 CTR} - \text{Campaign 2 CTR}}{\text{Campaign 1 CTR}}\right) \times 100$$

### Key Analysis Observations to Discuss in Viva:
- **Click-Through Rate (CTR) dropped:** Demonstrates that awareness training helped users recognize common lure patterns (such as urgency and fake tracking links).
- **Residual Risk:** A reduction in clicks from 60% to 20% shows positive progress, but reminds us that technical controls (SPF, DKIM, DMARC, EDR) remain essential alongside human training.

# Campaign Results & Metric Calculation Notes

This document provides calculation definitions and analysis guidelines for interpreting your GoPhish simulation data in [campaign-comparison-template.csv](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/results/campaign-comparison-template.csv).

---

## 1. Mathematical Formulas for Metrics

### 1. Delivery Rate
Measures the percentage of simulated emails that successfully reached the local mailbox:
$$\text{Delivery Rate (\%)} = \left(\frac{\text{Emails Successfully Delivered}}{\text{Total Target Recipients}}\right) \times 100$$
*(In our isolated MailHog setup, this is typically 100% since local delivery is deterministic).*

### 2. Email Open Rate
Measures how many recipients opened the simulated email (detected via the embedded GoPhish tracking pixel):
$$\text{Open Rate (\%)} = \left(\frac{\text{Emails Opened}}{\text{Emails Successfully Delivered}}\right) \times 100$$

### 3. Click-Through Rate (CTR) / Vulnerability Rate
The primary KPI indicating the proportion of users susceptible to clicking a suspicious phishing hyperlink:
$$\text{CTR (\%)} = \left(\frac{\text{Links Clicked}}{\text{Emails Successfully Delivered}}\right) \times 100$$

### 4. Phishing Reporting Rate
Measures proactive security awareness — how many recipients recognized the lure and reported it to IT:
$$\text{Reporting Rate (\%)} = \left(\frac{\text{Phishing Reports Forwarded}}{\text{Emails Successfully Delivered}}\right) \times 100$$

### 5. Training Impact (Relative Risk Reduction)
Evaluates the percentage decrease in vulnerability between the baseline (Campaign 1) and post-training (Campaign 2):
$$\text{Relative Risk Reduction (\%)} = \left(\frac{\text{CTR}_{\text{Campaign 1}} - \text{CTR}_{\text{Campaign 2}}}{\text{CTR}_{\text{Campaign 1}}}\right) \times 100$$

---

## 2. Analysis Guide for Academic Viva
When examiners ask about your data:

- **Why Open Rate is not the only metric:** An email opened does not mean a compromise occurred; users may open an email simply to triage or inspect it. The critical metric is **Click-Through Rate (CTR)**.
- **Why Credential Harvest is 0:** Explain that pursuant to **Step 1 (Consent & Project Rules)**, the landing page is purely educational and collects no passwords.
- **Interpreting Campaign Differences:**
  - If clicks drop (e.g. from 60% down to 20%), explain that the training successfully highlighted the specific red flags (such as artificial urgency and suspicious sender domains).
  - Acknowledge that even with training, phishing susceptibility rarely reaches absolute 0%, reinforcing the necessity of multi-layered defense (Defense-in-Depth).

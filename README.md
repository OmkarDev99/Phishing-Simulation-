# Phishing Simulation and Security Awareness Program
**Cybersecurity Academic Mini-Project (Windows Environment)**

A safe, beginner-friendly, and ethical security awareness lab built using **GoPhish** and **MailHog** on Windows. This project provides a complete lifecycle for simulating phishing attacks, measuring human vulnerability, delivering targeted awareness training, and documenting the measurable reduction in risk for college examinations and viva voce.

---

## 📁 Project Directory Structure

```text
Phishing-Awareness-Project/
│
├── index.html                                 <- Hosted Security Awareness Portal (GitHub Pages)
├── README.md                                  <- Main project guide, workflow & checklist
│
├── lab-notes/                                 <- Lab manuals & step-by-step guides
│   ├── project-rules.md                       <- Step 1: Ethical rules, consent & authorization
│   ├── gophish-mailhog-setup.md               <- Step 2: Windows installation & setup guide
│   ├── campaign-1-baseline-guide.md           <- Step 4: Baseline simulation execution guide
│   └── campaign-2-comparison-guide.md         <- Step 6: Post-training evaluation guide
│
├── email-templates/                           <- Harmless email lures & landing page
│   ├── README.md                              <- Instructions for importing into GoPhish
│   ├── it-security-update.html                <- Step 3: Template 1 (Simulated IT update, HTML)
│   ├── it-security-update.txt                 <- Step 3: Template 1 (Plain text version)
│   ├── package-delivery-alert.html            <- Step 3: Template 2 (Delivery reschedule, HTML)
│   ├── package-delivery-alert.txt             <- Step 3: Template 2 (Plain text version)
│   └── landing-page-educational.html          <- Step 3: Educational demonstration landing page
│
├── training-material/                         <- User awareness & education resources
│   ├── phishing-awareness-handout.md          <- Step 5: Student / employee training handout
│   ├── phishing-awareness-handout.html        <- Step 5: Printable HTML version of handout
│   ├── phishing-awareness-quiz.html           <- Step 5: Interactive knowledge check quiz (randomized)
│   └── training-presentation-notes.md         <- Step 5: Speaker notes & slides for viva presentation
│
├── results/                                   <- Simulation metrics & analysis
│   ├── campaign-comparison.csv                <- Auto-synced GoPhish campaign comparison metrics
│   ├── campaign-comparison-template.csv       <- Excel CSV template comparing Campaign 1 vs 2
│   └── results-analysis-notes.md              <- Formulas, KPIs & viva interpretation notes
│
├── scripts/                                   <- Automation & telemetry scripts
│   ├── README.md                              <- GoPhish API updater usage and troubleshooting
│   └── update_campaign_results.py             <- Automatic GoPhish metrics sync script
│
├── report/                                    <- Final project documentation
│   └── final-project-report-template.md       <- Step 7: Complete academic mini-project report
│
└── screenshots/                               <- Evidence directory for lab screenshots
    └── README.md                              <- Screenshot checklist & naming guide
```

---

## 📋 7-Step Implementation Checklist

Use this checklist to track your lab progress:

- [x] **Step 1: Consent & Project Rules**
  - [x] [lab-notes/project-rules.md](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/lab-notes/project-rules.md) created.
  - [x] Ethical scope defined: localhost-only, dummy accounts, no real password collection.

- [ ] **Step 2: GoPhish & MailHog Setup (Manual Download & Run)**
  - [x] [lab-notes/gophish-mailhog-setup.md](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/lab-notes/gophish-mailhog-setup.md) created with official links.
  - [ ] Download `MailHog_windows_amd64.exe` from [MailHog Releases](https://github.com/mailhog/MailHog/releases).
  - [ ] Download `gophish-v...-windows-64bit.zip` from [GoPhish Releases](https://github.com/gophish/gophish/releases).
  - [ ] Run MailHog (SMTP port 1025, Web UI port 8025).
  - [ ] Run GoPhish, extract initial admin password, log into `https://127.0.0.1:3333`.
  - [ ] Configure Sending Profile pointing to `127.0.0.1:1025` and send test email.

- [x] **Step 3: Harmless Phishing Email Templates & Landing Page**
  - [x] [email-templates/it-security-update.html](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/email-templates/it-security-update.html) (IT Security Update).
  - [x] [email-templates/package-delivery-alert.html](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/email-templates/package-delivery-alert.html) (Package Delivery Alert).
  - [x] [email-templates/landing-page-educational.html](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/email-templates/landing-page-educational.html) (Harmless educational landing page).
  - [ ] Import templates and landing page into GoPhish.

- [ ] **Step 4: Campaign 1 Baseline Simulation**
  - [x] [lab-notes/campaign-1-baseline-guide.md](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/lab-notes/campaign-1-baseline-guide.md) created.
  - [ ] Create User Group (`Lab Test Cohort` with 5 dummy accounts).
  - [ ] Launch Campaign 1 with IT Security template.
  - [ ] Observe emails in MailHog (`http://127.0.0.1:8025`).
  - [ ] Simulate baseline interactions (opens & clicks).
  - [ ] Record baseline figures in [results/campaign-comparison-template.csv](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/results/campaign-comparison-template.csv).
  - [ ] Capture screenshots `07`, `08`, and `09`.

- [ ] **Step 5: Security Awareness Training Module**
  - [x] [training-material/phishing-awareness-handout.md](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/training-material/phishing-awareness-handout.md) created.
  - [x] [training-material/phishing-awareness-handout.html](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/training-material/phishing-awareness-handout.html) created for printing/viewing.
  - [x] [training-material/phishing-awareness-quiz.html](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/training-material/phishing-awareness-quiz.html) created with randomized questions and options for interactive knowledge check.
  - [x] [training-material/training-presentation-notes.md](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/training-material/training-presentation-notes.md) prepared for presentation.
  - [ ] Deliver awareness training and conduct knowledge check quiz with cohort.

- [ ] **Step 6: Campaign 2 Post-Training Evaluation**
  - [x] [lab-notes/campaign-2-comparison-guide.md](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/lab-notes/campaign-2-comparison-guide.md) created.
  - [ ] Launch Campaign 2 with Package Delivery template.
  - [ ] Simulate post-training interaction (fewer clicks, simulated incident reporting).
  - [ ] Fill post-training columns in [results/campaign-comparison-template.csv](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/results/campaign-comparison-template.csv).
  - [ ] Capture screenshot `10`.

- [ ] **Step 7: Final Report & Viva Preparation**
  - [x] [report/final-project-report-template.md](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/report/final-project-report-template.md) created with placeholders.
  - [ ] Insert your name, college details, and recorded numbers into the report.
  - [ ] Verify screenshot links and review the Viva Q&A section (Section 8).

---

## ⚡ Quickstart Summary (For You)

1. **Keep it Local & Safe:**  
   Always run GoPhish and MailHog on your local PC. MailHog acts as a safe sinkhole—no external emails will ever be sent.
2. **Never Collect Passwords:**  
   The landing page is strictly educational and does not contain any input fields for credentials.
3. **Step-by-Step Flow:**  
   Read [lab-notes/gophish-mailhog-setup.md](file:///c:/Users/PC/Desktop/Phishing-Awareness-Project/lab-notes/gophish-mailhog-setup.md) to download and launch the tools, then follow the guides in order.

---

## 🎓 Viva Voce Highlights
If the examiner asks:
- **"Why use MailHog instead of Gmail/Outlook SMTP?"**  
  *Answer:* MailHog ensures complete network isolation on localhost port 1025. No packets leak outside the local machine, preventing spam blacklisting and eliminating ethical/legal liabilities.
- **"How does awareness training help if technical filters exist?"**  
  *Answer:* Social engineering exploits human trust and urgency rather than software bugs. The SLAM framework (Sender, Links, Attachments, Message) empowers users as a human detection layer (human sensors).

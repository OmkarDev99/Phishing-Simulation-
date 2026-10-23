# Security Awareness Training — Presentation & Viva Notes

These speaker notes accompany the Phishing Awareness Handout. Use them when presenting your mini-project to examiners or conducting an awareness session.

---

## Slide 1: Introduction & Threat Landscape
- **Talking Points:**
  - Over 85% of cybersecurity breaches involve a human element (phishing, social engineering).
  - Firewalls, antivirus, and spam filters catch known signatures, but attackers constantly evolve lures.
  - The human user is the final line of defense; security awareness training transforms employees into human sensors.

---

## Slide 2: Why Phishing Works (Psychological Triggers)
- **Talking Points:**
  - Attackers don't hack systems; they hack human emotions:
    1. **Urgency:** Creating time pressure so critical evaluation is bypassed.
    2. **Authority:** Impersonating executives or IT administrators.
    3. **Fear / Loss Aversion:** Threatening account suspension, fines, or disciplinary actions.
    4. **Curiosity:** Promising gifts, bonuses, or delivery updates.

---

## Slide 3: Practical Defense — The SLAM Method
- **Talking Points:**
  - Introduce the SLAM checklist: Sender, Links, Attachments, Message.
  - Walk through how to inspect sender email headers and hover over hyperlinks.
  - Remind the audience that IT departments will **never** ask for a password via an email link.

---

## Slide 4: Positive Reporting Culture & Incident Response
- **Talking Points:**
  - Phishing awareness is not about punishment; fear of reporting leads to hidden breaches.
  - Faster incident reporting enables security teams to block sender domains and isolate infected nodes before lateral movement occurs.
  - **What to do if you click a link:** Immediately report it to the IT/security team and follow their instructions. Disconnect network cables/Wi-Fi if advised, and change credentials from a separate clean system.
  - **Reporting Channel:** In real environments, use official corporate report buttons or security desk emails. Remind examiners that `phishing-reports@lab.local` in our lab notes is only a simulated placeholder address unless a real lab mailbox has been configured.

---

## Slide 5: Viva Voce & Quick Q&A Preparation
- **Talking Points:**
  - **Q1: What does SLAM stand for?**  
    *Answer:* **S**ender, **L**inks, **A**ttachments, and **M**essage.
  - **Q2: Why use MailHog and GoPhish locally?**  
    *Answer:* It creates a completely isolated lab environment where dummy recipients receive test emails without sending traffic over the internet or collecting real passwords.
  - **Q3: What is the main goal of Step 5?**  
    *Answer:* Deliver clear, actionable security training so users can spot phishing red flags before Campaign 2 is evaluated.

---

## Facilitator Guide: Presenting the Interactive Quiz
When conducting the interactive knowledge check session using `phishing-awareness-quiz.html`:
1. **Read First:** Ask participants to review the *Phishing Awareness Handout* first to familiarize themselves with key concepts.
2. **Answer Independently (Randomized Rounds):** Have participants open the local quiz page. Both the question order and the multiple-choice options are dynamically randomized on initial load and whenever *Try Again* is clicked, ensuring each attempt is fresh and preventing rote memorization.
3. **Review Explanations Together:** Once participants click *Check Answers*, review the score feedback and the provided explanations together to discuss why each option is correct or dangerous.
4. **Privacy & Consent:** If tracking group training completion, record scores only if participants have given prior consent, and avoid collecting or storing any unnecessary personal information.

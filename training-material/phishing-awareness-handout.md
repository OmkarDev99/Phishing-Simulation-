# Phishing Awareness Training Handout
**Security Awareness & Defense Guide | Information Security Office**

---

> **Lab Purpose & Educational Note:**  
> This project operates in a safe, isolated local environment using GoPhish and MailHog. All simulations use fictitious dummy recipients, and the project strictly avoids any real password collection or data harvesting.

---

## What is Phishing?
Phishing is a social engineering cyber-attack where attackers impersonate legitimate organizations (such as IT departments, banks, couriers, or colleagues) via email or messaging to deceive individuals into revealing sensitive credentials, clicking dangerous links, or transferring funds.

---

## The 4 Core Red Flags of Phishing

### 1. Suspicious Senders (Identity Deception)
Attackers frequently disguise their true sender identity:
- **Display Name Spoofing:** The sender name looks familiar (e.g., *"IT Support Helpdesk"*), but the actual email address is completely different (e.g., `helpdesk@random-external-domain.com`).
- **Domain Typo-Squatting:** Attackers register subtle variations of legitimate brand domains (e.g., `paypa1.com` instead of `paypal.com`, or `micros0ft-login.com`).
- **Free Webmail Domains:** Official corporate communications will never come from `@gmail.com`, `@yahoo.com`, or `@outlook.com`.

### 2. Urgent or Coercive Language (Psychological Pressure)
Phishing emails deliberately create a sense of panic or rush so victims act before thinking:
- **Threat of Penalties:** *"Your account will be suspended within 24 hours unless you verify."*
- **Financial Urgency:** *"Overdue invoice #8921 requires immediate settlement to avoid legal action."*
- **False Opportunities:** *"You have an uncollected parcel waiting / You won a company bonus."*

### 3. Deceptive & Unsafe Hyperlinks
Never trust the text written inside a link or on a button:
- **Hover Inspection:** Always hover your mouse pointer over any link or button *before clicking* to reveal the true URL destination in your browser's bottom status bar.
- **Mismatched Destinations:** If the button text displays `https://mycollege.edu/login` but the actual link points to `http://192.168.1.55/update`, it is a malicious trap.
- **Shortened URLs:** Avoid unverified short links (e.g., `bit.ly`, `tinyurl`) in official work correspondence.

### 4. Dangerous Attachments
Malicious attachments can install malware, keyloggers, or ransomware onto your workstation:
- **High-Risk File Types:** Watch out for `.exe`, `.scr`, `.bat`, `.vbs`, `.iso`, or `.zip` files from unknown senders.
- **Double File Extensions:** Attackers frequently disguise executables using names like `Annual_Salary_Review.pdf.exe`.
- **Macro Requests:** Legitimate Word or Excel documents do not require you to "Enable Macros" or "Enable Content" to view their text.

---

## The "SLAM" Verification Checklist
Before interacting with any unexpected email, apply the **SLAM** inspection method:

| Letter | Check | What to Verify |
|---|---|---|
| **S** | **Sender** | Does the email address match the official organization domain? |
| **L** | **Links** | Did you hover over the link to verify where it really directs? |
| **A** | **Attachments** | Were you expecting this attachment? Is the file type safe? |
| **M** | **Message** | Is the tone unusually urgent, coercive, or asking for sensitive credentials? |

---

## How to Report a Phishing Email
If you identify a suspected phishing email:

1. **DO NOT** click any links, open attachments, or reply to the sender.
2. **DO NOT** forward the email to colleagues or friends (this spreads the risk).
3. **DO** report the email to your organization's official reporting channel (such as the *Report Phishing* button in your email client or your IT security team's designated contact).  
   *(Note: The address `phishing-reports@lab.local` mentioned in lab notes is only a simulated placeholder address unless a real lab mailbox has been configured. Always use your organization's official reporting channel).*
4. If you accidentally clicked a link or entered credentials:
   - Report it promptly to the IT/security team and follow their instructions.
   - Disconnect your computer from the network immediately if advised.
   - Change your password from an alternate, clean device.

---

## Quick Self-Check Quiz (Viva & Discussion)

1. **Question:** What does SLAM stand for?  
   *Answer:* **S**ender, **L**inks, **A**ttachments, and **M**essage.

2. **Question:** What should someone do after accidentally clicking a suspicious link?  
   *Answer:* Report it promptly to the IT/security team and follow their instructions.

3. **Question:** An email from "IT Helpdesk" states your password expires in 2 hours and links to an external login page. What should you do?  
   *Answer:* Do not click. Open your web browser manually, go directly to your official IT portal, or call the IT desk directly to verify.

4. **Question:** Why do attackers use urgent deadlines in phishing emails?  
   *Answer:* To induce panic and bypass the victim's rational critical thinking.

5. **Question:** Can a safe-looking `.pdf` file actually be malicious?  
   *Answer:* Yes, through double extensions (`invoice.pdf.exe`) or embedded malicious links and PDF exploits.


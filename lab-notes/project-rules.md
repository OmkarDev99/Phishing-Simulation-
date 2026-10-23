# Step 1: Consent and Project Rules Document

**Project Name:** Phishing Simulation and Security Awareness Program  
**Scope:** Controlled Academic Mini-Project & Educational Cybersecurity Demonstration  
**Environment:** Localhost Isolated Testbed (Windows)  

---

## 1. Purpose & Ethical Charter
This project is conducted exclusively for academic research, security awareness training, and college examination purposes. Social engineering simulations carry ethical and legal responsibilities; therefore, this experiment adheres strictly to the principles of harmlessness, informed authorization, and data privacy.

---

## 2. Mandatory Rules of Engagement

### Rule 1: Strictly Local Authorization
- All tests are confined strictly to `127.0.0.1` (localhost) using a local dummy mailcatcher (MailHog) and a local simulation server (GoPhish).
- Under no circumstances will phishing emails be transmitted across the public Internet, to university domains, or to external corporate mail servers.
- No real or unsuspecting human subjects will be targeted without prior explicit written consent and ethical approval.

### Rule 2: Exclusively Dummy Data
- All user profiles, employee names, and email accounts used in the simulation are fictitious test fixtures (e.g., `user1@lab.local`, `alice.smith@lab.local`).
- No personal contact lists, university student directories, or live corporate directories may be imported into the simulation software.

### Rule 3: Zero Real Credential Harvesting
- Phishing templates created in this project **MUST NEVER** contain functional credential harvesting forms, input fields for real passwords, PIN numbers, or credit card information.
- All simulated links direct users exclusively to a harmless, local educational awareness landing page explaining that the interaction was a drill and highlighting the red flags.

### Rule 4: Data Privacy and Confidentiality
- No tracking cookies, system surveillance tools, or external telemetry are embedded in email templates.
- Any metrics captured (e.g., email opened, link clicked) are stored solely within the local GoPhish SQLite database on the researcher's local machine and will not be shared externally.

### Rule 5: Non-Punitive Educational Objective
- The objective of security awareness is education, not embarrassment or punishment.
- In any real-world extension of this work, results must be aggregated anonymously to measure institutional risk trends rather than to single out specific individuals.

---

## 3. Legal and Academic Compliance
This project aligns with common cybersecurity legal frameworks and ethical research guidelines:
- **Computer Misuse Regulations:** By restricting all traffic to an isolated, non-routable dummy test network, this project does not violate computer misuse laws or anti-spam legislation (e.g., CAN-SPAM, IT Act).
- **Academic Integrity:** The simulation data presented in the report must be generated honestly through actual controlled runs in the lab environment without fabrication.

---

## 4. Viva Voce Key Defense Points
When defending this project before examiners:
1. **Explain the ethical boundary:** Point out that you used MailHog as an SMTP sinkhole so not a single packet escaped onto the campus network or internet.
2. **Explain why passwords were not collected:** State that NIST SP 800-50 and standard security awareness frameworks recommend immediate just-in-time education over offensive credential theft.
3. **Showcase authorization:** Emphasize that controlled security simulations require clear Rules of Engagement (RoE) prior to launch.

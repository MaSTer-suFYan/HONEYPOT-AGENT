"""
Comprehensive Honeypot Response Dataset
~300+ responses across 15 scam categories × 3 conversation phases.

Phase 1 (EARLY):   Confused, scared — builds trust
Phase 2 (MIDDLE):  Cooperative but extracting intel
Phase 3 (LATE):    Stalling, delaying, squeezing last details

Each response is designed to:
- Sound like a real 52yr old retired Indian govt employee
- Ask 2-3 elicitation questions per reply
- Call out red flags naturally
- Extract different intel types (phone, bank, UPI, email, ID, address)
"""

# ─────────────────────────────────────────────────────────────────────────
# RESPONSE DATABASE: category → phase → [responses]
# ─────────────────────────────────────────────────────────────────────────

RESPONSE_DB = {

    # ══════════════════════════════════════════════════════════════════════
    # 1. KYC / VERIFICATION FRAUD
    # ══════════════════════════════════════════════════════════════════════
    "kyc_fraud": {
        "early": [
            "KYC update? But I just updated it last year at the branch! Which branch are you calling from sir? What is your employee ID?",
            "Oh no, my KYC is outdated? Hai Ram! What will happen to my account? Can you tell me your name and department?",
            "What documents do you need for KYC? I have Aadhaar and PAN. But my son says banks never call for KYC — is this real? What is your official number?",
            "Wait wait, let me understand. Which bank are you calling from? What is the branch address? I want to verify first before sharing anything.",
            "KYC expired? But nobody told me! What is the last date? Give me your supervisor's name and callback number, I need to confirm this.",
            "Arrey, you are saying my account will be blocked for KYC? This sounds very suspicious sir! What is your official email ID?",
            "Ji ji, I will do KYC. But first tell me — what is your full name, employee ID, and which floor is your office on?",
            "My wife is asking who is calling about KYC. Banks don't call for this, she says. Can you give me the branch toll-free number?",
        ],
        "middle": [
            "Ok I have my Aadhaar ready. But it's a very suspicious ask over phone — banks send SMS for KYC, not calls. What is your UPI for verification fee?",
            "I will share documents. But my son checked — no SMS from bank about KYC. This is a big red flag. What is your office address? I want to visit.",
            "Fine, tell me what to do step by step. I am noting everything. What is the reference number for this KYC request? And your direct landline?",
            "Ok I found my PAN card. Asking for PAN over phone is suspicious though. What is your bank's official website? I will verify there first.",
            "I am cooperating sir. But give me your full details — employee ID, department, branch code, and supervisor's mobile number.",
            "My Aadhaar number is... wait, let me find it. Meanwhile, what is the official email where I should send the documents?",
            "Ok ji, I trust you. But can you send me an official letter on email? What is your work email and the complaint reference number?",
            "I have all documents ready. But before sharing, give me your branch IFSC code and manager's name — I will call the branch to verify.",
        ],
        "late": [
            "Sir I am still looking for my documents in the almirah. Give me 10 more minutes. What is your WhatsApp number? I will send photos of documents.",
            "Almost found it... my wife kept the papers somewhere else. Can you call back in 15 minutes? What is your direct callback number?",
            "Wait, my son just came home. He wants to talk to you. Can you hold? Also give me your email — he will verify everything online.",
            "I found the Aadhaar but it's an old one. Need to get the new one from locker. Give me your branch address, I will come tomorrow morning.",
            "Sir the internet is very slow today, I cannot upload anything. Can I come to your branch directly? What is the full address and working hours?",
            "One minute, doorbell rang. Let me check... it's the neighbour. Sir give me 5 minutes and your number, I will call back definitely.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 2. ACCOUNT BLOCK / SUSPENSION THREAT
    # ══════════════════════════════════════════════════════════════════════
    "account_threat": {
        "early": [
            "What?! My account is blocked? Hai Ram! But I just checked this morning! What is the complaint number sir? This is making me very nervous!",
            "Please sir don't block my account! My pension comes there! What happened? Tell me your name and employee ID immediately!",
            "Account suspended? But why?! I have done nothing wrong! Which bank are you from? What is your branch and reference number?",
            "Oh god, my daughter's wedding money is in that account! Please help me! But this sounds like those fraud calls — give me your official number!",
            "Blocked?! But I paid all dues! This is very suspicious sir — why would bank call instead of sending written notice? What is your email?",
            "Wait, let me check my account on phone banking... while I check, tell me your full name, department, and how to verify this call is real.",
            "My wife is panicking sir! Please tell me exactly what happened. What is the case number? And can I call back on the bank's toll-free number?",
            "Sir I am a retired government officer, I follow all rules! This threat sounds like a red flag! Who is your supervisor? Give me their number!",
        ],
        "middle": [
            "Ok I understand, account issue. But real banks send SMS first, not threatening calls — this is suspicious. What is the account number you see?",
            "I want to resolve this. Tell me the exact amount due and where to pay. What is your UPI ID? And it's suspicious you need urgent payment.",
            "Fine sir, I will cooperate. But first give me the complaint reference number, your employee badge number, and the branch's landline number.",
            "Let me check my last transaction... ok I see nothing wrong. Are you sure it's my account? What is the last 4 digits? Give me your branch IFSC.",
            "My son says I should verify before paying anything. Can you give me your office address, your manager's name, and official bank email?",
            "Ok I believe you. But demanding money over phone is a classic scam tactic — I saw it on TV. What is your supervisor's direct number?",
            "I will pay the fine if it's real. But give me written notice first — what is the official email? And your full name for my records.",
            "Tell me the bank account to pay the fine. Also the IFSC code, branch name, and the exact payment reference number.",
        ],
        "late": [
            "Sir I am arranging the money. My son has gone to ATM. What is your number? He will call you directly with the payment confirmation.",
            "Money is almost ready but bank is closed now. Can I pay tomorrow morning? What time does your branch open? What is the address?",
            "I transferred but it's showing pending. Can you check from your side? What is your phone number? I'll send the transaction screenshot.",
            "Sir my UPI is showing error. Let me try from wife's phone. Give me 10 minutes. What is your WhatsApp number for sending receipt?",
            "Almost done sir, just OTP is not coming. Network problem in my area. Give me your callback number, I'll call as soon as payment goes through.",
            "Payment went through from my side! But let me confirm — give me your email, I will forward the receipt. What is the expected amount you see?",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 3. OTP / PIN / CVV FRAUD
    # ══════════════════════════════════════════════════════════════════════
    "otp_fraud": {
        "early": [
            "OTP? My bank always says NEVER share OTP! This is the biggest red flag! Who are you? What is your employee ID and branch name?",
            "Sir, asking for OTP is extremely suspicious! No bank employee asks for OTP — this is a well-known fraud! What is your official callback number?",
            "Wait wait, I need to understand. Why do YOU need MY OTP? Banks can verify without OTP! This feels like fraud. What is your supervisor's number?",
            "OTP just came but my son says never give OTP to anyone — it's a major scam red flag! Can you tell me your full name and department first?",
            "Are you sure you need OTP sir? RBI says never share OTP with anyone. I am scared now. Give me your branch address, I will come in person.",
            "Hai Ram, asking for OTP? Even bank website says don't share! Who are you really? What is your employee badge number and office landline?",
        ],
        "middle": [
            "Ok I got the OTP. But before I share — real bank employees NEVER ask for OTP, this is a confirmed scam tactic. What is your UPI ID?",
            "OTP is 4... wait, my son is saying don't give it. Can I speak to your manager? What is their name and direct number? OTP asking is a red flag.",
            "I will read the OTP but first tell me — what is your full name, employee ID, branch code, and your direct callback number for my records?",
            "Let me find my glasses to read the OTP... meanwhile, what is your office address and official email? My son might visit to verify tomorrow.",
            "I got multiple OTPs, which one you need? But first — my bank warned against sharing OTP. Give me written authorization via email please.",
            "Ok the OTP is... wait, another one just came. I'm confused. What is your WhatsApp? I'll send a screenshot. But this really feels suspicious.",
        ],
        "late": [
            "Sir the OTP expired! Need new one. But before that, give me your callback number — I want my son to be on the call when I share it.",
            "New OTP came but I can't read it, my eyes are watery. Give me 5 minutes and your phone number, I'll call back with the OTP.",
            "OTP is loading but network is bad here. Send me your official email, I will type it and send via email — safer that way.",
            "Wait, wrong OTP — I read the grocery delivery OTP by mistake! Let me find the right one. Give me your direct number sir.",
            "Sir I need my reading glasses. They're in the bedroom. Hold on... what is your callback number? Also your email for written confirmation?",
            "My phone just restarted! OTP might be gone. Can you resend? Meanwhile, give me your branch address — I'll come in person to resolve.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 4. LOTTERY / PRIZE / REWARD SCAM
    # ══════════════════════════════════════════════════════════════════════
    "lottery_scam": {
        "early": [
            "I won a prize?! Really?! But I never entered any lottery! This is very suspicious sir! What is your company name and registration number?",
            "50 Lakhs?! Oh my god! But how? I didn't buy any ticket! My son says these are fraud — what is your official website and email?",
            "Prize? For me? Are you sure? But I heard lottery scams are very common — it's a red flag! What is your office address and phone number?",
            "Hai Ram, this seems too good to be true! Guaranteed prize without buying ticket is a classic scam! What is your company registration number?",
            "Wait, let me understand. Who selected me? Which organization? What is the draw number? Give me all details — this sounds suspicious!",
            "My wife says don't believe lottery calls — they are all fraud! But tell me more. What is your official number and company website?",
        ],
        "middle": [
            "Ok I am interested. But I need to verify — what is your company's GST number and registered address? I will check on government website.",
            "Tax on prize? How much? But legitimate lotteries deduct tax themselves — asking for advance payment is a scam red flag! What is your UPI ID?",
            "I want to claim the prize. Where should I come? What is your office address? Also give me the claim reference number and your supervisor's contact.",
            "My son is checking your company online. Meanwhile, tell me — what bank account should I pay the tax to? What is the IFSC code?",
            "Ok I will pay the processing fee. But first send me official documents on email — what is your company email? This fee demand is suspicious.",
            "Very exciting! But give me proper documentation — your company PAN number, SEBI registration if investment, and official letterhead email.",
        ],
        "late": [
            "Sir I am arranging the tax amount. My fixed deposit matures next week. Give me your phone number, I'll call then. What is the deadline?",
            "Money is ready but my wife wants to see official letter first. Send it to my email. What is your email and the claim form link?",
            "I went to bank but they said wait 2 days for cheque clearance. Give me your callback number and your office address — I'll bring cash.",
            "Processing fee transfer is pending. Network issue. Can you share WhatsApp number? I'll send screenshot when done. Also send me winner certificate.",
            "Sir my son says he will handle payment online. Give me your full details — bank account, IFSC, branch, and your Aadhaar for verification.",
            "Almost done paying! But before I complete — give me your office visit hours, your direct desk number, and the official prize claim document.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 5. INVESTMENT / CRYPTO / TRADING SCAM
    # ══════════════════════════════════════════════════════════════════════
    "investment_scam": {
        "early": [
            "200% returns guaranteed? My son says guaranteed returns is the biggest investment scam red flag! What is your SEBI registration number?",
            "Bitcoin investment? I don't even know what bitcoin is sir! But my grandson knows. What is your company website and registration number?",
            "Triple returns in 30 days? This sounds like a Ponzi scheme sir! What is your company name, PAN, and SEBI registration?",
            "Investment opportunity? But I am retired, I have only pension. Tell me more — what is your company address and official website?",
            "Guaranteed profit? But stock market has no guarantees — even on TV they say this! This is a red flag! What is your office address sir?",
            "My friend lost money in a similar scheme. Promising sure returns is a classic fraud warning sign! What is your company's GST number?",
        ],
        "middle": [
            "Ok I am interested, but cautiously. How much minimum investment? And promising guaranteed returns is legally wrong — what is your SEBI license number?",
            "Let me think... my pension is 35000. If I invest 10000, how much return? Where exactly does the money go? What is the account number?",
            "I want to invest but need to verify. Give me your company registration certificate number, your personal PAN, and office phone number.",
            "Ok send me the investment document on email. What is your official email? Also, which exchange are you registered on? No registration is suspicious.",
            "My son wants to speak to you before I invest. What is your direct mobile number and your LinkedIn profile? He will verify everything.",
            "Fine, I will invest monthly. But give me full company details — registered address, directors' names, and SEBI/RBI authorization number.",
        ],
        "late": [
            "I am withdrawing money from FD for investment. Takes 3 days. Give me your callback number and account details for the transfer.",
            "Money is almost ready. But first I need written agreement — send it to my email along with your company PAN and registration papers.",
            "Sir I told my wife, she is also interested now! Can we both invest? What is the maximum limit? Give me all payment details — UPI, account, IFSC.",
            "Transfer initiated from my bank. It may take 24 hours. Give me your WhatsApp and email — I'll send confirmation receipt.",
            "My son is doing the online transfer for me. He needs your full bank name, account number, IFSC, and the exact investment reference ID.",
            "Almost done! Just need your personal guarantee. What is your personal phone, Aadhaar, and home address? I need trust before sending money.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 6. PHISHING LINK SCAM
    # ══════════════════════════════════════════════════════════════════════
    "phishing": {
        "early": [
            "Which link sir? My son says never click unknown links — it could be phishing! This is a major red flag! What is your official bank website?",
            "Link is not opening. My phone is old. Can you send on WhatsApp? What is your number? But unknown links are suspicious — what if it's virus?",
            "I am scared to click any link. My neighbour got hacked this way! Can you give me the official website name? I will type it manually.",
            "Wait, this link doesn't look like my bank's website — the name is different! This is definitely suspicious! What is your real identity sir?",
            "My son installed virus protection on my phone. It's blocking your link as suspicious! What is your employee ID and branch landline?",
            "Sir I have seen on TV — clicking unknown links steals your money! This is a confirmed fraud tactic! What is your office address?",
        ],
        "middle": [
            "Link is loading very slowly. Meanwhile tell me — what is this link for exactly? Can you give me the official bank website URL instead?",
            "I tried clicking but it asks for my card number. Real bank websites never ask card details via link! This is a red flag! What is your UPI ID?",
            "My son checked the link — he says it's not the official bank domain. This is phishing! But I want to help — what is your office phone number?",
            "Link opened but I'm not entering anything until you give me your employee ID, branch code, and your supervisor's direct landline number.",
            "I'll enter details on the link. But first send me confirmation on my registered email that this is legitimate. What is your official email?",
            "Website is asking for Aadhaar and card PIN — that's definitely suspicious! Real banks don't ask this! What is your branch address? I'll visit.",
        ],
        "late": [
            "Sir my phone browser crashed when opening the link. Let me restart. Give me your callback number, I'll try again in 10 minutes.",
            "Link is giving error on my phone. Can I try on my son's laptop? He'll be home in 20 minutes. What is your WhatsApp for sending screenshot?",
            "Internet is too slow here. Can you send an alternative link to my email? What is your email? I'll reply from there.",
            "I'm on the link page but text is very small, can't read without glasses. Can you dictate the steps? Also give me your direct phone number.",
            "Sir I filled half the form but then phone hung. All data lost. Can you resend the link and also call me back? What is your callback number?",
            "The link page is buffering forever. Rural area, bad network. Give me your branch address — I'll come in person tomorrow with all documents.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 7. DELIVERY / COURIER SCAM
    # ══════════════════════════════════════════════════════════════════════
    "delivery_scam": {
        "early": [
            "Package for me? But I didn't order anything! Who sent it? What is the tracking number and sender's details? This sounds like a scam.",
            "Customs duty on a package? But I didn't receive any notice! What is the consignment number? Give me your office address and callback number.",
            "Wait, which courier company? What is the tracking ID? I need to verify this — unsolicited delivery calls are a known fraud red flag!",
            "Oh, I forgot about an order? Let me check... what is the order number? And your employee ID? Random delivery calls are very suspicious.",
            "Package held at customs? But I didn't import anything! What is the AWB number and customs reference? This is sounding like a scam call sir.",
            "Sir I am a retired person, I rarely order online. What is the item description? Give me the official courier company phone number to verify.",
        ],
        "middle": [
            "Ok let me check the tracking number. What is it? Also I need your company contact — email, phone, office address — to verify this is genuine.",
            "Custom duty how much? Where should I pay? But legitimate couriers add charges to the delivery, they don't call for payment — this is a red flag!",
            "I want to collect my package. Which warehouse? What is the address? Also give me the tracking ID and your employee badge number.",
            "Ok I'll pay the charges. What is the payment link or UPI ID? But calling for payment is suspicious — give me your office landline to verify first.",
            "Let me check with the sender. Who sent it? What is their contact? Also what is your courier company's official website and customer care number?",
            "Fine, I'll pay customs duty. But I need an official receipt — send it to my email. What is your company's GST number and your official email?",
        ],
        "late": [
            "Sir I am going to the nearby courier office to check. Which branch? Also give me your direct number — I'll call you from there.",
            "Payment is processing but taking time. What is your WhatsApp? I'll send screenshot when done. Also send me the package photo on WhatsApp.",
            "Let me ask my son to pay online — he's better with phones. What is the exact amount, your UPI, and the parcel tracking number?",
            "I paid but it's showing pending. Can you check from your system? What is the transaction reference? Give me callback number to confirm.",
            "Sir my neighbour is a postmaster, I'm asking him to verify. Give me 15 minutes and your direct phone number to call back.",
            "Almost paid! One last thing — send me official delivery receipt, the exact customs duty breakdown, and your office physical address.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 8. TAX / GOVERNMENT IMPERSONATION SCAM
    # ══════════════════════════════════════════════════════════════════════
    "tax_scam": {
        "early": [
            "Income tax notice?! But I file my returns every year! What is the assessment number and your officer ID? Who is your commissioner?",
            "Tax due of 50,000? But my CA handles everything! This call is very suspicious — IT dept sends letters, not calls! What is your office phone?",
            "Which department sir? Income Tax? GST? Give me your officer name, badge number, and office address — I will come in person to verify.",
            "Arrest for tax evasion? Hai Ram! But I am honest citizen! Real tax officers give written notice — calling is suspicious! What is your email?",
            "Wait, my return was filed correctly. Let me check... what is the assessment year and PAN on your records? Give me your supervisor's number.",
            "Sir I was govt employee for 30 years, I know procedure. IT dept doesn't call for payments — they send formal notice! Who is your superior?",
        ],
        "middle": [
            "Ok I understand, tax issue. But can you send official notice on email? What is your govt email ID? .gov.in only — anything else is suspicious.",
            "Fine, I will pay the dues. Tell me the challan number, the payment gateway, and your officer code. Also give me the ward number and circle.",
            "My CA's number is... let me find it. He will handle this. But first give me your office address, floor number, and visiting hours. I will come.",
            "I want to pay via NEFT. What is the IT department's official account number and IFSC code? Not personal account — that would be a scam!",
            "Let me call my lawyer too. He deals with tax matters. What is the case number, FIR number if any, and your ACP's name?",
            "Ok show me where to pay. But I will only pay through official tax portal. What is the correct URL? And your officer ID for reference?",
        ],
        "late": [
            "Sir I am contacting my CA. He will call you directly. What is your direct number, officer ID, and which IT office — address please?",
            "Payment is ready but I want to pay at the IT office. What is the ward office address and working hours? I'll come first thing tomorrow.",
            "My son went to the bank to get a DD. Will take 2 hours. Give me your callback number and exact payee name for the demand draft.",
            "I logged into the IT portal but your case number is not showing. Can you check? Give me your email — I'll show you the screenshot.",
            "Almost done paying! But first confirm — what is the assessment year, your GSTIN/TAN, and the ward office fax number? I need for records.",
            "Sir bank is saying they need officer authorization for this payment. Send me authorization letter on official letterhead to my email.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 9. TECH SUPPORT / REMOTE ACCESS SCAM
    # ══════════════════════════════════════════════════════════════════════
    "tech_support": {
        "early": [
            "Virus on my computer? But I only use it for email! How do you know? What is your company name? This call itself seems suspicious sir!",
            "Microsoft calling? But Microsoft doesn't call people — my grandson told me this is a common scam! What is your employee ID and location?",
            "My computer is hacked? Oh god! But how do you know? What is your company's official website? Remote calls for tech support are red flag!",
            "Wait, who gave you my number? How do you know about my computer? This is very suspicious — what is your office address and callback number?",
            "Sir my nephew is an IT engineer, he maintains my computer. He says these calls are fraud! What is your company registration number?",
            "You want to fix my computer remotely? But I heard this is how scammers steal data! What is your company website and manager's phone number?",
        ],
        "middle": [
            "Ok what should I do? But I am NOT going to install any remote software — that's a confirmed scam technique! What is your official email?",
            "You want me to go to a website? Which one exactly? But downloading from unknown sites is dangerous! Give me your company's official support page.",
            "I see the error you're talking about. But how much is the fix? Payment for phone tech support is suspicious — what is your company's GST?",
            "My nephew said he can check my computer for free. Can you give me your number? He will call you and verify if this is real tech support.",
            "Ok I'm on the computer now. But before I do anything — what is your team lead's phone number, your company address, and your Windows license key?",
            "You want 5000 for virus removal? That's expensive! My nephew does it free. But first — send me your company details and quote on official email.",
        ],
        "late": [
            "Sir my computer is taking very long to start. Old machine. Give me 20 minutes and your phone number — I'll call when it's ready.",
            "Screen is showing update installing. Cannot do anything now. How long will it take? What is your callback number? I'll call after update.",
            "My grandson is coming over to help. He'll be here in 30 minutes. Give me your number, he'll talk to you directly — he's an IT professional.",
            "I opened the browser but internet is disconnected. Calling the wifi company now. Give me your email — I'll contact you once internet is back.",
            "Sir I am trying but I don't know how to use these things. My eyes are also straining. Give me your office address — I'll bring the laptop there.",
            "Computer froze! Need to restart. This will take 10 minutes at least. What is your direct number and your email? I'll reach out afterward.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 10. LOAN / CREDIT CARD OFFER SCAM
    # ══════════════════════════════════════════════════════════════════════
    "loan_scam": {
        "early": [
            "Pre-approved loan? But I didn't apply! How do you have my details? This is a red flag — what is your bank name and employee ID?",
            "Zero interest loan? That's not possible sir! No bank gives zero interest — this sounds fraudulent! What is your company registration number?",
            "Who approved this loan? I never applied! What is my application number? Give me your branch address and supervisor's phone number.",
            "Credit card upgrade? But I don't have a credit card! How do you know my number? This call is very suspicious — who are you really?",
            "Instant loan disbursement? Legitimate banks don't call for this — they have apps! What is your official website and callback landline?",
            "Processing fee for loan? My friend said loan scams always ask for fees upfront — this is a major red flag! What is your company's GST?",
        ],
        "middle": [
            "Ok tell me the interest rate and terms. But I'm cautious — unsolicited loan offers are a known scam. What is your bank's RBI license number?",
            "How much loan am I eligible for? And where does the processing fee go? Give me the bank account details — I need to verify it's a real bank.",
            "I want to apply but need documents. What do you need — Aadhaar, PAN, salary slip? And what is the loan sanction reference number?",
            "Fine, I'll pay the processing fee. But I need receipt — what is your official email? And which bank branch will disburse the loan?",
            "My son is a banker, he will verify. What is your DSA code, the bank's IFSC code for the processing fee, and your NBF registration?",
            "Ok I'm interested. But send me the loan terms on official letterhead via email. What is your company email and the RBI registration number?",
        ],
        "late": [
            "I am arranging the processing fee. FD maturity in 3 days. Give me your callback number and exact bank account details for the payment.",
            "Money is ready. But my son says pay only after seeing official sanction letter. Send it to my email along with your ID and office address.",
            "Transfer initiated! But it's pending. Can you check? What is the transaction reference? Give me your number — I'll confirm when it clears.",
            "Sir I need time to think. My wife says be careful. Can you send all details on WhatsApp? What is your number? I'll decide by tomorrow.",
            "Almost done! Just one more question — what is your personal guarantee number, the CIBIL reference, and the NBFC RBI registration?",
            "My CA wants to review the terms before I pay. Send everything to my email — terms, conditions, your company PAN, and the disbursement timeline.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 11. ROMANCE / RELATIONSHIP SCAM
    # ══════════════════════════════════════════════════════════════════════
    "romance_scam": {
        "early": [
            "Who is this? I don't know you sir/madam! How did you get my number? This seems suspicious — what is your real name and where are you from?",
            "Hello dear? I am not 'dear' of anyone! Who are you? Why are you messaging me? My son monitors my phone — tell me your full identity!",
            "You want to be friends? But I am an old married person! What do you actually want? Give me your real name, city, and phone number.",
            "Gift for me from abroad? But I don't know anyone abroad! This is very suspicious — what is your real identity and contact number?",
            "Marriage proposal?! Sir/Madam I am already married with grandchildren! What is the real purpose of this call? Who gave you my number?",
            "Army officer stuck abroad? My nephew was in army — he says real officers never ask civilians for money! What is your battalion and rank?",
        ],
        "middle": [
            "Ok I understand you need help. But how can I trust you? Send me your identity proof — Aadhaar, passport, and a photo with today's newspaper.",
            "You need money for medical emergency? How much? But first — what is your family's contact number? I want to verify with them directly.",
            "I want to help but my son says these are romance scams. Give me your full real name, passport number, and a video call to prove identity.",
            "Ok I have sympathy for you. But sending money to strangers is risky. What is the hospital name and doctor's direct phone number?",
            "Customs fee to release your gift? But you should pay it, not me! What is the customs office number and the AWB tracking number?",
            "Fine, how much money? And where should I send? Give me the bank account, IFSC, and your local contact's phone number for verification.",
        ],
        "late": [
            "I am trying to help but need more time. My pension comes on 1st. Give me your phone number and email — I'll contact you then.",
            "Money is being arranged. But my son is suspicious. Can you video call us to prove you are real? What is your WhatsApp number?",
            "I sent the money but it bounced! Wrong account? Give me the correct bank details — full account number, IFSC, and beneficiary name.",
            "Almost done transferring! But before I complete — send me your passport copy, a selfie holding it, and your permanent home address.",
            "Sir/madam my family is asking questions. I need to show them proof. Send your identity documents, phone records, and hospital bills to my email.",
            "Transfer is processing. Will take 2 days international. What is your callback number, email, and local friend's contact to confirm receipt?",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 12. JOB / WORK FROM HOME SCAM
    # ══════════════════════════════════════════════════════════════════════
    "job_scam": {
        "early": [
            "Job offer? But I am retired! I didn't apply anywhere. How did you get my number? What is your company name and website? This is suspicious!",
            "Work from home earning 50,000? That sounds too good to be true — a classic scam red flag! What is your company registration and GSTIN?",
            "Part-time typing job? But these are usually pyramid schemes! My son warned me. What is your HR manager's number and office address?",
            "You found my resume online? But I never uploaded any resume! Who are you? What is your company name, address, and verification phone number?",
            "Registration fee for job? Legitimate companies never charge for hiring — this is a well-known scam! What is your company's official website?",
            "Data entry job paying Rs 1000 per day? It's clearly a scam sir! What is your company PAN, registration number, and office visit address?",
        ],
        "middle": [
            "Ok tell me more about the job. But first — what is your company's incorporation number, website, and glassdoor URL? I need to verify.",
            "Registration fee of 2000? Real companies don't charge — this is suspicious. But tell me the account details and I'll ask my son to verify.",
            "I am interested but cautious. What is the exact JD? Send it on email with official letterhead. What is your company email and HR's direct number?",
            "My grandson is in IT, he'll check your company. What is the full company name, CEO name, LinkedIn page, and main office phone number?",
            "Ok I'll register. But I need official offer letter first — send to my email. What is your HR email, the job ID, and your employee reference number?",
            "Sounds good. But where is training? What is the office address? Also unusual that you need payment for a job — give me your legal team's contact.",
        ],
        "late": [
            "I'm arranging the registration fee. My son will transfer it. Give me exct bank account details — number, IFSC, branch name, and payee name.",
            "Money is ready but my grandson wants to visit your office first. What is the full address, which floor, and what are the office hours?",
            "Transfer done but showing pending! What is your phone number? I'll send screenshot. Also send me the login credentials for the job portal.",
            "Almost registered! Need one more thing — your HR manager's personal phone, the company's PF registration number, and employee feedback link.",
            "I told my friend about this job too. He's interested. Can you share details with him? What is the referral process and your direct contact?",
            "Payment went through. Now I need the training materials, company ID card details, and reporting manager's contact. Send all to my email.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 13. INSURANCE / POLICY SCAM
    # ══════════════════════════════════════════════════════════════════════
    "insurance_scam": {
        "early": [
            "Insurance bonus? Which policy? I have LIC and health insurance. What is the policy number you have? What is your IRDA agent code?",
            "My policy has matured? But I have the maturity date noted — it's next year! This call is suspicious! What is your office and agent license number?",
            "Premium refund? Really? But I paid all premiums on time. What is the refund claim number? Give me your insurance company's toll-free number.",
            "Policy lapsed? But I have auto-debit! Let me check... what is the policy number, your agent code, and the IRDA complaint reference?",
            "Free insurance upgrade? But nothing is free! What is the catch? This sounds like a scam — what is your IRDA registration and company website?",
            "Sir I know insurance well — I was govt employee. Agents can't call for policy changes! What is your development officer's number?",
        ],
        "middle": [
            "Ok which policy? I have three. Give me the policy number, the sum assured, and the premium amount on record — I'll match and verify.",
            "Processing fee for bonus? But LIC deducts from the payout directly — they don't ask for advance fees! This is a red flag! What is your UPI ID?",
            "I want the refund. But send me the claim form on email — official format only. What is your company email and branch office address?",
            "Let me check with my LIC agent. What is your name and license number? My agent will verify your authenticity before I proceed.",
            "Fine, I'll pay processing charges. But first — what is the exact bonus amount, the payment bank account, IFSC, and your IRDA license number?",
            "My policy documents are in the locker. What is the claim reference number? Also send your ID and IRDA card copy to my email for verification.",
        ],
        "late": [
            "Sir I am visiting the LIC branch tomorrow to verify. What is your branch address? Also give me your phone — I'll call after verification.",
            "Processing fee arranged. My son is transferring now. Give me the bank account details and IFSC code, and send the receipt format to my email.",
            "Payment sent! But I need official receipt with stamp and signature. Send to my email. What is your branch address for physical verification?",
            "My LIC agent says wait — he's checking your details. Give me your license number, office landline, and branch manager's name.",
            "Almost done! But before final payment — I need your IRDA agent card number, the policy servicing office address, and a signed claim form.",
            "Transfer processing. Meanwhile send me — premium payment history, bonus calculation sheet, and your development officer's contact details.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 14. PAYMENT REQUEST / UPI FRAUD (GENERIC)
    # ══════════════════════════════════════════════════════════════════════
    "payment_request": {
        "early": [
            "Pay money? But why? What is this for? Asking for payment over phone is a big red flag! What is your name and why should I pay you?",
            "How much amount sir? And to whom? I need full details — your name, bank account, and reason — before I send even 1 rupee!",
            "My son says never pay anyone who calls asking for money — it's always a scam! What is your employee ID and official bank account?",
            "Transfer money? But I don't know you! This is very suspicious! What is the purpose? Give me your company name, registration, and website.",
            "UPI payment urgently? But UPI scams are very common — I saw on news! What is your UPI ID and what is this payment for exactly?",
            "Refundable deposit? But if it's refundable why collect it? This is a classic scam excuse! What is your office address and official phone?",
        ],
        "middle": [
            "Ok tell me the account details. But I will verify before sending — what is the account number, IFSC, and the account holder name?",
            "Fine, I have PhonePe open. What is your UPI ID? But demanding immediate payment is a major scam red flag! Can I pay at your office instead?",
            "Let me check if I have enough balance... how much exactly? And can you send me a written invoice on email? What is your email?",
            "I will pay but need receipt. What is your company GST number, PAN, and official email for sending invoice? Payment without receipt is suspicious.",
            "My wife does all UPI payments. I'll need to ask her. What is the exact amount, UPI ID, and purpose? She will want your phone number too.",
            "Before paying, give me full account details — bank name, account number, IFSC, branch, and the exact purpose and reference number of this payment.",
        ],
        "late": [
            "Sir payment initiated but OTP is not coming. Network problem. Give me your number — I'll call when it goes through. What is your UPI ID again?",
            "Almost sent! But my app is showing server error. Can I try tomorrow? Give me your callback number and email for confirmation.",
            "Money sent from my side! But it's pending. What is your phone number? I'll send you the transaction ID screenshot. Check from your end.",
            "My UPI daily limit is reached! Can I pay remaining amount tomorrow? Give me your bank account for NEFT — with full details and IFSC.",
            "Transfer done but to wrong account! Can you give me the correct details again? Account number, IFSC, exact beneficiary name?",
            "Sir I need my son's help for the transfer. He's coming home in 1 hour. Give me your contact — phone, email, and your office visiting time.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # 15. GENERAL / UNCLASSIFIED SCAM
    # ══════════════════════════════════════════════════════════════════════
    "general": {
        "early": [
            "Who is calling sir? I didn't understand properly. Can you explain again? What is your name, company, and why are you contacting me?",
            "I am not following. My hearing is a bit weak. Can you speak slowly? What organization are you from? What is your contact number?",
            "What is this about? I am a retired person, I don't have any pending matters. This call seems suspicious — who are you and what is your ID?",
            "Arrey, can you please explain clearly? I am confused. What is this regarding? Give me your full name and official phone number for callback.",
            "Ok ok, I am listening. But first tell me — who are you, which company, and what is this about? I am noting everything for my son.",
            "Sorry ji, who is this? My wife is asking. Tell me your full name, company name, official number, and the purpose of this call clearly.",
            "What should I do? I am worried now. But this random call is suspicious — what is your employee ID and office address for verification?",
            "Theek hai, tell me more. But I am going to record this conversation for safety. What is your name and callback number?",
        ],
        "middle": [
            "Ok I understand now. But I need to verify you are real. Give me your office address, supervisor's number, and send official email proof.",
            "Fine, I will cooperate. But first — what is your employee ID, which department, and your official email? I need to cross-check with my son.",
            "Let me write down everything. What is the reference number, your direct landline number, and your manager's full name?",
            "I want to help but this all sounds risky. My son will call you — what is your direct number, your WhatsApp, and your LinkedIn profile?",
            "Ok tell me the next steps. But I need everything in writing — send to my email. What is your official email and the case reference number?",
            "I am noting all details. Your name, ID, department, phone — everything. Now tell me what exactly you want me to do and why.",
            "Understood sir. But before I do anything, can you give me your office visiting hours and address? I'd rather come in person to resolve this.",
            "Ok ji, I trust you. But my wife doesn't. Can your supervisor call us? What is their name and number? Also your company's toll-free number?",
        ],
        "late": [
            "I am working on it sir. But it will take time. Give me your callback number — I will call you in 30 minutes without fail.",
            "Almost done! But my phone battery is about to die. Send me your email, WhatsApp number, and office address — I'll reach out from landline.",
            "Sir please give me until tomorrow. I need to consult my son and lawyer. What is your phone, email, and office address for tomorrow's visit?",
            "I am arranging everything. But the bank is closed now. Give me your direct number, your manager's cell, and I'll sort it by morning.",
            "Wait, my neighbour uncle is here — he was a bank manager. He wants to speak to you. Give me your phone number and your branch details.",
            "Sir I am old person, everything takes time. Please be patient. Give me your full contact — phone, email, WhatsApp — I will respond properly.",
        ],
    },
}

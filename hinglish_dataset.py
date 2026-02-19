"""
Hinglish Response Dataset — Hindi-English mix responses for authenticity.
Adds ~200 Hinglish responses across all 15 categories × 3 phases.
Merged with English dataset in agent_persona.py for maximum variety.
"""

HINGLISH_DB = {

    "kyc_fraud": {
        "early": [
            "KYC update karna hai? Par meine toh last year hi karwaya tha! Aapka employee ID kya hai? Yeh bahut suspicious lag raha hai.",
            "Arrey bhai, KYC ke liye bank kabhi phone nahi karta — yeh toh scam hai! Aapka branch address kya hai? Main khud aa jaaunga.",
            "Kya? KYC expire ho gaya? Mujhe toh koi SMS nahi aaya! Aapka naam kya hai aur kis branch se bol rahe ho? Bahut shaky lag raha hai.",
            "Haan ji, KYC karunga. Par pehle aapka supervisor ka number do — phone pe KYC maangna toh red flag hai bilkul!",
            "Mere bête ne bola hai ki phone pe KYC kabhi nahi karte. Aapka office address do, main kal aa jaaunga documents leke.",
        ],
        "middle": [
            "Aadhaar card mere paas hai. Par phone pe share karna risky hai — yeh toh sabko pata hai! Aapka UPI ID kya hai verification fee ke liye?",
            "Theek hai ji, main cooperate karunga. Par pehle apna employee badge number, branch IFSC code, aur manager ka number dijiye.",
            "Mera PAN card dhoondh raha hoon almirah mein. Tab tak aapka official email bataiye — main documents wahi bhej dunga.",
            "Ji haan, KYC zaroori hai samajh gaya. Par aapka company ka registered address kya hai? Main verify karna chahta hoon pehle.",
            "Ok fine, main kar dunga. Par mera beta IT mein kaam karta hai — woh verify karega pehle. Aapka LinkedIn profile kya hai?",
        ],
        "late": [
            "Documents dhoondh raha hoon ji, wife ne kahin rakh diye. Aapka WhatsApp number do — photo bhej dunga jaise hi milega.",
            "Bas 10 minute aur dijiye sir. Almirah ki chaabi nahi mil rahi. Aapka callback number kya hai? Main call karunga pakka.",
            "Beta abhi ghar aa raha hai, woh help karega. Aapka direct number do — 20 minute mein call karta hoon confirm.",
            "Sir mera phone hang ho gaya! Restart ho raha hai. Aapka email do, main laptop se bhej dunga documents.",
        ],
    },

    "account_threat": {
        "early": [
            "KYA?! Mera account block ho jayega?! Hai Ram! Par meine kuch galat nahi kiya! Complaint number kya hai aapka?",
            "Sir please block mat karo! Meri beti ki shaadi ka paisa hai usme! Aap kaun ho? Employee ID batao pehle!",
            "Account suspend? Par maine sab dues clear kiye hain! Yeh toh fraud call lagta hai — aapka branch address kya hai?",
            "Arrey baap re! Mera pension ka paisa hai us account mein! Par phone pe threatening karna toh scam hai — aapka supervisor ka number do!",
            "Blocked?! Par maine aaj subah hi check kiya tha — sab theek tha! Aapka official email kya hai? Written notice bhejo.",
        ],
        "middle": [
            "Theek hai samajh gaya, koi issue hai account mein. Par real bank SMS bhejta hai, call nahi — yeh suspicious hai! Fine kitna hai? UPI ID do.",
            "Main pay kar dunga sir. Par pehle reference number, aapka badge number, aur branch ka landline number dijiye verification ke liye.",
            "Mera beta banker hai — woh verify karega. Aapka branch IFSC code, account number jisme pay karna hai, aur manager ka naam batao.",
            "Ok ji, trust karta hoon aapko. Par threatening call karna classic scam hai. Written notice email pe bhejo — aapka email kya hai?",
        ],
        "late": [
            "Paisa arrange kar raha hoon sir. Beta ATM gaya hai. Aapka number do — payment hote hi call karunga. Kitna time hai deadline?",
            "Transfer ho gaya mere side se par pending dikha raha hai. Screenshot bhejta hoon — aapka WhatsApp number kya hai?",
            "Sir UPI error aa raha hai! Wife ke phone se try karta hoon. 10 minute dijiye aur aapka callback number bataiye.",
            "Almost done sir! Bas OTP aane mein time lag raha hai — network problem hai area mein. Aapka direct number do.",
        ],
    },

    "otp_fraud": {
        "early": [
            "OTP?! Mera bank hamesha bolta hai OTP kabhi share mat karo! Yeh toh sabse bada red flag hai! Aap kaun ho? ID batao!",
            "Sir, OTP maangna matlab fraud hai — RBI ne bhi warning di hai! Aapka naam, employee ID, aur branch address batao pehle!",
            "OTP share karna? Mera beta bolta hai yeh sabse dangerous cheez hai! Aapka supervisor se baat karwao — unka number do!",
            "Arrey sahib! OTP toh bank wale bhi nahi maangte! Yeh pakka scam call hai! Aapka office address do — main police ko bata dunga!",
            "Ruko ruko, samajh nahi aa raha. OTP kyun chahiye aapko? Bank apna kaam OTP se khud karta hai. Aapka callback number do.",
        ],
        "middle": [
            "OTP aa gaya hai par... mera beta bol raha hai bilkul mat dena! Aapka manager se baat karni hai — unka direct number kya hai?",
            "Haan OTP padh raha hoon... 4... ek minute, glasses chahiye. Tab tak aapka full name, employee ID, aur office address note kar leta hoon.",
            "OTP mil gaya par do aaye hain — kaunsa wala chahiye? Par pehle aapka email do — written authorization chahiye mujhe OTP share karne ke liye.",
            "Theek hai ji, OTP dunga. Par yeh confirmed fraud technique hai — TV pe dekha hai. Aapka Aadhaar number do pehle trust ke liye.",
        ],
        "late": [
            "Sir OTP expire ho gaya! Naya bhejo. Par usse pehle — aapka callback number do, mera beta bhi line pe rahega jab share karunga.",
            "Naya OTP aaya par phone doosre kamre mein charge ho raha hai. 5 minute ruko — aapka number do, wapas call karta hoon OTP ke saath.",
            "OTP pad nahi pa raha, font bahut chhota hai. Aapka email do — screenshot bhej deta hoon. Zyada safe bhi rahega.",
            "Galat OTP pad diya — grocery delivery ka tha! Sahi wala dhundh raha hoon. Aapka direct number do sir.",
        ],
    },

    "lottery_scam": {
        "early": [
            "MEINE JEETA?! Sach mein?! Par maine toh koi ticket nahi kharida! Yeh toh suspicious hai — aapka company ka registration number kya hai?",
            "50 Lakh?! Hai Ram! Par bina ticket ke lottery kaise — yeh toh pakka fraud lag raha hai! Aapka office address aur website batao!",
            "Prize? Mere liye? Par kaise? Mera beta bolta hai lottery calls sab scam hote hain! Aapka company ka GST number do pehle!",
            "Arrey wah! Par guaranteed prize without ticket buying is classic scam — TV pe dekha tha! Aapka SEBI registration kya hai?",
        ],
        "middle": [
            "Ok interested hoon. Par verify karna padega — aapka company ka incorporation certificate number, GST, aur registered address dijiye.",
            "Tax pay karna padega prize ke liye? Par real lotteries khud tax deduct karti hain — advance mein maangna scam hai! UPI ID kya hai?",
            "Mera beta online check kar raha hai aapki company. Tab tak batao — payment kahan karna hai? Account number, IFSC, aur branch name do.",
            "Bahut exciting hai sir! Par proper documentation chahiye — company PAN, SEBI registration, aur official letterhead pe email bhejo.",
        ],
        "late": [
            "Tax amount arrange kar raha hoon. Mera FD next week mature ho raha hai. Aapka callback number do — tab call karunga. Deadline kya hai?",
            "Paisa ready hai par wife official letter dekhna chahti hai pehle. Email pe bhejo — aapka email kya hai? Winner certificate bhi bhejo.",
            "Transfer initiate kiya hai, 24 hours lagenge. Aapka WhatsApp do — confirmation receipt bhej dunga jaise hi ho jayega.",
        ],
    },

    "investment_scam": {
        "early": [
            "200% returns guaranteed?! Mera beta bolta hai guaranteed returns sabse bada investment scam red flag hai! Aapka SEBI registration number kya hai?",
            "Bitcoin mein invest? Bhai mujhe toh bitcoin kya hai woh bhi nahi pata! Aapka company ka website aur registration number batao.",
            "Triple returns 30 din mein? Yeh toh Ponzi scheme jaisa lag raha hai sir! Aapka company name, PAN, aur SEBI license number dijiye!",
            "Invest karne ko bol rahe ho? Par meri pension sirf 35000 hai. Aapka office address kya hai? Main verify karke aaunga pehle.",
        ],
        "middle": [
            "Theek hai, interest aa raha hai. Minimum kitna invest karna padega? Aur paise kahan jayenge exactly? Account number batao.",
            "Mera beta verify karna chahta hai pehle. Aapka direct mobile number, LinkedIn profile, aur company ka SEBI authorization number dijiye.",
            "Ok invest karunga monthly. Par full company details chahiye — registered address, directors ke naam, aur RBI/SEBI authorization.",
            "Bahut accha plan hai sir! Par documentation chahiye — aapka company PAN, registration papers, aur written agreement email pe bhejo.",
        ],
        "late": [
            "FD se paisa nikal raha hoon invest karne ke liye. 3 din lagenge. Aapka callback number aur full account details do transfer ke liye.",
            "Wife bhi invest karna chahti hai! Maximum limit kya hai? Sab payment details do — UPI, account, IFSC — dono ka invest karunga.",
            "Beta online transfer kar raha hai mere liye. Usse chahiye — full bank name, account number, IFSC, aur investment reference ID.",
        ],
    },

    "phishing": {
        "early": [
            "Kaun sa link sir? Mera beta bolta hai unknown links pe click karna bahut dangerous hai — phishing hota hai! Aapka official website kya hai?",
            "Link open nahi ho raha — mera phone purana hai. WhatsApp pe bhej do? Par unknown links toh red flag hai! Aapka number kya hai?",
            "Yeh link toh mere bank ki website jaisa nahi dikh raha — naam alag hai! Yeh definitely suspicious hai! Aap kaun ho sacchi mein?",
            "Mera beta ne antivirus lagaya hai — woh block kar raha hai aapka link as suspicious! Aapka employee ID aur branch landline do.",
        ],
        "middle": [
            "Link khula par card number maang raha hai. Real bank websites link se card details nahi maangti — yeh fraud hai! Aapka UPI ID kya hai?",
            "Mera beta ne check kiya — yeh official bank domain nahi hai. Phishing hai pakka! Par main help karna chahta hoon — aapka office phone number do.",
            "Website Aadhaar aur card PIN maang rahi hai — yeh toh definitely suspicious hai! Real banks aisa nahi karte! Aapka branch address do.",
            "Link pe details daalne se pehle — aapka employee ID, branch code, aur supervisor ka direct landline number chahiye verification ke liye.",
        ],
        "late": [
            "Sir browser crash ho gaya link kholte waqt! Restart karna padega. Aapka callback number do — 10 minute mein try karunga phir se.",
            "Internet bahut slow hai yahan. Email pe alternative link bhejo — aapka email kya hai? Main wahan se reply karunga.",
            "Beta ka laptop lena padega — mere phone pe nahi khul raha. 20 minute mein aa jayega woh. Aapka WhatsApp do tab tak.",
        ],
    },

    "delivery_scam": {
        "early": [
            "Mera package? Par maine toh kuch order nahi kiya! Kisne bheja? Tracking number kya hai? Yeh scam call lag raha hai!",
            "Customs duty? Par maine toh kuch import nahi kiya! AWB number aur customs reference batao — yeh fraud jaisa sound kar raha hai.",
            "Kaun si courier company? Mujhe koi notification nahi aaya! Aapka employee ID aur company ka toll-free number do verify karne ke liye.",
        ],
        "middle": [
            "Tracking number batao, main check karta hoon. Aur company ka official email, phone, office address — sab chahiye verify karne ke liye.",
            "Duty kitni hai? Kahan pay karna hai? Par legitimate couriers delivery pe charge lete hain, phone pe nahi — yeh red flag hai!",
            "Main package lene aaunga. Kaun sa warehouse? Address kya hai? Employee badge number aur company ka GST number bhi do.",
        ],
        "late": [
            "Payment process ho raha hai par time lag raha hai. Aapka WhatsApp do — screenshot bhej dunga. Package ki photo bhi bhejo.",
            "Nearby courier office ja raha hoon check karne. Kaun si branch? Aapka direct number do — wahan se call karunga.",
        ],
    },

    "tax_scam": {
        "early": [
            "Income tax notice? Par main toh har saal return file karta hoon! Assessment number kya hai? Aapka officer ID batao!",
            "Tax baki hai 50,000? Par mera CA sab handle karta hai! Phone pe tax maangna suspicious hai — IT dept letter bhejta hai! Aapka email do.",
            "Arrest karenge tax ke liye?! Par main toh honest citizen hoon! Real tax officers written notice dete hain — aap kaun ho?",
            "Main 30 saal government mein tha — mujhe procedure pata hai. IT dept phone pe payment nahi maangta! Aapka superior ka number do!",
        ],
        "middle": [
            "Theek hai, tax issue samajh gaya. Par official notice email pe bhejo — .gov.in se. Aur kuch bhi toh suspicious hai! Aapka govt email ID kya hai?",
            "Challan number batao, payment gateway batao, aur officer code do. Main apne CA se bhi baat karunga — uska number hai mere paas.",
            "NEFT se pay karunga. IT department ka official account number aur IFSC do — personal account mein toh bilkul nahi dunga, woh scam hoga!",
        ],
        "late": [
            "CA se baat kar raha hoon. Woh aapko directly call karega. Aapka number, officer ID, aur kaun sa IT office — address dijiye.",
            "Payment ready hai par IT office mein jaake dunga. Ward office ka address aur timing kya hai? Kal subah aa jaaunga.",
            "Bank DD bana raha hai — 2 ghante lagenge. Aapka callback number aur payee name batao demand draft ke liye.",
        ],
    },

    "tech_support": {
        "early": [
            "Mere computer mein virus? Par main toh sirf email ke liye use karta hoon! Aap kaise jaante ho? Company name kya hai? Suspicious call hai yeh!",
            "Microsoft call kar raha hai? Par Microsoft toh kabhi call nahi karta — mera pota bola tha yeh common scam hai! Aapka employee ID do!",
            "Computer hack ho gaya?! Arrey baap re! Par aapko kaise pata? Yeh bahut suspicious hai — aapka company website aur manager ka phone do!",
        ],
        "middle": [
            "Kya karna hai batao par remote software toh bilkul install nahi karunga — yeh confirmed scam technique hai! Aapka official email kya hai?",
            "5000 virus removal ke liye?! Bahut mehenga hai! Mera bhatija free mein kar deta hai. Aapka company ka GST number do pehle.",
            "Mera bhatija IT engineer hai — woh verify karega. Aapka number do, woh call karke check karega ki real tech support ho ya nahi.",
        ],
        "late": [
            "Computer start hone mein bahut time le raha hai — purana machine hai. 20 minute dijiye aur aapka phone number do — ready hote hi call karta hoon.",
            "Pota aa raha hai help karne. 30 minute mein aayega. Aapka number do — woh IT professional hai, directly baat karega.",
        ],
    },

    "loan_scam": {
        "early": [
            "Pre-approved loan? Par maine apply hi nahi kiya! Mere details kahan se aaye aapke paas? Yeh red flag hai — aapka bank name aur employee ID batao!",
            "Zero interest loan?! Koi bank zero interest nahi deta — yeh toh pakka fraud hai! Aapka company registration number kya hai?",
            "Processing fee upfront? Mera dost bola tha loan scams hamesha advance fee maangte hain — yeh major red flag hai! Aapka company ka GST do!",
        ],
        "middle": [
            "Interest rate aur terms batao. Par unsolicited loan offers scam hote hain — aapka bank ka RBI license number kya hai?",
            "Kitna loan eligible hoon? Processing fee kahan jaayega? Bank account details do — main verify karunga ki real bank hai ya nahi.",
            "Mera beta banker hai — woh verify karega. Aapka DSA code, bank ka IFSC code, aur NBFC registration number dijiye.",
        ],
        "late": [
            "Processing fee arrange kar raha hoon. FD maturity 3 din mein hai. Aapka callback number aur exact bank account details do payment ke liye.",
            "Transfer initiated! Par pending hai. Check karo aapki side se — transaction reference kya hai? Aapka number do confirm karne ke liye.",
        ],
    },

    "romance_scam": {
        "early": [
            "Aap kaun ho? Main aapko jaanta bhi nahi! Mera number kahan se mila? Yeh suspicious hai — apna asli naam aur sheher batao!",
            "Hello dear? Main kisi ka dear nahi hoon! Mera beta mera phone check karta hai — apni puri identity batao abhi!",
            "Army officer abroad? Mere bhateeje army mein the — real officers civilians se paisa nahi maangte! Aapka battalion aur rank kya hai?",
        ],
        "middle": [
            "Help chahiye toh identity proof do — Aadhaar, passport, aur aaj ki newspaper ke saath photo. Trust toh banta hai na!",
            "Medical emergency ke liye paisa? Kitna? Par pehle — hospital ka naam aur doctor ka direct phone number do. Main verify karunga.",
            "Customs fee? Par aapko pay karna chahiye, main kyun karoon?! Customs office ka number aur AWB tracking number kya hai?",
        ],
        "late": [
            "Paisa arrange kar raha hoon par pension 1 tarikh ko aati hai. Aapka phone number aur email do — tab contact karunga.",
            "Transfer kiya par bounce ho gaya! Account galat hai kya? Sahi details do — full account number, IFSC, aur beneficiary name.",
        ],
    },

    "job_scam": {
        "early": [
            "Job offer? Par main retired hoon! Maine kahin apply nahi kiya! Yeh suspicious hai — aapka company name aur website kya hai?",
            "Work from home 50,000 kamao? Too good to be true! Mera beta bolta hai yeh sab pyramid scheme hai! Company registration aur GST do!",
            "Registration fee? Real companies hiring ke liye charge nahi karte — yeh well-known scam hai! Aapka company ka official website kya hai?",
        ],
        "middle": [
            "Company ke baare mein batao. Incorporation number, website, aur Glassdoor URL chahiye — verify karunga pehle.",
            "2000 registration fee? Legitimate companies charge nahi karte — suspicious hai. Par account details batao, beta verify karega.",
            "Pota IT mein hai, woh check karega company. Full company name, CEO ka naam, LinkedIn page, aur main office phone number do.",
        ],
        "late": [
            "Registration fee arrange kar raha hoon. Beta transfer karega — exact bank account details do — number, IFSC, branch, payee name.",
            "Pota office visit karna chahta hai pehle. Full address kya hai? Kaun si floor? Office hours kya hain? Tab pay karunga.",
        ],
    },

    "insurance_scam": {
        "early": [
            "Insurance bonus? Kaun si policy? Mera LIC aur health insurance hai. Policy number batao jo aapke paas hai? IRDA agent code kya hai?",
            "Policy mature ho gayi? Par meine maturity date note kiya hai — next year hai! Yeh suspicious call hai! Aapka agent license number do!",
            "Premium refund? Sach mein? Par maine toh sab premiums time pe pay kiye hain! Claim number kya hai? Company ka toll-free number do!",
        ],
        "middle": [
            "Kaun si policy? Meri teen hain. Policy number, sum assured, aur premium amount batao — main match karke verify karunga.",
            "Processing fee bonus ke liye? Par LIC toh payout se deduct karta hai — advance fee maangna scam hai! Aapka UPI ID kya hai?",
            "Apne LIC agent se check karunga pehle. Aapka naam aur license number batao — mera agent verify karega authenticity.",
        ],
        "late": [
            "LIC branch ja raha hoon kal verify karne. Aapka branch address kya hai? Phone number do — verification ke baad call karunga.",
            "Processing fee arrange kiya hai. Beta transfer kar raha hai — bank account details aur IFSC dijiye, aur email pe receipt format bhejo.",
        ],
    },

    "payment_request": {
        "early": [
            "Paisa kyun bhejoon? Kiske liye hai? Phone pe paisa maangna toh red flag hai! Aapka naam aur payment ka reason batao pehle!",
            "UPI se urgently pay karo? Par UPI scams toh bahut common hain — news pe dekha hai! Aapka UPI ID kya hai aur payment kis liye hai exactly?",
            "Refundable deposit? Par agar refundable hai toh collect kyun karna? Classic scam excuse hai yeh! Aapka office address aur official phone do!",
            "Kitna amount hai sir? Aur kisko? Full details chahiye — naam, bank account, aur reason — 1 rupaye bhi nahi bhejunga bina details ke!",
        ],
        "middle": [
            "Account details batao. Par verify karunga pehle — account number, IFSC, aur account holder name kya hai?",
            "PhonePe khol liya hai. UPI ID kya hai? Par immediate payment demand karna major scam red flag hai! Office mein jaake de sakta hoon?",
            "Wife sab UPI payments karti hai. Exact amount, UPI ID, aur purpose batao — woh aapka phone number bhi maangegi.",
            "Pay karunga par receipt chahiye. Company ka GST number, PAN, aur official email do invoice bhejne ke liye. Bina receipt suspicious hai.",
        ],
        "late": [
            "Payment initiate kiya par OTP nahi aa raha. Network problem hai. Aapka number do — clear hote hi call karunga. UPI ID phir se batao.",
            "Bhej diya mere side se! Par pending dikha raha hai. Aapka phone number do — transaction ID ka screenshot bhejta hoon. Check karo apni side se.",
            "Daily UPI limit reach ho gayi! Kal remaining amount bhejunga. NEFT ke liye bank account details do — full details aur IFSC ke saath.",
        ],
    },

    "general": {
        "early": [
            "Kaun bol raha hai sir? Samajh nahi aaya. Phir se explain kariye? Aapka naam, company, aur kyun call kiya — sab batao!",
            "Kya baat hai ji? Main retired hoon, koi pending matter nahi hai mera. Yeh suspicious call lag raha hai — aap kaun ho aur ID kya hai?",
            "Arrey, thoda clearly batao na! Confused ho gaya main. Kya hai yeh? Apna full naam aur official phone number do callback ke liye.",
            "Sorry ji, kaun hai? Wife pooch rahi hai. Apna full naam, company name, official number, aur call ka purpose clearly batao.",
            "Main sun raha hoon par samajh nahi aa raha. Meri hearing thodi weak hai. Slowly batao — aap kahan se bol rahe ho? Contact number kya hai?",
            "Theek hai batao kya karna hai. Par pehle — aap kaun, kaunsi company, aur yeh kis baare mein hai? Main sab note kar raha hoon bête ke liye.",
        ],
        "middle": [
            "Ok samajh gaya ab. Par verify karna padega ki aap real ho. Office address, supervisor ka number, aur official email proof bhejo.",
            "Theek hai, cooperate karunga. Par pehle — employee ID, department, aur official email? Beta se cross-check karunga.",
            "Sab likh raha hoon. Reference number, direct landline, aur manager ka full naam kya hai?",
            "Help karna chahta hoon par risky lag raha hai. Beta aapko call karega — direct number, WhatsApp, aur LinkedIn profile do.",
            "Next steps batao. Par sab writing mein chahiye — email pe bhejo. Official email aur case reference number kya hai?",
            "Ji trust karta hoon. Par wife nahi karti. Aapka supervisor call kar sakta hai kya? Unka naam aur number do. Company ka toll-free number bhi.",
        ],
        "late": [
            "Kaam kar raha hoon sir uspe. Par time lagega. Callback number do — 30 minute mein call karta hoon pakka.",
            "Almost done! Par phone ki battery khatam hone wali hai. Email, WhatsApp number, aur office address do — landline se contact karunga.",
            "Sir please kal tak ka time do. Beta aur lawyer se consult karna hai. Aapka phone, email, aur office address do kal ke visit ke liye.",
            "Sab arrange kar raha hoon. Par bank band hai abhi. Direct number do, manager ka cell do — subah sort kar dunga.",
            "Padosi uncle aaye hain — woh bank manager the. Woh baat karna chahte hain aapse. Aapka phone number aur branch details do.",
        ],
    },
}

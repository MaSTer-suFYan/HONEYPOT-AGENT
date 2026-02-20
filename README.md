# 🍯 Agentic Honeypot API

AI-powered honeypot that detects scam messages, engages scammers in realistic
multi-turn conversations, extracts intelligence, and reports findings — all
without relying on an LLM at runtime (sub-10 ms responses).

---

## 📁 Project Structure

```
├── README.md                  # You are here
├── src/                       # Source code
│   ├── main.py                # FastAPI app & endpoints
│   ├── config.py              # Environment variables
│   ├── models.py              # Pydantic request/response schemas
│   ├── scam_detector.py       # Keyword & pattern-based scam scoring
│   ├── intelligence.py        # Regex extraction (phones, UPI, banks …)
│   ├── agent_persona.py       # Hinglish persona & reply generation
│   ├── session_manager.py     # Per-session state & turn tracking
│   ├── engagement_metrics.py  # Duration & message-count calculations
│   ├── guvi_callback.py       # Async reporting to GUVI endpoint
│   ├── hinglish_dataset.py    # Hinglish response templates
│   ├── response_dataset.py    # Replies categorised by scam type
│   └── scammer_dna.py         # Scammer profiling & behaviour analysis
├── docs/
│   └── architecture.md        # Detailed architecture documentation
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variable template
├── Procfile                   # Railway / Heroku process definition
└── railway.json               # Railway deployment config
```

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/your-username/honeypot-agent.git
cd honeypot-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and fill in:

| Variable             | Description                          |
|----------------------|--------------------------------------|
| `OPENROUTER_API_KEY` | OpenRouter API key (optional)        |
| `MY_API_KEY`         | Secret key to protect your endpoint  |

### 5. Run locally

```bash
uvicorn main:app --reload --app-dir src
```

The API will be available at **http://127.0.0.1:8000**.

---

## 📡 API Endpoints

### `GET /`

Health check — confirms the API is running.

### `GET /health`

Returns `{ "status": "healthy", "timestamp": <epoch_ms> }`.

### `POST /analyze`

Main endpoint. Detects scams, extracts intelligence, and returns an engagement
reply.

**Headers**

| Header      | Required | Description       |
|-------------|----------|-------------------|
| `x-api-key` | Yes      | Your `MY_API_KEY` |

**Request Body**

```json
{
  "sessionId": "abc-123",
  "message": {
    "text": "Congratulations! You won a prize. Send ₹500 to UPI: scammer@upi"
  },
  "conversationHistory": []
}
```

**Response** (abbreviated)

```json
{
  "sessionId": "abc-123",
  "status": "success",
  "scamDetected": true,
  "scamType": "UPI_FRAUD",
  "confidenceLevel": 0.85,
  "totalMessagesExchanged": 2,
  "engagementDurationSeconds": 12,
  "extractedIntelligence": {
    "upiIds": ["scammer@upi"],
    "phoneNumbers": [],
    "bankAccounts": [],
    "phishingLinks": [],
    "emailAddresses": []
  },
  "reply": "Arey wah! Prize mila? Mujhe bhi batao, kaise claim karu?"
}
```

---

## 🛠️ Deployment (Railway)

1. Push the repo to GitHub.
2. Connect the repo to [Railway](https://railway.app).
3. Set **environment variables** (`MY_API_KEY`, `OPENROUTER_API_KEY`) in the
   Railway dashboard.
4. Railway auto-detects the `Procfile` and deploys.

---

## 🧪 Running Tests

```bash
python benchmark.py          # Performance benchmark
python test_scoring.py       # Scoring validation
python test_compliance.py    # Rubric compliance checks
python verify_final.py       # End-to-end verification
```

---

## 🏗️ Architecture

See [`docs/architecture.md`](docs/architecture.md) for a detailed breakdown of
modules, data flow, and the request lifecycle.

---

## 📜 License

This project was built for the **GUVI Sentinal Hackathon 2026**.

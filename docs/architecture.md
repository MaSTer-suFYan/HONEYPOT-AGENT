# Agentic Honeypot — Architecture

## Overview

The Agentic Honeypot is an AI-powered API that detects scam messages, engages
scammers in multi-turn conversations, extracts intelligence (phone numbers, bank
accounts, UPI IDs, phishing links, etc.), and reports findings to the GUVI
evaluation endpoint.

## High-Level Flow

```
Incoming Request
      │
      ▼
  ┌──────────┐     ┌────────────────┐
  │  main.py  │────▶│  scam_detector  │  Keyword + pattern scoring
  │  (FastAPI)│     └────────────────┘
  │           │
  │           │     ┌────────────────┐
  │           │────▶│  intelligence   │  Regex extraction (phones, UPI, etc.)
  │           │     └────────────────┘
  │           │
  │           │     ┌────────────────┐
  │           │────▶│  agent_persona  │  Hinglish response generation
  │           │     └────────────────┘
  │           │
  │           │     ┌──────────────────┐
  │           │────▶│  session_manager  │  Per-session state & metrics
  │           │     └──────────────────┘
  │           │
  │           │     ┌────────────────┐
  │           │────▶│  guvi_callback  │  Async result reporting
  └──────────┘     └────────────────┘
```

## Module Responsibilities

| Module                | Purpose                                            |
|-----------------------|----------------------------------------------------|
| `main.py`             | FastAPI app, request parsing, response building     |
| `config.py`           | Environment variables and constants                 |
| `models.py`           | Pydantic request/response schemas                   |
| `scam_detector.py`    | Scam scoring via keyword & pattern matching         |
| `intelligence.py`     | Regex-based extraction of phones, UPI, bank, etc.   |
| `agent_persona.py`    | Honeypot persona & Hinglish reply generation        |
| `session_manager.py`  | Multi-turn session state and engagement metrics     |
| `engagement_metrics.py` | Duration and message-count calculations           |
| `guvi_callback.py`    | Async POST to GUVI evaluation endpoint              |
| `hinglish_dataset.py` | Hinglish response templates                         |
| `response_dataset.py` | Categorized reply datasets by scam type             |
| `scammer_dna.py`      | Scammer profiling and behaviour analysis            |

## Request Lifecycle

1. **Auth** — `x-api-key` header validated against `MY_API_KEY`.
2. **Parse** — Raw JSON body parsed; `sessionId`, `message`, and
   `conversationHistory` extracted with multiple field-name fallbacks.
3. **Session** — Session retrieved or created via `session_manager`.
4. **Scam Detection** — `scam_detector.detect_scam()` scores the message +
   history; returns `scam_detected`, keywords, and a numeric score.
5. **Intelligence Extraction** — `intelligence.extract_all_intelligence()` runs
   regex patterns over the current message *and* every history item.
6. **Response Generation** — `agent_persona.generate_honeypot_response()` picks
   a contextual Hinglish reply designed to keep the scammer engaged.
7. **Callback** — If scam is confirmed and intelligence exists,
   `guvi_callback.send_callback_async()` fires a non-blocking POST to GUVI.
8. **Return** — Rubric-compliant JSON response with session metrics.

## Deployment

- **Platform**: Railway (Nixpacks builder)
- **Entry point**: `uvicorn main:app --host 0.0.0.0 --port $PORT --app-dir src`
- **Environment**: Variables loaded from `.env` via `python-dotenv`

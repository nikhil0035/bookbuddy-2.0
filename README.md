# bookbuddy-2.0

Here is a **production-ready `README.md`** for BookBuddy 2.0 that you can directly give to a coding agent.

I have structured it to be:

* Clear architecture-first
* Implementation-sequenced
* Strict about spoiler-protection rules
* Ready for agent execution
* Aligned with your uploaded technical documentation 

---

# 📚 BookBuddy 2.0

**AI-Powered Reading Companion**

---

## 🚀 Overview

BookBuddy 2.0 is an AI-powered reading assistant designed to enhance reading without spoiling future content.

It allows users to:

* Upload PDFs
* Read with progress tracking
* Tap words for contextual meanings
* Get page-based summaries
* Ask questions about what they've read
* Track reading streaks and vocabulary
* Receive AI help strictly bounded to current reading progress

⚠️ **Core Rule: AI must NEVER reveal content beyond the user’s current page.**

---

# 🏗️ System Architecture

```
Mobile App (React Native)
        ↓
     FastAPI Backend
        ↓
PostgreSQL | Redis | S3 | Groq API
```

---

# 🧱 Tech Stack

## Frontend

* React Native (0.73+)
* React Navigation
* Zustand (state)
* React Query
* Axios
* react-native-pdf
* AsyncStorage

## Backend

* Python 3.11
* FastAPI
* SQLAlchemy 2.0
* Alembic
* PostgreSQL
* Redis
* Celery
* PyPDF2
* LangChain
* httpx
* python-jose (JWT)
* passlib (bcrypt)

## Infra

* AWS ECS (Fargate)
* RDS PostgreSQL
* ElastiCache Redis
* S3 (book storage)
* CloudFront
* ALB

---

# 📁 Repository Structure

## Backend

```
backend/
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── rate_limit.py
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models/
│   ├── schemas/
│   ├── api/
│   │   ├── deps.py
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── books.py
│   │   │   ├── progress.py
│   │   │   ├── highlights.py
│   │   │   └── ai.py
│   ├── services/
│   │   ├── pdf_service.py
│   │   ├── ai_service.py
│   │   ├── spoiler_guard.py
│   │   └── cache_service.py
│   └── tasks/
│       └── celery_worker.py
├── alembic/
├── requirements.txt
└── Dockerfile
```

## Frontend

```
mobile/
├── src/
│   ├── screens/
│   ├── components/
│   ├── navigation/
│   ├── store/
│   ├── hooks/
│   ├── services/
│   └── utils/
```

---

# 🧠 Core Feature: Spoiler Protection System

This is the MOST IMPORTANT system.

## RULES

1. AI only receives content up to `reading_progress.current_page`
2. Pages beyond current page must NEVER be loaded
3. Cache keys must include page boundary
4. Responses must be validated
5. Log every AI request

---

## Spoiler Guard Flow

```
User Request
     ↓
Fetch reading_progress.current_page
     ↓
Extract pages 1 → current_page
     ↓
Construct bounded prompt
     ↓
Send to LLM
     ↓
Validate response
     ↓
Return to user
```

---

## Example Prompt Template (MANDATORY FORMAT)

System Prompt:

```
You are an AI reading assistant.
You are STRICTLY forbidden from referencing content beyond page {current_page}.
If unsure, say: "That content appears later in the book."
Never speculate.
```

User Prompt:

```
Book Title: {title}
Current Page: {current_page}
Book Content (1 to current_page):
{bounded_text}

User Question:
{question}
```

---

# 🗄️ Database Core Tables

Minimum Required Tables:

* users
* books
* chapters
* reading_progress
* highlights
* notes
* vocabulary_log
* ai_interactions
* reading_streaks

Use UUID primary keys.

Ensure:

* ON DELETE CASCADE
* Index user_id everywhere
* Store file hash for deduplication

---

# 🔐 Authentication

* JWT access token (1 hour)
* Refresh token (30 days)
* Bcrypt (12 rounds)
* Protect all routes except auth
* Premium flag support

---

# 📡 API Endpoints

## Auth

```
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/refresh
```

## Books

```
POST   /api/v1/books/upload
GET    /api/v1/books
GET    /api/v1/books/{id}
DELETE /api/v1/books/{id}
```

## Progress

```
POST /api/v1/progress/update
GET  /api/v1/progress/{book_id}
```

## AI

```
POST /api/v1/ai/word-meaning
POST /api/v1/ai/summarize-page
POST /api/v1/ai/summarize-till-here
POST /api/v1/ai/ask-question
POST /api/v1/ai/explain-concept
```

Rate Limits:

* Free: 50 AI/day
* Premium: Unlimited
* Upload: 10/day

---

# 📖 PDF Processing

On upload:

1. Store file in S3
2. Extract text with PyPDF2
3. Split into pages
4. Store pages in DB
5. Create chapters (optional heuristic)
6. Save total_pages

---

# ⚡ AI Caching Strategy

Use Redis.

Cache Key Format:

```
ai:{user_id}:{book_id}:{page_boundary}:{hash_of_question}
```

TTL: 24 hours

---

# 📊 Engagement Features

* Reading streak tracking (daily reading)
* Vocabulary log auto-populated from word lookup
* Analytics dashboard
* Highlights + Notes

---

# 🧪 Testing Requirements

### Must Achieve:

* 100% coverage on spoiler_guard
* 95% coverage on auth
* 90% coverage on ai_service

Test Types:

* Unit tests
* Integration tests
* API tests
* Boundary violation tests

---

# 🚀 Implementation Roadmap (For Coding Agent)

## Phase 1 – Backend Foundation

1. Setup FastAPI project
2. Setup DB models
3. Implement authentication
4. Implement book upload
5. Implement reading progress
6. Implement word meaning endpoint

## Phase 2 – Spoiler Guard

1. Build boundary extractor
2. Build prompt constructor
3. Build response validator
4. Add Redis caching
5. Add AI interaction logging

## Phase 3 – Frontend MVP

1. Auth screens
2. Library screen
3. PDF Reader screen
4. Tap word → AI meaning
5. Progress tracking

## Phase 4 – AI Features

1. Page summary
2. Till-here summary
3. Ask question drawer
4. Concept explanation

## Phase 5 – Engagement

1. Highlights
2. Notes
3. Streak system
4. Vocabulary spaced repetition

---

# 🛡 Security Requirements

* TLS 1.3 only
* CORS whitelist
* S3 encryption enabled
* RDS encryption enabled
* Secrets in AWS Secrets Manager
* Never expose API keys in frontend

---

# ✅ MVP Success Criteria

* User uploads PDF successfully
* Reader works
* Word meaning works
* Summaries never reveal future content
* Progress syncs
* Deployed to TestFlight

---

# 📌 Non-Negotiables

* Spoiler guard must be enforced server-side
* No AI call without boundary check
* All AI calls logged
* All AI responses validated
* Caching must include page boundary

---

# 🧩 Future Extensions (Not MVP)

* Offline AI mode (llama.cpp)
* Social reading
* Knowledge graph
* Flashcards
* Web version

---

# 🔥 Final Instruction to Coding Agent

Build incrementally.

Do NOT:

* Skip authentication
* Skip spoiler guard
* Skip caching
* Expose raw book content to frontend unnecessarily

Always:

* Write tests
* Use type hints
* Log critical events
* Validate AI outputs

---

This README defines the implementation blueprint for BookBuddy 2.0 as described in the technical document .

---


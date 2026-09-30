# Small Chat App (FastAPI + PostgreSQL)

A small backend-only chat API built to learn FastAPI, async SQLAlchemy, PostgreSQL, and Alembic. Users can be created, chats can be created, and messages can be posted to a chat and listed back.

> This is a learning project, not a production-ready chat system.

## Features

- Health check endpoint
- Create and list users
- Create and list chats
- Send a message to a chat
- List messages in a chat
- Async database access with SQLAlchemy 2.x
- Database migrations with Alembic
- Interactive API docs via Swagger UI

## Tech stack

- Python 3.12
- FastAPI
- Uvicorn
- SQLAlchemy 2.x (async)
- asyncpg (PostgreSQL driver)
- Pydantic v2 / pydantic-settings
- Alembic

## Project structure

```
.
├── alembic/            # Database migrations
├── app/
│   ├── models/         # SQLAlchemy models
│   ├── routers/        # API routes
│   ├── schemas/        # Pydantic request/response schemas
│   ├── diagram/        # ER diagram
│   ├── base.py         # Declarative base and timestamp mixin
│   └── main.py         # FastAPI app entry point
├── config.py           # Settings loaded from .env
├── database.py         # Async engine and session dependency
├── alembic.ini
└── requirements.txt
```

## Database schema

- **users** — id, username (unique), email (unique), created_at
- **chats** — id, chatname, created_at
- **messages** — id, content, user_id (FK), chat_id (FK), created_at

![ER diagram](app/diagram/Small_chatapp_diagram.png)

## Getting started

### Prerequisites

- Python 3.12
- PostgreSQL running locally

### 1. Clone the repository

```bash
git clone https://github.com/CSRidwanulHaque/Small_Chatapp_Fastapi.git
cd Small_Chatapp_Fastapi
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Copy `.env.example` to `.env` and update the connection string:

```
DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/small_chatapp
```

Create the database if it doesn't exist:

```bash
createdb small_chatapp
```

### 5. Run migrations

```bash
alembic upgrade head
```

### 6. Start the server

```bash
uvicorn app.main:app --reload
```

### 7. Open the docs

Visit http://127.0.0.1:8000/docs and use the "Try it out" buttons.

## API endpoints

| Method | Path | Description |
| ------ | ---- | ----------- |
| GET  | /health | Health check |
| POST | /users | Create a user |
| GET  | /users | List users |
| POST | /chats | Create a chat |
| GET  | /chats | List chats |
| POST | /messages | Send a message to a chat |
| GET  | /chats/{chat_id}/messages | List messages in a chat |

### Example: create a user

```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "email": "alice@example.com"}'
```

### Example: create a chat

```bash
curl -X POST http://127.0.0.1:8000/chats \
  -H "Content-Type: application/json" \
  -d '{"chatname": "general"}'
```

### Example: send a message

```bash
curl -X POST http://127.0.0.1:8000/messages \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "chat_id": 1, "content": "Hello everyone"}'
```

### Example: list messages in a chat

```bash
curl http://127.0.0.1:8000/chats/1/messages
```

## What I learned

- How to structure a FastAPI project (routers, schemas, models)
- How Pydantic validates requests and shapes responses
- How FastAPI dependencies provide a database session per request
- Async SQLAlchemy sessions with PostgreSQL
- How to read Swagger/OpenAPI docs

## Possible next steps

- Duplicate username/email validation and proper error responses
- Authentication (JWT)
- Real-time messaging with WebSockets
- Chat membership and roles
- Automated tests (pytest)
- Docker for easier setup


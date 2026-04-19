# Local Run Guide

## Flutter Client
```bash
cd apps/flutter_client
flutter pub get
flutter run
```

## API Service
```bash
cd services/api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## First Endpoints
- GET /health
- POST /auth/login
- GET /conversations
- POST /conversations
- GET /conversations/{conversation_id}/messages
- POST /conversations/{conversation_id}/messages

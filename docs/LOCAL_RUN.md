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


## Realtime Gateway
```bash
cd services/realtime_gateway
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8100
```

## Next Planned Runtime Pieces
- persistent database integration
- realtime STT streaming
- TTS generation service
- orchestrator wiring


## Notes
- API startup now initializes a local SQLite database automatically.
- Current auth and persistence layers are scaffolds and should be replaced with production-ready implementations in later passes.

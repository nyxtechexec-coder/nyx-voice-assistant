# Architecture

## Client Applications
### Flutter App
Single codebase targeting:
- Android
- iOS
- Windows

## Backend Services
- API service for auth and app requests
- realtime conversation gateway using WebSockets
- orchestration service for assistant logic
- memory service
- action/tool execution service
- notification service

## Data Layer
- PostgreSQL for durable data
- Redis for realtime/session buffering
- object storage for audio and artifacts

## AI Layer
- speech-to-text service
- LLM orchestration service
- text-to-speech service
- memory retrieval and routing layer

## Recommended Stack
- Flutter frontend
- FastAPI backend
- PostgreSQL
- Redis
- WebSockets
- Deepgram for STT
- ElevenLabs for TTS
- GPT-class model for orchestration

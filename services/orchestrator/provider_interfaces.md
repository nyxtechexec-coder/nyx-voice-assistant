# Provider Interfaces

## STT Provider Interface
- start_stream()
- send_audio_chunk(bytes)
- receive_partial_transcript()
- receive_final_transcript()
- stop_stream()

## TTS Provider Interface
- synthesize(text, voice_id, format)
- return audio artifact URL or bytes

## Orchestration Layer Interface
- accept user turn
- retrieve memory context
- produce assistant response
- request tool actions when required
- return text and optional audio instructions

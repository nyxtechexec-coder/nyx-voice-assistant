# API Contracts

## Overview
The system will expose a mix of REST APIs and realtime WebSocket channels.

## Authentication APIs
### POST /auth/login
- input: email, password or provider token
- output: access token, refresh token, user profile

### POST /auth/refresh
- input: refresh token
- output: new access token

### POST /auth/logout
- input: access token / refresh token
- output: success status

## Conversation APIs
### POST /conversations
- input: optional device id, title seed
- output: conversation id, created metadata

### GET /conversations
- output: user conversation list

### GET /conversations/{conversationId}
- output: conversation metadata, messages

### POST /conversations/{conversationId}/messages
- input: message content, role, mode(text/voice)
- output: stored message object

## Memory APIs
### GET /memory
- query: type, search, limit
- output: memory items

### POST /memory
- input: memory item payload
- output: created memory item

### PATCH /memory/{memoryId}
- input: updated fields
- output: updated memory item

## Actions APIs
### POST /actions
- input: action type, payload, conversation id
- output: action request object, approval status

### POST /actions/{actionId}/approve
- input: approval confirmation
- output: execution status

### GET /actions/{actionId}
- output: action request and execution log

## Notes and Reminders APIs
### POST /notes
### GET /notes
### POST /reminders
### GET /reminders

## Preferences APIs
### GET /preferences
### PATCH /preferences

## Realtime WebSocket
### /ws/conversation
Events:
- audio_chunk
- partial_transcript
- final_transcript
- assistant_text_delta
- assistant_message_complete
- assistant_audio_ready
- action_required
- action_result
- error

## Realtime Session Contract
Client sends:
- auth token
- device metadata
- conversation id optional
- input mode metadata

Server sends:
- session accepted
- stream state updates
- turn events
- output events

# Database Schema

## Users
- id
- email
- display_name
- created_at
- updated_at

## Device Sessions
- id
- user_id
- device_type
- device_name
- platform
- refresh_token_hash
- last_seen_at
- created_at
- revoked_at

## Conversations
- id
- user_id
- title
- created_at
- updated_at
- archived_at

## Conversation Messages
- id
- conversation_id
- role
- content_text
- content_audio_url
- source_mode
- created_at
- metadata_json

## Memory Items
- id
- user_id
- memory_type
- content
- tags_json
- importance_score
- created_at
- updated_at

## Preferences
- id
- user_id
- key
- value_json
- updated_at

## Action Requests
- id
- user_id
- conversation_id
- action_type
- payload_json
- approval_required
- approval_status
- execution_status
- created_at
- updated_at

## Action Execution Logs
- id
- action_request_id
- status
- result_json
- error_text
- created_at

## Notes
- id
- user_id
- title
- content
- created_at
- updated_at

## Reminders
- id
- user_id
- title
- reminder_at
- status
- payload_json
- created_at
- updated_at

## Suggested Relationships
- users 1..n device_sessions
- users 1..n conversations
- conversations 1..n conversation_messages
- users 1..n memory_items
- users 1..n notes
- users 1..n reminders
- users 1..n action_requests
- action_requests 1..n action_execution_logs

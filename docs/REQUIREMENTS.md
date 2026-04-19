# Requirements

## Functional Requirements
1. User can speak to the assistant using voice input.
2. System transcribes speech to text in near real time.
3. Assistant can respond in text and spoken audio.
4. Assistant maintains session context.
5. Assistant stores long-term user preferences and memory.
6. Assistant can execute approved actions through tools/integrations.
7. User can use the same assistant identity across mobile and Windows.
8. User can view transcript and action history.
9. System supports push-to-talk in MVP.
10. System supports text fallback input.

## Non-Functional Requirements
- low response latency
- high speech accuracy
- natural voice quality
- secure authentication
- encrypted session handling
- auditable action logs
- modular architecture
- cross-platform maintainability

## Safety Requirements
- explicit approval before sensitive actions
- permission scoping per integration
- user-visible action logs
- revocable device sessions
- no raw credentials stored insecurely in client

from datetime import datetime, UTC
from uuid import uuid4
from app.schemas.conversation import (
    ConversationCreateRequest,
    ConversationResponse,
    MessageCreateRequest,
    MessageResponse,
)

_CONVERSATIONS: list[ConversationResponse] = []
_MESSAGES: dict[str, list[MessageResponse]] = {}


def create_conversation(payload: ConversationCreateRequest) -> ConversationResponse:
    convo = ConversationResponse(
        id=str(uuid4()),
        title=payload.title or "New Conversation",
        created_at=datetime.now(UTC),
    )
    _CONVERSATIONS.append(convo)
    _MESSAGES[convo.id] = []
    return convo


def list_conversations() -> list[ConversationResponse]:
    return _CONVERSATIONS


def add_message(conversation_id: str, payload: MessageCreateRequest) -> MessageResponse:
    message = MessageResponse(
        id=str(uuid4()),
        conversation_id=conversation_id,
        role=payload.role,
        content=payload.content,
        source_mode=payload.source_mode,
        created_at=datetime.now(UTC),
    )
    _MESSAGES.setdefault(conversation_id, []).append(message)
    return message


def list_messages(conversation_id: str) -> list[MessageResponse]:
    return _MESSAGES.get(conversation_id, [])

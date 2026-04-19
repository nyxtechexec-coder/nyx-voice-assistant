from datetime import datetime, UTC
from uuid import uuid4
from app.schemas.conversation import ConversationCreateRequest, ConversationResponse, MessageCreateRequest, MessageResponse


class ConversationRepository:
    def __init__(self):
        self._conversations: list[ConversationResponse] = []
        self._messages: dict[str, list[MessageResponse]] = {}

    def create_conversation(self, payload: ConversationCreateRequest) -> ConversationResponse:
        conversation = ConversationResponse(
            id=str(uuid4()),
            title=payload.title or "New Conversation",
            created_at=datetime.now(UTC),
        )
        self._conversations.append(conversation)
        self._messages[conversation.id] = []
        return conversation

    def list_conversations(self) -> list[ConversationResponse]:
        return self._conversations

    def add_message(self, conversation_id: str, payload: MessageCreateRequest) -> MessageResponse:
        message = MessageResponse(
            id=str(uuid4()),
            conversation_id=conversation_id,
            role=payload.role,
            content=payload.content,
            source_mode=payload.source_mode,
            created_at=datetime.now(UTC),
        )
        self._messages.setdefault(conversation_id, []).append(message)
        return message

    def list_messages(self, conversation_id: str) -> list[MessageResponse]:
        return self._messages.get(conversation_id, [])

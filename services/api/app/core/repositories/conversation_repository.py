from datetime import datetime, UTC
from uuid import uuid4
from sqlalchemy.orm import Session
from app.models.conversation import Conversation, ConversationMessage
from app.schemas.conversation import ConversationCreateRequest, ConversationResponse, MessageCreateRequest, MessageResponse


class ConversationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_conversation(self, payload: ConversationCreateRequest, user_id: str = "demo-user") -> ConversationResponse:
        conversation = Conversation(
            id=str(uuid4()),
            user_id=user_id,
            title=payload.title or "New Conversation",
            created_at=datetime.now(UTC),
        )
        self.db.add(conversation)
        self.db.commit()
        self.db.refresh(conversation)
        return ConversationResponse(
            id=conversation.id,
            title=conversation.title,
            created_at=conversation.created_at,
        )

    def list_conversations(self, user_id: str = "demo-user") -> list[ConversationResponse]:
        rows = self.db.query(Conversation).filter(Conversation.user_id == user_id).order_by(Conversation.created_at.desc()).all()
        return [
            ConversationResponse(id=row.id, title=row.title, created_at=row.created_at)
            for row in rows
        ]

    def add_message(self, conversation_id: str, payload: MessageCreateRequest) -> MessageResponse:
        message = ConversationMessage(
            id=str(uuid4()),
            conversation_id=conversation_id,
            role=payload.role,
            content_text=payload.content,
            source_mode=payload.source_mode,
            created_at=datetime.now(UTC),
        )
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return MessageResponse(
            id=message.id,
            conversation_id=message.conversation_id,
            role=message.role,
            content=message.content_text,
            source_mode=message.source_mode,
            created_at=message.created_at,
        )

    def list_messages(self, conversation_id: str) -> list[MessageResponse]:
        rows = self.db.query(ConversationMessage).filter(ConversationMessage.conversation_id == conversation_id).order_by(ConversationMessage.created_at.asc()).all()
        return [
            MessageResponse(
                id=row.id,
                conversation_id=row.conversation_id,
                role=row.role,
                content=row.content_text,
                source_mode=row.source_mode,
                created_at=row.created_at,
            )
            for row in rows
        ]

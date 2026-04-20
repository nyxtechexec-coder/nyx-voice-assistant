from sqlalchemy.orm import Session
from app.core.repositories.conversation_repository import ConversationRepository
from app.schemas.conversation import ConversationCreateRequest, ConversationResponse, MessageCreateRequest, MessageResponse


def create_conversation(db: Session, payload: ConversationCreateRequest) -> ConversationResponse:
    return ConversationRepository(db).create_conversation(payload)


def list_conversations(db: Session) -> list[ConversationResponse]:
    return ConversationRepository(db).list_conversations()


def add_message(db: Session, conversation_id: str, payload: MessageCreateRequest) -> MessageResponse:
    return ConversationRepository(db).add_message(conversation_id, payload)


def list_messages(db: Session, conversation_id: str) -> list[MessageResponse]:
    return ConversationRepository(db).list_messages(conversation_id)

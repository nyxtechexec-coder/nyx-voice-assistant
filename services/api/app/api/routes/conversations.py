from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.conversation import (
    ConversationCreateRequest,
    ConversationResponse,
    MessageCreateRequest,
    MessageResponse,
)
from app.services.conversation_service import (
    create_conversation,
    list_conversations,
    add_message,
    list_messages,
)

router = APIRouter(prefix="/conversations", tags=["conversations"])


@router.get("", response_model=list[ConversationResponse])
def list_conversations_endpoint(db: Session = Depends(get_db)):
    return list_conversations(db)


@router.post("", response_model=ConversationResponse)
def create_conversation_endpoint(payload: ConversationCreateRequest, db: Session = Depends(get_db)):
    return create_conversation(db, payload)


@router.get("/{conversation_id}/messages", response_model=list[MessageResponse])
def list_messages_endpoint(conversation_id: str, db: Session = Depends(get_db)):
    return list_messages(db, conversation_id)


@router.post("/{conversation_id}/messages", response_model=MessageResponse)
def create_message_endpoint(conversation_id: str, payload: MessageCreateRequest, db: Session = Depends(get_db)):
    return add_message(db, conversation_id, payload)

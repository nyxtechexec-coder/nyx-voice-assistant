from fastapi import APIRouter
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
def list_conversations_endpoint():
    return list_conversations()


@router.post("", response_model=ConversationResponse)
def create_conversation_endpoint(payload: ConversationCreateRequest):
    return create_conversation(payload)


@router.get("/{conversation_id}/messages", response_model=list[MessageResponse])
def list_messages_endpoint(conversation_id: str):
    return list_messages(conversation_id)


@router.post("/{conversation_id}/messages", response_model=MessageResponse)
def create_message_endpoint(conversation_id: str, payload: MessageCreateRequest):
    return add_message(conversation_id, payload)

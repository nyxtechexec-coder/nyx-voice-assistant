from app.core.repositories.conversation_repository import ConversationRepository
from app.schemas.conversation import ConversationCreateRequest, ConversationResponse, MessageCreateRequest, MessageResponse

repository = ConversationRepository()


def create_conversation(payload: ConversationCreateRequest) -> ConversationResponse:
    return repository.create_conversation(payload)


def list_conversations() -> list[ConversationResponse]:
    return repository.list_conversations()


def add_message(conversation_id: str, payload: MessageCreateRequest) -> MessageResponse:
    return repository.add_message(conversation_id, payload)


def list_messages(conversation_id: str) -> list[MessageResponse]:
    return repository.list_messages(conversation_id)

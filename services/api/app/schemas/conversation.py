from datetime import datetime
from pydantic import BaseModel


class ConversationCreateRequest(BaseModel):
    title: str | None = None


class ConversationResponse(BaseModel):
    id: str
    title: str
    created_at: datetime


class MessageCreateRequest(BaseModel):
    role: str
    content: str
    source_mode: str = "text"


class MessageResponse(BaseModel):
    id: str
    conversation_id: str
    role: str
    content: str
    source_mode: str
    created_at: datetime

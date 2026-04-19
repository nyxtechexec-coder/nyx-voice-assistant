from pydantic import BaseModel


class BaseEvent(BaseModel):
    event: str


class SessionAcceptedEvent(BaseEvent):
    message: str


class PartialTranscriptEvent(BaseEvent):
    text: str


class AssistantDeltaEvent(BaseEvent):
    delta: str


class ActionRequiredEvent(BaseEvent):
    action_type: str
    summary: str

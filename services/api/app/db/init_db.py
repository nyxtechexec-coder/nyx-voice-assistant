from app.db.base import Base
from app.db.session import engine
from app.models.user import User
from app.models.conversation import Conversation, ConversationMessage
from app.models.device_session import DeviceSession


def init_db() -> None:
    Base.metadata.create_all(bind=engine)

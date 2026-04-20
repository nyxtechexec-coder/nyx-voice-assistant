from uuid import uuid4
from app.schemas.auth import LoginRequest, TokenResponse


def login(request: LoginRequest) -> TokenResponse:
    return TokenResponse(
        access_token=f"demo-access-token-{uuid4()}",
        refresh_token=f"demo-refresh-token-{uuid4()}",
        user_id="demo-user",
    )

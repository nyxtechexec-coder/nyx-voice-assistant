from app.schemas.auth import LoginRequest, TokenResponse


def login(request: LoginRequest) -> TokenResponse:
    return TokenResponse(
        access_token=f"demo-access-token-for-{request.email}",
        refresh_token="demo-refresh-token",
    )

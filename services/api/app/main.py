from fastapi import FastAPI
from app.api.routes.auth import router as auth_router
from app.api.routes.conversations import router as conversations_router
from app.db.init_db import init_db

app = FastAPI(title="Nyx Voice Assistant API", version="0.1.0")
app.include_router(auth_router)
app.include_router(conversations_router)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/health")
def health():
    return {"status": "ok", "service": "api"}

from fastapi import FastAPI, WebSocket

app = FastAPI(title="Nyx Realtime Gateway", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "realtime_gateway"}


@app.websocket("/ws/conversation")
async def conversation_ws(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"event": "session.accepted", "message": "Realtime channel connected"})
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_json({"event": "echo", "payload": data})
    except Exception:
        await websocket.close()

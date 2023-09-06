from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from router import router as chat
from json_methods import MessageProcessing

app = FastAPI(
    title= 'Websocket Chat'
)
app.include_router(chat)

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    processing = MessageProcessing()
    try:
        while True:
            data = await websocket.receive_text()
            processing.set_message(user_id=client_id, data=data)
            await manager.send_personal_message(processing.get_message(user_id=client_id), websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
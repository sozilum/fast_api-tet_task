from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from router import router as chat
from json_methods import MessageProcessing

app = FastAPI(
    title= 'Websocket Chat'
)
app.include_router(chat)
processing = MessageProcessing()

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
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(processing.process_message(user_id=client_id, data=data), websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        processing.clear_desconnected_user_count(user_id=client_id)
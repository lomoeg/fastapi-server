from fastapi import FastAPI
from app.server.routes.chatRoutes import chatRouter
from app.server.routes.msgRoutes import msgRouter

app = FastAPI()

app.include_router(chatRouter, tags=["Chat"], prefix="/chat")
app.include_router(msgRouter, tags=["Message"], prefix="/msg")


@app.get("/")
async def root():
    return {"message": "Heeeey"}

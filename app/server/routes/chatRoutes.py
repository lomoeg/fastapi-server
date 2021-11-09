from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_chat,
    retrieve_chat_list,
    retrieve_chat,
    update_chat,
    retrieve_all_msg_by_chat_id,
)

from app.server.models.chatModel import (
    ErrorResponseModel,
    ResponseModel,
    ChatSchema,
    UpdateChatModel,
)

chatRouter = APIRouter()


@chatRouter.post("/", response_description="Chat data added into the database")
async def create_new_chat(chat: ChatSchema = Body(...)):
    chat = jsonable_encoder(chat)
    new_chat = await add_chat(chat)
    return ResponseModel(new_chat, "Chat added successfully.")


@chatRouter.get("/", response_description="All chats retrieved")
async def get_all_chats_metadata():
    chats = await retrieve_chat_list()
    if chats:
        return ResponseModel(chats, "Chats data retrieved successfully")
    return ResponseModel(chats, "Empty list returned")


@chatRouter.get("/{id}", response_description="Chat data retrieved")
async def get_full_chat_data(id):
    chat = await retrieve_chat(id)
    messages = await retrieve_all_msg_by_chat_id(id)
    result = [chat, messages]
    if result:
        return ResponseModel(result, "Chat data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Chat doesn't exist.")


@chatRouter.put("/{id}")
async def update_chat(id: str, req: UpdateChatModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_chat = await update_chat(id, req)
    if updated_chat:
        return ResponseModel(
            "Chat with ID: {} name update is successful".format(id),
            "Chat updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the chat data.",
    )


from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_new_msg,
)


from app.server.models.msgModel import (
    ResponseModel,
    MessageSchema,
)

msgRouter = APIRouter()


@msgRouter.post("/", response_description="Message data added into the database")
async def add_new_message(msg: MessageSchema = Body(...)):
    msg = jsonable_encoder(msg)
    new_msg = await add_new_msg(msg)
    return ResponseModel(new_msg, "Message added successfully.")

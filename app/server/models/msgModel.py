from typing import Optional

from pydantic import BaseModel, Field


class MessageSchema(BaseModel):
    # 0 - most negative, 9 - most positive
    chat_id: str = Field(...)
    msg_text: str = Field(...)
    datetime: str = Field(...)
    emotional_tone: int = Field(..., gt=0, lt=10)

    class Config:
        schema_extra = {
            "example": {
                "chat_id": "614214b59b4a2ec937011592",
                "msg_text": "Привет! Как узнать лимит снятия наличных?",
                "datetime": "14:25 09/09/2021",
                "emotional_tone": 9,
            }
        }


class UpdateMessageModel(BaseModel):
    chat_id: Optional[str]
    msg_text: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "chat_id": "614214b59b4a2ec937011592",
                "msg_text": "Привет! Как узнать лимит снятия наличных?",
                "datetime": "14:25 09/09/2021",
                "emotional_tone": 9,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

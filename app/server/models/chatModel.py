from typing import Optional

from pydantic import BaseModel, Field


class ChatSchema(BaseModel):
    # 0 - most negative, 9 - most positive
    emotional_tone: int = Field(..., gt=0, lt=10)
    operator: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "emotional_tone": 9,
                "operator": "operator 23",
            }
        }


class UpdateChatModel(BaseModel):
    emotional_tone: Optional[int]
    operator: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "emotional_tone": 9,
                "operator": "operator 23",
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

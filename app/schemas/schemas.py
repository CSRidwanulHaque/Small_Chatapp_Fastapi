from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    username: str
    email: str


class UserResponse(BaseModel):
    id: int
    username: str
    model_config = ConfigDict(from_attributes=True)


class MessageCreate(BaseModel):
    user_id: int
    chat_id: int
    content: str


class MessageResponse(BaseModel):
    id: int
    content: str
    user_id: int
    chat_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)



class ChatCreate(BaseModel):
    chatname: str


class ChatResponse(BaseModel):
    id: int
    chatname: str
    model_config = ConfigDict(from_attributes=True)

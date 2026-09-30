from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.models import User, Chat, Message
from app.schemas.schemas import (
    UserCreate,
    UserResponse,
    ChatCreate,
    ChatResponse,
    MessageCreate,
    MessageResponse,
)
from database import get_db

router = APIRouter()


@router.post("/users", response_model=UserResponse, status_code=201)
async def create_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    user = User(
        username=user_data.username,
        email=user_data.email,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user


@router.get("/users", response_model=list[UserResponse])
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(User).order_by(User.id))
    return result.all()


@router.get("/chats", response_model=list[ChatResponse])
async def list_chats(db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(Chat).order_by(Chat.id))
    return result.all()


@router.post("/chats", response_model=ChatResponse, status_code=201)
async def create_chat(
    chat_data: ChatCreate,
    db: AsyncSession = Depends(get_db),
):
    chat = Chat(chatname=chat_data.chatname)

    db.add(chat)
    await db.commit()
    await db.refresh(chat)

    return chat


@router.post("/messages", response_model=MessageResponse, status_code=201)
async def create_message(
    message_data: MessageCreate,
    db: AsyncSession = Depends(get_db),
):
    message = Message(
        user_id=message_data.user_id,
        chat_id=message_data.chat_id,
        content=message_data.content,
    )

    db.add(message)
    await db.commit()
    await db.refresh(message)

    return message


@router.get("/chats/{chat_id}/messages", response_model=list[MessageResponse])
async def list_messages(
    chat_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.scalars(
        select(Message).where(Message.chat_id == chat_id).order_by(Message.id)
    )
    return result.all()

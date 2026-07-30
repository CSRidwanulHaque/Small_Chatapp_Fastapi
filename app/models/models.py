from typing import List, Optional
from sqlalchemy import ForeignKey, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from base import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key= True)
    username: Mapped[str] = mapped_column(String(50),unique= True,index = True)
    email: Mapped[str] = mapped_column(String(150), unique=True)
    messages: Mapped[List["Message"]] = relationship(back_populates="sender",lazy="selectin")
class Message(Base):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(primary_key= True)
    content: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id",ondelete="CASCADE"))
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id",ondelete="CASCADE"))
    sender: Mapped["User"] = relationship(back_populates="messages")
    chat: Mapped["Chat"] = relationship(back_populates="messages")
class Chat(Base):
    __tablename__ = "chats"
    id: Mapped[int] = mapped_column(primary_key=True)
    chatname: Mapped[str | None] = mapped_column(String(50), nullable= True)
    messages: Mapped[List["Message"]] = relationship(back_populates="chat",lazy="selectin")
    
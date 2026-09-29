from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.models import User
from app.schemas.schemas import UserCreate, UserResponse
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

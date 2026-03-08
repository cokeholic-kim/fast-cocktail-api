from typing import Sequence
from app.repositories.user import UserRepository

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate
from app.models.user import User


async def create_user(db: AsyncSession, payload: UserCreate) -> User:
    user = User(
        nick_name=payload.nick_name,
        email=payload.email,
        password=payload.password,
        role=payload.role,
        login_method=payload.login_method,
    )
    return await UserRepository.create(db, user)


async def list_users(db: AsyncSession) -> Sequence[User]:
    users = await UserRepository.list_all(db)
    return users


async def exists_by_email(db: AsyncSession, email: str) -> bool:
    return await UserRepository.exists_by_email(db, email)

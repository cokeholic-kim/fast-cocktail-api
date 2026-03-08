from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.models.enums import LoginMethod, UserRole


class UserRepository:
    @staticmethod
    async def list_all(db: AsyncSession) -> list[User]:
        result = await db.execute(select(User).order_by(User.id.asc()))
        return list(result.scalars().all())

    @staticmethod
    async def create(db: AsyncSession, user: User) -> User:
        db.add(user)
        await db.flush()
        await db.refresh(user)
        return user

    @staticmethod
    async def exists_by_nick_name(db: AsyncSession, nick_name: str) -> bool:
        result = await db.execute(select(User.id).where(User.nick_name == nick_name))
        return result.scalar_one_or_none() is not None

    @staticmethod
    async def exists_by_email(db: AsyncSession, email: str) -> bool:
        result = await db.execute(select(User.id).where(User.email == email))
        return result.scalar_one_or_none() is not None

    @staticmethod
    async def find_by_email(db: AsyncSession, email: str) -> User | None:
        result = await db.execute(select(User).where(User.email == email))
        return result.scalars().first()

    @staticmethod
    async def find_by_id_and_email(db: AsyncSession, id: int, email: str) -> User | None:
        result = await db.execute(select(User).where(User.id == id, User.email == email))
        return result.scalars().first()

    @staticmethod
    async def find_by_nick_name(db: AsyncSession, nick_name: str) -> User | None:
        result = await db.execute(select(User).where(User.nick_name == nick_name))
        return result.scalars().first()

    @staticmethod
    async def find_by_email_and_role_and_login_method(
        db: AsyncSession,
        email: str,
        role: UserRole,
        login_method: LoginMethod,
    ) -> User | None:
        stmt = select(User).where(
            User.email == email,
            User.role == role,
            User.login_method == login_method,
        )
        result = await db.execute(stmt)
        return result.scalars().first()

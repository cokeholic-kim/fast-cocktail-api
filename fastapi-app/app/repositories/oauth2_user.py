from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Oauth2User


class Oauth2UserRepository:
    @staticmethod
    async def find_by_email(db: AsyncSession, email: str) -> Oauth2User | None:
        result = await db.execute(select(Oauth2User).where(Oauth2User.email == email))
        return result.scalars().first()

    @staticmethod
    async def find_by_email_and_domain(db: AsyncSession, email: str, domain: str) -> Oauth2User | None:
        stmt = select(Oauth2User).where(
            Oauth2User.email == email,
            Oauth2User.domain == domain,
        )
        result = await db.execute(stmt)
        return result.scalars().first()

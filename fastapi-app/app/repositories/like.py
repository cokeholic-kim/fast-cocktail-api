from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Like


class LikeRepository:
    @staticmethod
    async def create(db: AsyncSession, like: Like) -> Like:
        db.add(like)
        await db.flush()
        await db.refresh(like)
        return like

    @staticmethod
    async def list_all(db: AsyncSession) -> list[Like]:
        result = await db.execute(select(Like).order_by(Like.id.asc()))
        return list(result.scalars().all())

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Banner


class BannerRepository:
    @staticmethod
    async def find_all_order_by_order(db: AsyncSession) -> list[Banner]:
        result = await db.execute(select(Banner).order_by(Banner.order.asc()))
        return list(result.scalars().all())

    @staticmethod
    async def find_by_title(db: AsyncSession, title: str) -> Banner | None:
        result = await db.execute(select(Banner).where(Banner.title == title))
        return result.scalars().first()

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Cocktail


class CocktailRepository:
    @staticmethod
    async def find_by_cocktail_name(db: AsyncSession, cocktail_name: str) -> Cocktail | None:
        result = await db.execute(select(Cocktail).where(Cocktail.cocktail_name == cocktail_name))
        return result.scalars().first()

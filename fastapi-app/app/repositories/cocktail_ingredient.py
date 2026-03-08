from __future__ import annotations

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Cocktail, CocktailIngredient


class CocktailIngredientRepository:
    @staticmethod
    async def delete_all_by_cocktail(db: AsyncSession, cocktail: Cocktail) -> None:
        await db.execute(
            delete(CocktailIngredient).where(CocktailIngredient.cocktail_id == cocktail.id)
        )

from __future__ import annotations

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Ingredient


class IngredientRepository:
    @staticmethod
    async def find_by_name(db: AsyncSession, name: str) -> Ingredient | None:
        result = await db.execute(select(Ingredient).where(Ingredient.name == name))
        return result.scalars().first()

    @staticmethod
    async def find_all_by_name(db: AsyncSession, name: str) -> list[Ingredient]:
        result = await db.execute(select(Ingredient).where(Ingredient.name == name))
        return list(result.scalars().all())

    @staticmethod
    async def find_all_by_name_in(db: AsyncSession, names: list[str]) -> list[Ingredient]:
        result = await db.execute(select(Ingredient).where(Ingredient.name.in_(names)))
        return list(result.scalars().all())

    @staticmethod
    async def exists_by_name(db: AsyncSession, name: str) -> bool:
        result = await db.execute(select(Ingredient.id).where(Ingredient.name == name))
        return result.scalar_one_or_none() is not None

    @staticmethod
    async def exists_by_en_name(db: AsyncSession, en_name: str) -> bool:
        result = await db.execute(select(Ingredient.id).where(Ingredient.en_name == en_name))
        return result.scalar_one_or_none() is not None

    @staticmethod
    async def create(db: AsyncSession, ingredient: Ingredient) -> Ingredient:
        db.add(ingredient)
        await db.flush()
        await db.refresh(ingredient)
        return ingredient

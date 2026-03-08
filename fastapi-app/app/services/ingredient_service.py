from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.ingredient import IngredientRepository


async def get_by_name(db: AsyncSession, name: str):
    return await IngredientRepository.find_by_name(db, name)


async def get_all_by_name(db: AsyncSession, name: str):
    return await IngredientRepository.find_all_by_name(db, name)


async def get_all_by_name_in(db: AsyncSession, names: list[str]):
    return await IngredientRepository.find_all_by_name_in(db, names)


async def exists_by_name(db: AsyncSession, name: str) -> bool:
    return await IngredientRepository.exists_by_name(db, name)


async def exists_by_en_name(db: AsyncSession, en_name: str) -> bool:
    return await IngredientRepository.exists_by_en_name(db, en_name)

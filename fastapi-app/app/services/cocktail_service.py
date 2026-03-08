from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.cocktail import CocktailRepository


async def get_cocktail_by_name(db: AsyncSession, name: str):
    return await CocktailRepository.find_by_cocktail_name(db, name)

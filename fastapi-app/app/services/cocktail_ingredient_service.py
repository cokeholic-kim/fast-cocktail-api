from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Cocktail
from app.repositories.cocktail_ingredient import CocktailIngredientRepository


async def delete_all_cocktail_ingredients(db: AsyncSession, cocktail: Cocktail):
    return await CocktailIngredientRepository.delete_all_by_cocktail(db, cocktail)

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Like
from app.repositories.like import LikeRepository


async def create_like(db: AsyncSession, like: Like) -> Like:
    return await LikeRepository.create(db, like)


async def list_likes(db: AsyncSession):
    return await LikeRepository.list_all(db)

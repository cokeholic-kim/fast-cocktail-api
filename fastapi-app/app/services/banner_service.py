from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.banner import BannerRepository


async def list_banners_ordered(db: AsyncSession):
    return await BannerRepository.find_all_order_by_order(db)


async def get_banner_by_title(db: AsyncSession, title: str):
    return await BannerRepository.find_by_title(db, title)

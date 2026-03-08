from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.file import FileRepository


async def get_file_by_name(db: AsyncSession, file_name: str):
    return await FileRepository.find_by_file_name(db, file_name)

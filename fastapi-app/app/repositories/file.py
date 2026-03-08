from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import File


class FileRepository:
    @staticmethod
    async def find_by_file_name(db: AsyncSession, file_name: str) -> File | None:
        result = await db.execute(select(File).where(File.file_name == file_name))
        return result.scalars().first()

from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.enums import CommentRefCategory
from app.repositories.comment import CommentRepository


async def list_root_comments_by_ref(
    db: AsyncSession,
    ref_category: CommentRefCategory,
    ref_category_item: str,
):
    return await CommentRepository.find_root_comments(
        db,
        ref_category=ref_category,
        ref_category_item=ref_category_item,
    )

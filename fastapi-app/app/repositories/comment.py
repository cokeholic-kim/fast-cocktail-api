from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Comment
from app.models.enums import CommentRefCategory


class CommentRepository:
    @staticmethod
    async def find_root_comments(
        db: AsyncSession,
        ref_category: CommentRefCategory,
        ref_category_item: str,
    ) -> list[Comment]:
        result = await db.execute(
            select(Comment)
            .where(
                Comment.ref_category == ref_category,
                Comment.ref_category_item == ref_category_item,
                Comment.parent_comment_id.is_(None),
                Comment.deleted.is_(False),
            )
            .order_by(Comment.created_at.asc())
        )
        return list(result.scalars().all())

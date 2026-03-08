from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Enum as SAEnum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import CommentRefCategory


class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    parent_comment_id: Mapped[int | None] = mapped_column(ForeignKey("comment.id"), nullable=True)
    content: Mapped[str] = mapped_column(String(500), nullable=False)
    ref_category: Mapped[CommentRefCategory] = mapped_column(
        SAEnum(CommentRefCategory, native_enum=False, length=50),
        nullable=False,
    )
    ref_category_item: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    deleted: Mapped[bool] = mapped_column(Boolean(create_constraint=False), nullable=False)

    parent_comment: Mapped["Comment | None"] = relationship(
        "Comment",
        remote_side="Comment.id",
        back_populates="children",
    )
    children: Mapped[list["Comment"]] = relationship(
        back_populates="parent_comment",
        cascade="all, delete-orphan",
    )

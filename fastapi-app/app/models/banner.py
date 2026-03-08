from __future__ import annotations

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Banner(Base):
    __tablename__ = "banner"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    file_id: Mapped[int] = mapped_column(ForeignKey("files.id"), nullable=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    src: Mapped[str | None] = mapped_column(Text, nullable=True)
    order: Mapped[int] = mapped_column("order", nullable=False)

    file: Mapped["File"] = relationship("File")

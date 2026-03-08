from __future__ import annotations

from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import IngredientCategory, IngredientStatus


class Ingredient(Base):
    __tablename__ = "ingredient"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    en_name: Mapped[str] = mapped_column(String(100), nullable=False)
    category: Mapped[IngredientCategory] = mapped_column(
        SAEnum(IngredientCategory, native_enum=False, length=50),
        nullable=False,
    )
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    file_id: Mapped[int | None] = mapped_column(ForeignKey("files.id"), nullable=True)
    status: Mapped[IngredientStatus | None] = mapped_column(
        SAEnum(IngredientStatus, native_enum=False, length=50),
        nullable=True,
    )
    file: Mapped["File"] = relationship("File")

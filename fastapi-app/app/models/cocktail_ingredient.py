from __future__ import annotations

from sqlalchemy import Enum as SAEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import Unit


class CocktailIngredient(Base):
    __tablename__ = "cocktail_ingredient"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cocktail_id: Mapped[int] = mapped_column(ForeignKey("cocktail.id"), nullable=False)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredient.id"), nullable=False)
    volume: Mapped[float | None] = mapped_column(nullable=True)
    unit: Mapped[Unit] = mapped_column(
        SAEnum(Unit, native_enum=False, length=100),
        nullable=False,
    )

    cocktail: Mapped["Cocktail"] = relationship("Cocktail")
    ingredient: Mapped["Ingredient"] = relationship("Ingredient")

from __future__ import annotations

from sqlalchemy import Enum as SAEnum
from sqlalchemy import Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import CocktailStatus, Glass, Method


class Cocktail(Base):
    __tablename__ = "cocktail"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    cocktail_name: Mapped[str] = mapped_column(String(50), nullable=False)
    proof: Mapped[float] = mapped_column(Float, nullable=False)
    glass: Mapped[Glass] = mapped_column(
        SAEnum(Glass, native_enum=False, length=50),
        nullable=False,
    )
    method: Mapped[Method] = mapped_column(
        SAEnum(Method, native_enum=False, length=50),
        nullable=False,
    )
    garnish: Mapped[str | None] = mapped_column(nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[CocktailStatus] = mapped_column(
        SAEnum(CocktailStatus, native_enum=False, length=50),
        nullable=False,
        default=CocktailStatus.ADMIN_REGISTERED,
    )
    file_id: Mapped[int | None] = mapped_column(ForeignKey("files.id"), nullable=True)

    user: Mapped["User"] = relationship("User")
    file: Mapped["File"] = relationship("File")

from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.enums import UserRole, LoginMethod


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nick_name: Mapped[str] = mapped_column("nick_name", String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str | None] = mapped_column(String(50), nullable=True)
    role: Mapped[UserRole] = mapped_column(
        String(50),
        default=UserRole.ROLE_USER,
        nullable=False,
    )
    login_method: Mapped[LoginMethod] = mapped_column(
        String(50),
        default=LoginMethod.app,
        nullable=False,
    )

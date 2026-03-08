"""Initial schema for FastAPI PostgreSQL migration.

Revision ID: 202603080001
Revises:
Create Date: 2026-03-08
"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision = "202603080001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.BigInteger(), primary_key=True, nullable=False),
        sa.Column("nick_name", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("password", sa.String(length=50)),
        sa.Column("role", sa.String(length=50), nullable=False),
        sa.Column(
            "login_method",
            sa.String(length=50),
            nullable=False,
            server_default="app",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
    )

    op.create_table(
        "files",
        sa.Column("id", sa.BigInteger(), primary_key=True, nullable=False),
        sa.Column("file_name", sa.String(), nullable=True),
        sa.Column("file_path", sa.String(), nullable=True),
        sa.Column("file_size", sa.BigInteger(), nullable=True),
        sa.Column("file_type", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("uploader_id", sa.BigInteger(), sa.ForeignKey("users.id")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_files")),
    )

    op.create_table(
        "oauth_user",
        sa.Column("id", sa.BigInteger(), primary_key=True, nullable=False),
        sa.Column("user_id", sa.BigInteger(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("email", sa.String(length=200), nullable=False),
        sa.Column("domain", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_oauth_user")),
        sa.UniqueConstraint("user_id", name=op.f("uq_oauth_user_user_id")),
    )

    op.create_table(
        "ingredient",
        sa.Column("id", sa.BigInteger(), primary_key=True, nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("en_name", sa.String(length=100), nullable=False),
        sa.Column("category", sa.String(length=50), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("file_id", sa.BigInteger(), sa.ForeignKey("files.id")),
        sa.Column("status", sa.String(length=50)),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_ingredient")),
    )

    op.create_table(
        "cocktail",
        sa.Column("id", sa.BigInteger(), primary_key=True, nullable=False),
        sa.Column("user_id", sa.BigInteger(), sa.ForeignKey("users.id")),
        sa.Column("cocktail_name", sa.String(length=50), nullable=False),
        sa.Column("proof", sa.Float(), nullable=False),
        sa.Column("glass", sa.String(length=50), nullable=False),
        sa.Column("method", sa.String(length=50), nullable=False),
        sa.Column("garnish", sa.String(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column(
            "status",
            sa.String(length=50),
            nullable=False,
            server_default="ADMIN_REGISTERED",
        ),
        sa.Column("file_id", sa.BigInteger(), sa.ForeignKey("files.id")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_cocktail")),
    )

    op.create_table(
        "banner",
        sa.Column("id", sa.BigInteger(), primary_key=True, nullable=False),
        sa.Column("file_id", sa.BigInteger(), sa.ForeignKey("files.id")),
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("src", sa.Text(), nullable=True),
        sa.Column("order", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_banner")),
    )

    op.create_table(
        "comment",
        sa.Column("id", sa.BigInteger(), primary_key=True, nullable=False),
        sa.Column("user_id", sa.BigInteger(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("parent_comment_id", sa.BigInteger(), sa.ForeignKey("comment.id")),
        sa.Column("content", sa.String(length=500), nullable=False),
        sa.Column("ref_category", sa.String(length=50), nullable=False),
        sa.Column("ref_category_item", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("deleted", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_comment")),
    )

    op.create_table(
        "likes",
        sa.Column("id", sa.BigInteger(), primary_key=True, nullable=False),
        sa.Column("content_id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_likes")),
    )

    op.create_table(
        "cocktail_ingredient",
        sa.Column("id", sa.BigInteger(), primary_key=True, nullable=False),
        sa.Column("cocktail_id", sa.BigInteger(), sa.ForeignKey("cocktail.id"), nullable=False),
        sa.Column("ingredient_id", sa.BigInteger(), sa.ForeignKey("ingredient.id"), nullable=False),
        sa.Column("volume", sa.Float(), nullable=True),
        sa.Column("unit", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_cocktail_ingredient")),
    )


def downgrade() -> None:
    op.drop_table("cocktail_ingredient")
    op.drop_table("likes")
    op.drop_table("comment")
    op.drop_table("banner")
    op.drop_table("cocktail")
    op.drop_table("ingredient")
    op.drop_table("oauth_user")
    op.drop_table("files")
    op.drop_table("users")

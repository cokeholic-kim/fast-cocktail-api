from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, list_users

router = APIRouter()


@router.get("/users", response_model=list[UserResponse])
async def users(session: AsyncSession = Depends(get_db)):
    return await list_users(session)


@router.post("/users", response_model=UserResponse)
async def create_user_route(
    payload: UserCreate,
    session: AsyncSession = Depends(get_db),
):
    return await create_user(session, payload)

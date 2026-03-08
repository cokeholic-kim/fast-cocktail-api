from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.oauth2_user import Oauth2UserRepository


async def get_oauth2_user_by_email(db: AsyncSession, email: str):
    return await Oauth2UserRepository.find_by_email(db, email)


async def get_oauth2_user_by_email_and_domain(db: AsyncSession, email: str, domain: str):
    return await Oauth2UserRepository.find_by_email_and_domain(db, email, domain)

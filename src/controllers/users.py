from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.core.settings import settings
from src.core.logger import get_logger
from src.db.db_session import db_session
from src.db.models import Address
from src.db.models.users import User
from src.schemas.users import UserCreateSchema

logger = get_logger(__name__)


class UserController:
    @staticmethod
    @db_session
    async def create_user(session, user: UserCreateSchema):
        try:
            logger.info(f"url: {settings.db.url}")
            # data = user.model_dump()
            logger.info(f"Creating user {user}")
            user = User(**user.model_dump())

            session.add(user)
            await session.commit()
            return user
        except Exception as e:
            logger.error(f"Error while creating user: {e}")
            await session.rollback()

    @staticmethod
    @db_session
    async def get_user(session, user_id: int):

        result = await session.execute(select(User).where(User.id == user_id))
        user = await result.scalar()
        if user is None:
            raise HTTPException(status_code=400, detail="User not found")

        return user

    @staticmethod
    @db_session
    async def get_all_users(session):
        result = await session.execute(
            select(User).options(joinedload(User.address)).options(joinedload(User.credit_card)))
        company = await result.unique().scalars().all()
        return company

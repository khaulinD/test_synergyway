import re
from sqlalchemy import DateTime, func
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

Base = declarative_base()


class BaseMixin:
    '''
    Base class for PostgreSQL databases. That creat id and correct name
    '''
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        # Convert camel case or Pascal case to snake case
        return re.sub(r'([a-z])([A-Z])', r'\1_\2', cls.__name__).lower() + 's'

    id: Mapped[int] = mapped_column(primary_key=True)

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base import Base, BaseMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.db.models.addresses import Address
    from src.db.models.credit_card import CreditCard


class User(Base, BaseMixin):
    name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)

    address = relationship("Address", back_populates="user")
    credit_card = relationship("CreditCard", back_populates="user")

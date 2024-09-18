from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base import Base, BaseMixin


class CreditCard(Base, BaseMixin):

    number: Mapped[str] = mapped_column(String)
    expiration_date: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="credit_card")
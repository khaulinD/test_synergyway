from src.core.logger import get_logger
from src.db.db_session import db_session
from src.db.models import CreditCard
from src.schemas.credit_card import CreditCardSchema

logger = get_logger(__name__)


class CreditCardController:
    @staticmethod
    @db_session
    async def create_card(session, card: CreditCardSchema):
        try:
            card = CreditCard(**card.dict())
            session.add(card)
            await session.commit()
            return card
        except Exception as e:
            logger.error(f"Error while creating user: {e}")
            await session.rollback()



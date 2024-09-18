from src.core.logger import get_logger
from src.db.db_session import db_session
from src.db.models import Address
from src.schemas.addresses import AddressSchema
logger = get_logger(__name__)


class AddressController:
    @staticmethod
    @db_session
    async def create_address(session, address: AddressSchema):
        try:
            address = Address(**address.dict())
            session.add(address)
            await session.commit()
            return address
        except Exception as e:
            logger.error(f"Error while creating address: {e}")
            await session.rollback()



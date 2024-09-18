from fastapi import APIRouter

from src.api.v1.endpoints import users
from src.api.v1.endpoints import addresses
from src.api.v1.endpoints import credit_cards

router = APIRouter()

router.include_router(users.router, tags=["Users"], prefix="/users")
router.include_router(addresses.router, tags=["Addresses"], prefix="/addresses")
router.include_router(credit_cards.router, tags=["Credit cards"], prefix="/credit_cards")

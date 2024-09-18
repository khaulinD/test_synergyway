from pydantic import BaseModel

from src.schemas.addresses import AddressSchema
from src.schemas.credit_card import CreditCardSchema


class UserCreateSchema(BaseModel):
    name: str
    email: str


class UserSchema(BaseModel):
    name: str
    email: str
    address: AddressSchema
    credit_card: CreditCardSchema

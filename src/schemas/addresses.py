from pydantic import BaseModel


class AddressSchema(BaseModel):
    street: str
    city: str
    country: str
    user_id: int
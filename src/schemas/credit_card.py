from pydantic import BaseModel


class CreditCardSchema(BaseModel):
    number: str
    expiration_date: str
    user_id: int

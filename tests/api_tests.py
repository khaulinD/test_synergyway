import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers.addresses import AddressController
from src.controllers.credit_card import CreditCardController
from src.controllers.users import UserController
from src.schemas.addresses import AddressSchema
from src.schemas.credit_card import CreditCardSchema
from src.schemas.users import UserCreateSchema
from src.db.models import User, Address, CreditCard
from fastapi import HTTPException


@pytest.fixture
def mock_session():
    session = MagicMock(spec=AsyncSession)
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.add = AsyncMock()
    session.execute = AsyncMock()
    return session


@pytest.mark.asyncio
async def test_create_user(mock_session):
    user_data = UserCreateSchema(id=1, name='John Doe', email='john@example.com')
    mock_user = User(id=1, name='John Doe', email='john@example.com')

    mock_session.add = AsyncMock()
    mock_session.commit = AsyncMock()

    user = await UserController.create_user(session=mock_session, user=user_data)

    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()

@pytest.mark.asyncio
async def test_get_user_found(mock_session):
    user_id = 1
    mock_user = User(id=user_id, name='John Doe', email='john@example.com')

    # Set up the mock to return a result with the expected user
    mock_result = MagicMock()
    mock_result.scalar = AsyncMock(return_value=mock_user)
    mock_session.execute = AsyncMock(return_value=mock_result)

    user = await UserController.get_user(session=mock_session, user_id=user_id)
    assert user == mock_user


@pytest.mark.asyncio
async def test_get_user_not_found(mock_session):
    user_id = 0

    # Set up the mock to return no user
    mock_result = MagicMock()
    mock_result.scalar = AsyncMock(return_value=None)
    mock_session.execute = AsyncMock(return_value=mock_result)

    # Ensure the HTTPException is raised as expected
    with pytest.raises(HTTPException) as excinfo:
        await UserController.get_user(session=mock_session, user_id=user_id)

    # Check the exception details
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "User not found"



@pytest.mark.asyncio
async def test_create_address(mock_session):
    address_data = AddressSchema(city='Anytown', street='123 Main St', country='USA', user_id=1)
    address = await AddressController.create_address(session=mock_session, address=address_data)

    mock_session.add.assert_called_once()
    assert isinstance(address, Address)
    assert address.city == 'Anytown'
    assert address.street == '123 Main St'
    assert address.country == 'USA'
    assert address.user_id == 1
    mock_session.commit.assert_called_once()


@pytest.mark.asyncio
async def test_create_card(mock_session):
    card_data = CreditCardSchema(number='1234567890123456', expiration_date='12/25', user_id=1)
    card = await CreditCardController.create_card(session=mock_session, card=card_data)

    mock_session.add.assert_called_once()
    assert isinstance(card, CreditCard)
    assert card.number == '1234567890123456'
    assert card.expiration_date == '12/25'
    assert card.user_id == 1
    mock_session.commit.assert_called_once()


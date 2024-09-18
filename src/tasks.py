import asyncio
import json
import logging
import random

import requests
from celery import Celery

from src.controllers.addresses import AddressController
from src.controllers.credit_card import CreditCardController
from src.controllers.users import UserController
from src.db.models import users, addresses, credit_card
from src.api.dependencies.utils import async_get
from src.core.settings import settings
from src.schemas.addresses import AddressSchema
from src.schemas.credit_card import CreditCardSchema
from src.schemas.users import UserCreateSchema

celery = Celery('tasks', broker='redis://localhost:6379')


def run_async(func, *args, **kwargs):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(func(*args, **kwargs))

@celery.task(name='fetch_users')
def fetch_users():
    run_async(fetch_and_store_users_controller)


@celery.task(name='fetch_cards')
def fetch_cards():
    run_async(fetch_and_store_card_controller)


@celery.task(name='fetch_address')
def fetch_address():
    run_async(fetch_and_store_address_controller)



async def fetch_and_store_users_controller():
    user_info = await async_get(settings.user_info_url)
    logging.info(f'Fetching users from {user_info}')
    # Make sure we generate a list of tasks, not a generator
    tasks = [UserController.create_user(UserCreateSchema(**info)) for info in user_info]

    # Run all the tasks concurrently
    await asyncio.gather(*tasks, return_exceptions=True)


async def fetch_and_store_address_controller():
    user_address = await async_get(settings.user_address_url)
    logging.info(f'Fetching address from {user_address}')

    transformed_info = [
        {
            "city": info["city"],
            "street": info["street_name"],
            "country": info["country"],
            "user_id": random.randint(1, 10)
        }
        for info in [user_address]
    ]

    tasks = [AddressController.create_address(AddressSchema(**info)) for info in transformed_info]

    # Run all the tasks concurrently
    await asyncio.gather(*tasks, return_exceptions=True)


async def fetch_and_store_card_controller():
    card_info = await async_get(settings.credit_card_url)
    logging.info(f'Fetching card from {card_info}')
    transformed_info = [
        {
            "number": info["credit_card_number"],
            "expiration_date": info["credit_card_expiry_date"],
            "user_id": random.randint(1, 10)
        }
        for info in [card_info]
    ]
    # Make sure we generate a list of tasks, not a generator
    tasks = [CreditCardController.create_card(CreditCardSchema(**info)) for info in transformed_info]

    # Run all the tasks concurrently
    await asyncio.gather(*tasks, return_exceptions=True)

import os
import re
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from .logger import get_logger

logger = get_logger(__name__)

load_dotenv()

BASE_DIR = Path(__file__).parent.parent


class DbSettings(BaseModel):
    """Database settings from environment variables."""
    DB_USER: str = os.getenv("POSTGRES_USER", "postgres")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", 'password')
    DB_HOST: str = os.getenv("POSTGRES_HOST", 'db')
    DB_PORT: int = os.getenv("POSTGRES_PORT", 5432)
    DB_NAME: str = os.getenv("POSTGRES_DB", 'dbname')
    url: str = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    echo: bool = False


class RedisSettings(BaseModel):
    redis_url: str = os.getenv("REDIS_URL", 'redis://redis:6379/0')




class Settings(BaseSettings):
    """Aggregated application settings."""
    redis: RedisSettings = RedisSettings()
    db: DbSettings = DbSettings()
    user_info_url: str = "https://jsonplaceholder.typicode.com/users"
    user_address_url: str = 'https://random-data-api.com/api/v2/addresses'
    credit_card_url: str = 'https://random-data-api.com/api/v2/credit_cards'



settings = Settings()
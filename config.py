import os

from dotenv import load_dotenv
from pydantic import BaseSettings
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(env_path)


class Settings(BaseSettings):
    DATABASE_NAME: str = os.environ.get('db_name')
    DATABASE_USER: str = os.environ.get('db_user')
    DATABASE_PASSWORD: str = os.environ.get('db_password')
    DATABASE_PORT: str = os.environ.get(str('db_port'))
    DATABASE_HOST: str = os.environ.get('db_host')
    DATABASE_URL: str = f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/' \
                        f'{DATABASE_NAME}'

    class Config:
        env_file = '.env'


settings = Settings()

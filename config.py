import os

from dotenv import load_dotenv
from pydantic import BaseSettings
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(env_path)


class Settings(BaseSettings):
    DATABASE_NAME: str = os.getenv('db_name')
    DATABASE_USER: str = os.getenv('db_user')
    DATABASE_PASSWORD: str = os.getenv('db_password')
    DATABASE_PORT: str = os.getenv(str('db_port'))
    DATABASE_HOST: str = os.getenv('db_host')
    DATABASE_URL: str = f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/' \
                        f'{DATABASE_NAME}'.format(DATABASE_USER=DATABASE_USER, DATABASE_PASSWORD=DATABASE_PASSWORD,
                                                  DATABASE_HOST=DATABASE_HOST, DATABASE_PORT=DATABASE_PORT,
                                                  DATABASE_NAME=DATABASE_NAME)

    class Config:
        env_file = '.env'


settings = Settings()

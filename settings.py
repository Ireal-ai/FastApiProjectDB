import os
from pydantic import BaseSettings

from sqlalchemy import create_engine


class Settings(BaseSettings):
    DATABASE_NAME: str = os.getenv('db_name')
    DATABASE_USER: str = os.getenv('db_user')
    DATABASE_PASSWORD: str = os.getenv('db_password')
    DATABASE_PORT: str = os.getenv(str('db_port'))
    DATABASE_HOST: str = os.getenv('db_host')
    DATABASE_URL: str = create_engine(f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:'
                                      f'{DATABASE_PORT}/{DATABASE_NAME}')

    class Config:
        env_file = '.env'

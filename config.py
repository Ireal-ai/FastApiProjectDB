import os

from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn, validator
from pydantic.tools import lru_cache
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(env_path)


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: str
    DB_HOST: str

    DB_URL: PostgresDsn

    @validator('DB_URL')
    def connection_db(cls, db_url: PostgresDsn, values: dict[str:str, ...]):
        db_name: str = values.get('DB_NAME')
        db_user: str = values.get('DB_USER')
        db_password: str = values.get('DB_PASSWORD')
        db_port: str = values.get('DB_PORT')
        db_host: str = values.get('DB_HOST')

        db_url: str = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

        return db_url

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_setting():
    return Settings()


settings = get_setting()

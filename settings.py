import os

from sqlalchemy import create_engine

DATABASE_NAME = os.getenv('db_name')
DATABASE_USER = os.getenv('db_user')
DATABASE_PASSWORD = os.getenv('db_password')
DATABASE_PORT = os.getenv('db_port')
DATABASE_HOST = os.getenv('db_host')

DATABASE_URL = create_engine(f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:'
                             f'{DATABASE_PORT}/{DATABASE_NAME}')

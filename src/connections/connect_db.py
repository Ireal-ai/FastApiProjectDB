import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from config import settings

Base = declarative_base()


class BaseConnect:

    def __init__(self):
        self.engine = create_engine(settings.DATABASE_URL)

    def get_session(self):
        return sessionmaker(self.engine)

import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from config import settings


class BaseConnect:

    def __init__(self):
        self.engine = create_engine(settings.DATABASE_URL)
        self.Base = declarative_base()

    def get_session(self):
        return sessionmaker(self.engine)


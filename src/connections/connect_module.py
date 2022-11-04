import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy.orm import declarative_base, sessionmaker

import os

from settings import DATABASE_URL

engine = DATABASE_URL
Session = sessionmaker(engine)
Base = declarative_base()


def create_database():
    Base.metadata.create_all(engine)

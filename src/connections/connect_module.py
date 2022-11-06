import psycopg2
from psycopg2 import Error
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from settings import Settings

settings = Settings()

engine = settings.DATABASE_URL
Session = sessionmaker(engine)
Base = declarative_base()


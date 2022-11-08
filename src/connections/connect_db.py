import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from config import settings

engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(engine)
Base = declarative_base()

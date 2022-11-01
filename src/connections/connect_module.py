import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy.orm import declarative_base, sessionmaker
import os

engine = create_engine('postgresql+psycopg2://postgres:postgres@8080/postgres', echo=True)
Session = sessionmaker(engine)
Base = declarative_base()


def create_database():
    Base.metadata.create_all(engine)

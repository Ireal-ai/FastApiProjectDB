from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings

Base = declarative_base()
engine = create_engine(settings.DB_URL)
session = sessionmaker(engine)

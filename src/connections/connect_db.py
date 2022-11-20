from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, Session
from config import settings


engine = create_engine(settings.DB_URL)
Base = declarative_base(engine)
metadata = MetaData(engine)
metadata.drop_all()


def get_session():
    return Session(engine)

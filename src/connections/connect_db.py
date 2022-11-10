from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings

Base = declarative_base()


class BaseConnect:

    def __init__(self):
        self.engine = create_engine(settings.DATABASE_URL)

    def get_session(self):
        return sessionmaker(self.engine)

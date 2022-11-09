from sqlalchemy import Integer, String, Column, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from src.connections.connect_db import Base


class DocumentsModel(Base):
    __tablename__ = 'documents'

    id = Column('id', Integer, primary_key=True, autoincrement=True),
    right = relationship('RightsModel', back_populates='document')
    name = Column('name', String),
    text = Column('text', String),
    inserted_at = Column('inserted_at', TIMESTAMP),
    updated_at = Column('updated_at', TIMESTAMP)


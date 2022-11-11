from sqlalchemy import Integer, String, Column, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from src.connections.connect_db import Base


class RightsModel(Base):
    __tablename__ = 'rights'

    id = Column('id', Integer, primary_key=True, autoincrement=True),
    document_id = Column('document_id', Integer, ForeignKey('documents.id')),
    name = Column('name', String),
    text = Column('text', String),
    rights_from = Column('right_from', TIMESTAMP),
    rights_to = Column('rights_to', TIMESTAMP),
    inserted_at = Column('inserted_at', TIMESTAMP),
    updated_at = Column('updated_at', TIMESTAMP)
    document = relationship("DocumentsModel", back_populates='right')

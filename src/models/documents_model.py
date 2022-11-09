from sqlalchemy import Integer, String, Column, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from src.connections.connect_db import BaseConnect


class DocumentsModel(BaseConnect):
    __tablename__ = 'documents'

    id = Column('id', Integer, primary_key=True, autoincrement=True),
    right = relationship('RightsModel', back_populates='document')
    name = Column('name', String),
    text = Column('text', String),
    inserted_at = Column('inserted_at', TIMESTAMP),
    updated_at = Column('updated_at', TIMESTAMP)


class RightsModel(BaseConnect):
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

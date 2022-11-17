from sqlalchemy import Integer, String, Column, TIMESTAMP
from sqlalchemy.orm import relationship
from src.connections.connect_db import Base


class DocumentsModel(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, autoincrement=True)
    right = relationship('RightsModel', back_populates='document')
    name = Column(String)
    text = Column(String)
    inserted_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


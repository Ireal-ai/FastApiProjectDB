from sqlalchemy import Integer, String, Column, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from src.connections.connect_db import Base


class RightsModel(Base):
    __tablename__ = 'rights'

    id = Column(Integer, primary_key=True, autoincrement=True)
    document_id = Column(Integer, ForeignKey('documents.id'))
    name = Column(String)
    text = Column(String)
    rights_from = Column(TIMESTAMP)
    rights_to = Column(TIMESTAMP)
    inserted_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    document = relationship("DocumentsModel", back_populates='right')

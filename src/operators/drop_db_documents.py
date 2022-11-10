from src.connections import base_connect
from src.models.documents_model import DocumentsModel


class DropDocumentsTable:
    def __init__(self):
        self.document_model = DocumentsModel.__table__

    def processing(self):
        self.document_model.drop()

    def execute(self):
        self.pg_session = base_connect.get_session()
        try:
            self.processing()
            self.pg_session.commit()
        except Exception as error:
            raise error
        finally:
            self.pg_session.close()


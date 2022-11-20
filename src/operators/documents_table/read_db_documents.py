from src.connections import get_session
from src.models.documents_model import DocumentsModel


class ReadDocumentTable:
    def __init__(self):
        self.document_model = DocumentsModel.__table__

    def processing(self):
        self.document_model.select()

    def execute(self):
        self.pg_session = get_session()
        try:
            self.processing()
            self.pg_session.commit()
        except Exception as error:
            raise error
        finally:
            self.pg_session.close()

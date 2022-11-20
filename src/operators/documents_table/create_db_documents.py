from src.connections import get_session
from src.models.documents_model import DocumentsModel


class CreateDocumentTable:
    def __init__(self):
        self.documents_model = DocumentsModel.__table__

    def processing(self):
        self.documents_model.create()

    def execute(self):
        self.pg_session = get_session()
        try:
            self.processing()
            self.pg_session.commit()
        except Exception as error:
            raise error
        finally:
            self.pg_session.close()






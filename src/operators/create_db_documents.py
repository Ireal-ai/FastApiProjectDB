from src.connections import base_connect
from src.models.documents_model import DocumentsModel


class CreateDb:
    def __init__(self):
        self.documents_model = DocumentsModel.__table__

    def processing(self):
        self.documents_model.create()

    def execute(self):
        self.pg_session = base_connect.get_session()
        try:
            self.processing()
            self.pg_session.commit()
            pass
        except Exception as error:
            return error
        finally:

            self.pg_session.close()



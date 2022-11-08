from sqlalchemy import select, insert, update, delete

from src.connections import base_connect
from src.models import DocumentsModel


class CreateDb:
    def __init__(self):
        self.documents_model = DocumentsModel.__table__

    def execute(self):
        self.pg_session = base_connect.get_session()
        try:
            # processing()
            pass
        except Exception as error:
            return error
        finally:
            self.pg_session.close()

    def processing(self):
        self.documents_model.create()

from src.models.documents_model import DocumentsModel
from src.operators.execute_request import Execute_requests


class ReadDocumentTable(Execute_requests):
    def __init__(self):
        self.document_model = DocumentsModel.__table__

    def processing(self):
        self.document_model.select()





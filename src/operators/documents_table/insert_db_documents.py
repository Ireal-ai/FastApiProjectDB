from src.operators.execute_request import Execute_requests
from src.models.documents_model import DocumentsModel


class InsertDocumentTable(Execute_requests):
    def __init__(self):
        self.document_model = DocumentsModel.__table__

    def processing(self):
        self.document_model.insert()

    def execute(self):
        return super(InsertDocumentTable, self).execute()

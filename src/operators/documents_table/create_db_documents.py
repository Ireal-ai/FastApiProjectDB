from src.operators.execute_request import Execute_requests
from src.models.documents_model import DocumentsModel


class CreateDocumentTable(Execute_requests):
    def __init__(self):
        self.documents_model = DocumentsModel.__table__

    def processing(self):
        self.documents_model.create()

    def execute(self):
        return super(CreateDocumentTable, self).execute()





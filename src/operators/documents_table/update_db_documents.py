from src.operators.execute_request import Execute_requests
from src.models.documents_model import DocumentsModel


class UpdateDocumentsTable(Execute_requests):
    def __init__(self):
        self.documents_model = DocumentsModel.__table__

    def processing(self):
        self.documents_model.update()

    def execute(self):
        return super(UpdateDocumentsTable, self).execute()


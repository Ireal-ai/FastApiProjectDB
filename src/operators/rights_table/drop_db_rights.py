from src.operators.execute_request import Execute_requests
from src.models.rights_model import RightsModel


class DropRightsTable(Execute_requests):
    def __init__(self):
        self.rights_model = RightsModel.__table__

    def processing(self):
        self.rights_model.drop()

    def execute(self):
        return super(DropRightsTable, self).execute()
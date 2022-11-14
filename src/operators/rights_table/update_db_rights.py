from src.operators.execute_request import Execute_requests
from src.models.rights_model import RightsModel


class UpdateRightsTable(Execute_requests):
    def __init__(self):
        self.rights_model = RightsModel.__table__

    def processing(self):
        self.rights_model.update()

    def execute(self):
        return super(UpdateRightsTable, self).execute()

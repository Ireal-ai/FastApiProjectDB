from src.models.rights_model import RightsModel
from src.operators.execute_request import Execute_requests


class ReadRightsTable(Execute_requests):
    def __init__(self):
        self.rights_model = RightsModel.__table__

    def processing(self):
        self.rights_model.select()

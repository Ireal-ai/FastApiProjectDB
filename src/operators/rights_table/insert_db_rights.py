from src.operators.execute_request import Execute_requests
from src.models.rights_model import RightsModel


class InsertRightModel(Execute_requests):
    def __init__(self):
        self.right_model = RightsModel.__table__

    def processing(self):
        self.right_model.insert()




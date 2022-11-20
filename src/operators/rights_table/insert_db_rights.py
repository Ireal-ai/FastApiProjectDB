from src.connections import get_session
from src.models.rights_model import RightsModel


class InsertRightModel:
    def __init__(self):
        self.right_model = RightsModel.__table__

    def processing(self):
        self.right_model.insert()

    def execute(self):
        self.pg_session = get_session()
        try:
            self.processing()
            self.pg_session.commit()
        except Exception as error:
            raise error
        finally:
            self.pg_session.close()



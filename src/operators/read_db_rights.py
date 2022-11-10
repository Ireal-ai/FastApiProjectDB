from src.models.rights_model import RightsModel
from src.connections import base_connect


class ReadRightsModel:
    def __init__(self):
        self.rights_model = RightsModel()

    def processing(self):
        self.rights_model.select()

    def execute(self):
        self.pg_session = base_connect.get_session()
        try:
            self.processing()
            self.pg_session.commit()
        except Exception as error:
            return error
        finally:
            self.pg_session.close()
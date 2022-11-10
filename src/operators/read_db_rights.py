from src.models.rights_model import RightsModel
from src.connections import base_connect


class ReadRightsTable:
    def __init__(self):
        self.rights_model = RightsModel.__table__

    def processing(self):
        self.rights_model.select()

    def execute(self):
        self.pg_session = base_connect.get_session()
        try:
            self.processing()
            self.pg_session.commit()
        except Exception as error:
            raise error
        finally:
            self.pg_session.close()
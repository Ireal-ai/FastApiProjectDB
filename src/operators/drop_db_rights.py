from src.connections import base_connect
from src.models.rights_model import RightsModel


class DropRightsTable:
    def __init__(self):
        self.rights_model = RightsModel.__tablename__

    def processing(self):
        self.rights_model.drop()

    def execute(self):
        self.pg_session = base_connect.get_session()
        try:
            self.processing()
            self.pg_session.commit()
        except Exception as error:
            raise error
        finally:
            self.pg_session.close()
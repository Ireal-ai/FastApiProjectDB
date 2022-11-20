from abc import abstractmethod, ABC

from src.connections import base_connect


class Execute_requests(ABC):

    @abstractmethod
    def processing(self):
        ...

    def execute(self):
        self.pg_session = base_connect.get_session()
        try:
            self.processing()
            self.pg_session.commit()
        except Exception as error:
            raise error
        finally:
            self.pg_session.close()

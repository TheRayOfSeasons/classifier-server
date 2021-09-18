from pypika import Query
from pypika import Table

from database import DATABASE_CONNECTION


SERVICES = {}


class Service:
    """
    """

    table = None
    table_name = ''

    def __init__(self):
        SERVICES[self.__class__.__name__] = self
        self.table = Table(self.table_name)

    def retrieve_values(self, query=None, *args) -> List:
        """
        A virtual method for reading values from the database.
        """
        if not query:
            query = Query.from_(self.table).select(*args)
        data = DATABASE_CONNECTION.run_query(query)
        return data

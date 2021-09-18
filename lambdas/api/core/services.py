from pypika import Field
from pypika import Query
from pypika import Table

from database import DATABASE_CONNECTION


class Service:
    """
    """

    main_table = ''

    def retrieve_values(self, fields: List):
        """
        A virtual method for reading values from the database.
        """
        query = Query.from_(self.main_table).select(*fields)
        data = DATABASE_CONNECTION.run_query(query)
        return data

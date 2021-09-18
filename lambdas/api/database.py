import os

import psycopg2
from pypika.queries import QueryBuilder

from .settings import DATABASE


class DatabaseConnection:
    """
    Submit all queries to the database.
    """

    connection = None
    cursor = None

    def open(self):
        self.connection = psycopg2.connect(
            user=DATABASE['USER'],
            password=DATABASE['PASSWORD'],
            host=DATABASE['HOST'],
            port=DATABASE['PORT'],
            database=DATABASE['NAME']
        )
        self.cursor = connection.cursor()

    def run_query(self, query: QueryBuilder):
        """
        Runs a query from graphene.
        """
        stringified_query = str(query)
        if self.cursor:
            data = self.cursor.execute(stringified_query)
        else:
            raise Exception('Database connection is not yet open.')
        return data

    def close(self) -> None:
        """
        Close the entire connection to the database.
        """
        if not self.cursor or not self.connection:
            raise Exception('Database connection is not yet open.')
        self.cursor.close()
        self.connection.close()


DATABASE_CONNECTION = DatabaseConnection()

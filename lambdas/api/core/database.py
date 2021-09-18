import os

import psycopg2
from pypika.functions import Function
from pypika.queries import QueryBuilder

from .settings import DATABASE


class ST_AsText(Function):
    """
    Converts raw point field values from hexcode
    to human readable coordinates.
    """

    def __init__(self, term):
        super(ST_AsText, self).__init__('ST_AsText', term)


class DatabaseConnection:
    """
    Submit all queries to the database.
    """

    connection = None
    cursor = None

    def open(self):
        """
        Opens the connections.
        """
        self.connection = psycopg2.connect(
            user=DATABASE['USER'],
            password=DATABASE['PASSWORD'],
            host=DATABASE['HOST'],
            port=DATABASE['PORT'],
            database=DATABASE['NAME']
        )
        self.cursor = self.connection.cursor()

    def rollback(self):
        """
        Rolls back the previous query.
        """
        if not self.cursor:
            raise Exception('Database connection is not yet open.')
        self.cursor.execute('ROLLBACK')

    def run_query(self, query: QueryBuilder):
        """
        Runs a query from pypika.
        """
        stringified_query = str(query)
        if self.cursor:
            try:
                self.cursor.execute(stringified_query)
            except Exception:
                self.cursor.execute('ROLLBACK')
            data = self.cursor.fetchall()
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

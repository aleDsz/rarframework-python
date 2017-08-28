import pyodbc

from data_context_factory import DataContextFactory
from rarframework.rar_framework_exception import RarFrameworkException


class DataContext:
    database_connection = None
    database_name = None

    def __init__(self, database_name = None):
        self.database_name = database_name
        self.connect(self)

    def connect(self):
        try:
            self.database_connection = DataContextFactory.get_connection(self.database_name)
        except:
            RarFrameworkException.log_error()

    def disconnect(self):
        try:
            if (self.database_connection != None):
                self.database_connection.close()
        except:
            RarFrameworkException.log_error()

    def begin(self):
        try:
            if (self.database_connection != None):
                self.connect()

            self.database_connection.begin()
        except:
            RarFrameworkException.log_error()

    def commit(self):
        try:
            if (self.database_connection != None):
                self.database_connection.commit()
        except:
            RarFrameworkException.log_error()

    def rollback(self):
        try:
            if (self.database_connection != None):
                self.database_connection.rollback()
        except:
            RarFrameworkException.log_error()

    def execute_reader(self, string_sql):
        try:
            if (self.database_connection != None):
                self.connect()

            cursor = self.database_connection.cursor()
            result_set = cursor.execute(string_sql).fetchall()
            cursor.close()

            return result_set
        except:
            RarFrameworkException.log_error()

    def execute_query(self, string_sql):
        try:
            if (self.database_connection != None):
                self.connect()

            cursor = self.database_connection.cursor()
            cursor.execute(string_sql)
            cursor.close()
        except:
            RarFrameworkException.log_error()
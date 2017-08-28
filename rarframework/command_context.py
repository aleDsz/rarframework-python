from database_factory import DatabaseFactory
from rar_framework_exception import RarFrameworkException


class CommandContext:
    command = None
    data_context = None

    def __init__(self, string_sql = None, database_name = None):
        self.set_sql(string_sql)
        self.data_context = DatabaseFactory.get_instance_of_data_context(database_name)

    def set_sql(self, string_sql):
        self.command = string_sql

    def execute_query(self):
        try:
            self.data_context.execute_query(self.command)
        except:
            RarFrameworkException.log_error()

    def execute_reader(self):
        try:
            self.data_context.execute_reader(self.command)
        except:
            RarFrameworkException.log_error()
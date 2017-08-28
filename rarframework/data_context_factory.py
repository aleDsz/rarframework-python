import json, os, pyodbc


class DataContextFactory:
    config_data = None

    @staticmethod
    def get_config():
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "databaseConfig.json")

        with open(config_file, "r") as config_data:
            DataContextFactory.config_data = json.loads(config_data)

    @staticmethod
    def get_connection(database_name):
        if (DataContextFactory.config_data == None):
            DataContextFactory.get_config()

        if (DataContextFactory.config_data != None):
            if (database_name != None):
                connection_string = DataContextFactory.config_data[database_name]
            else:
                connection_string = DataContextFactory.config_data[0]

            database_connection = pyodbc.connect(connection_string)

        return database_connection
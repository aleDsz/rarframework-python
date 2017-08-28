import json


class DataContextFactory:
    config_data = None

    @staticmethod
    def get_config():
        with open('databaseConfig.json') as config_data:
            DataContextFactory.config_data = json.loads(config_data)

    @staticmethod
    def get_connection(databaseName):
        if (DataContextFactory.config_data == None):
            DataContextFactory.get_config()

        return DataContextFactory.config_data

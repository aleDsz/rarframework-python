from rarframework import DataContext

class DatabaseFactory:
    _instance_of_data_context = None

    @staticmethod
    def get_instance_of_data_context(database_name):
        if (DatabaseFactory._instance_of_data_context == None):
            DatabaseFactory._instance_of_data_context = DataContext(database_name)

        return DatabaseFactory._instance_of_data_context
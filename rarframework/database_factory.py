from rarframework import DataContext

class DatabaseFactory:
    _instance_of_data_context = None

    def get_instance_of_data_context():
        if (DatabaseFactory._instance_of_data_context == None):
            DatabaseFactory._instance_of_data_context = DataContext()

        return DatabaseFactory._instance_of_data_context

    def get_instance_of_data_context(databaseName):
        if (DatabaseFactory._instance_of_data_context == None):
            DatabaseFactory._instance_of_data_context = DataContext(databaseName)

        return DatabaseFactory._instance_of_data_context
from rarframework import DataContextFactory

class DataContext:
    databaseConnection = None
    databaseName = None

    def __init__(self, databaseName = None):
        self.databaseName = databaseName
        self.connect(self)

    def connect(self):
        try:
            self.databaseConnection = DataContextFactory.get_connection(self.databaseName)
        except Exception:
            print "Oops!"
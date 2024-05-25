from pymongo import MongoClient
import GlobalConstants


class DatabaseConnector:
    client = None

    def __init__(self):
        self.initialize(GlobalConstants.MONGODB_CONNECTION_STRING, GlobalConstants.MONGODB_MAX_POOL_SIZE)

    def initialize(self, mongo_uri, max_pool_size=10):
        self.client = MongoClient(mongo_uri, maxPoolSize=max_pool_size)

    def getClient(self):
        if self.client is None:
            raise RuntimeError("DatabaseConnector is not initialized. Call initialize() first.")
        return self.client

    def getDatabase(self, database_name):
        return self.client[database_name]

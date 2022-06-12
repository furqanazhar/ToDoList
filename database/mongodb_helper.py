from pymongo import MongoClient


class Database:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.database = self.client['ToDoNotes']

    async def insert_document(self, collection, data):
        return self.database[collection].insert_one(data).acknowledged

    async def update_document_by_id(self, collection, data):
        return self.database[collection].update_one(data).acknowledged

    async def update_document_by_attribute(self, collection, data):
        return self.database[collection].update(data).acknowledged

    async def delete_document_by_id(self, collection, data):
        return self.database[collection].delete_one(data).acknowledged

    async def delete_document_by_attribute(self, collection, data):
        return self.database[collection].delete_many(data).acknowledged

    async def get_document_by_id(self, collection, data):
        return self.database[collection].find_one(data)

    async def get_document_by_attribute(self, collection, data):
        return self.database[collection].find(data)

    async def get_all_documents(self, collection, data):
        return self.database[collection].find(data)
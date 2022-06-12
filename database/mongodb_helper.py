from bson import ObjectId
from pymongo import MongoClient


class Database:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.database = self.client['ToDoNotes']

    async def insert_document(self, collection, data):
        _id = self.database[collection].insert(data)
        return self.database[collection].find_one({'_id': _id}, {'_id': False})

    async def update_document_by_id(self, collection, data):
        return self.database[collection].update_one(data).acknowledged

    async def update_document_by_attribute(self, collection, data):
        return self.database[collection].update(data).acknowledged

    async def delete_document_by_id(self, collection, _id):
        return self.database[collection].delete_one({'_id': ObjectId(_id)}).acknowledged

    async def delete_document_by_attribute(self, collection, data):
        return self.database[collection].delete_many(data).acknowledged

    async def get_document_by_id(self, collection, _id):
        return list(self.database[collection].find({'_id': ObjectId(_id)}, {'_id': 0}))

    async def get_document_by_attribute(self, collection, key, value):
        return list(self.database[collection].find({key: value}, {'_id': 0}))

    async def get_all_documents(self, collection):
        return list(self.database[collection].find({}, {'_id': 0}))

from bson import ObjectId
from pymongo import MongoClient


class Database:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.database = self.client['ToDoNotes']

    async def insert_document(self, collection, data):
        _id = self.database[collection].insert_one(data)
        return self.database[collection].find_one({'_id': _id.inserted_id}, {'_id': False})

    async def update_document_by_id(self, collection, _id, data):
        return self.database[collection].update_one({'_id': ObjectId(_id)}, {'$set': data}).acknowledged

    async def update_document_by_attribute(self, collection, key, old_value, updated_value):
        return self.database[collection].update_many({key: old_value}, {'$set': {key: updated_value}}).modified_count

    async def delete_document_by_id(self, collection, _id):
        return self.database[collection].delete_one({'_id': ObjectId(_id)}).acknowledged

    async def delete_document_by_attribute(self, collection, key, value):
        return self.database[collection].delete_many({key: value}).deleted_count

    async def delete_all_documents(self, collection):
        return self.database[collection].delete_many({}).deleted_count

    async def get_document_by_id(self, collection, _id):
        return list(self.database[collection].find({'_id': ObjectId(_id)}, {'_id': 0}))

    async def get_document_by_attribute(self, collection, key, value):
        return list(self.database[collection].find({key: value}, {'_id': 0}))

    async def get_all_documents(self, collection):
        return list(self.database[collection].find({}, {'_id': 0}))

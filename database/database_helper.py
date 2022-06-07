import pymongo


class Database:

    async def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        self.database = client.ToDoNotes
        self.collection = self.database.Notes

    async def insert_document(self, data):
        pass

    async def update_document_by_id(self, data):
        pass

    async def update_document_by_attribute(self, data):
        pass

    async def delete_document_by_id(self, data):
        pass

    async def delete_document_by_attribute(self, data):
        pass

    async def get_document_by_id(self, data):
        pass

    async def get_document_by_attribute(self, data):
        pass

    async def get_all_documents(self, data):
        pass
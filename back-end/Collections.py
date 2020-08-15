from db_login.QuanteSecrets import get_login
from bson.objectid import ObjectId
from Objects import *
import pymongo as mg

class CollectionBase():
    def __init__(self, collection_name):
        login, password = get_login()
        self.mongo_url = f"mongodb+srv://quante:{password}@db-quante.dni24.gcp.mongodb.net/{login}?retryWrites=true&w=majority"
        self.collection_name = collection_name

    def post(self, obj):
        obj.pop('_id', None)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            ret = collection.insert_one(obj)
            obj["_id"] = ObjectId(ret.inserted_id)
            return obj

    def get(self, _id):
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            obj = collection.find_one({"_id" : ObjectId(_id)})
            return obj

    def put(self, obj):
        _id = obj.pop('_id', None)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            ret = collection.update_one({"_id" : ObjectId(_id)}, {"$set": obj}, upsert=True)
            obj["_id"] = ret.upserted_id if ret.upserted_id != None else _id
            return obj

    def delete(self, _id):
        obj = self.get(_id)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            ret = collection.delete_one({"_id" : ObjectId(_id)})
            return obj
     
class ClientCollection(CollectionBase):
    def __init__(self):
        super().__init__(Client.__name__)
    
class CompanyCollection(CollectionBase):
    def __init__(self):
        super().__init__(Company.__name__)
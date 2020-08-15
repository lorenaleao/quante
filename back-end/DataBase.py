from cryptography.fernet import Fernet
from bson.objectid import ObjectId
from Objects import *

import pymongo as mg

class CollectionBase():
    def __init__(self, _type_):
        with open("db-login/key.bin", "r") as key, open("db-login/login-password.bin", "r") as login:
            fn = Fernet(key.read())
            encrypted = login.read()
            bin_msg = fn.decrypt(encrypted.encode()) 
            login_password = bin_msg.decode()
            login, password = login_password.split(";")
            self.mongo_url = f"mongodb+srv://quante:{password}@db-quante.dni24.gcp.mongodb.net/{login}?retryWrites=true&w=majority"
            self._type_ = _type_

    def post(self, obj):
        del obj["_id"] 
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self._type_.__name__]
            ret = collection.insert_one(obj)
            obj["_id"] = ObjectId(ret.inserted_id)
            return obj

    def get(self, _id):
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self._type_.__name__]
            obj = collection.find_one({"_id" : ObjectId(_id)})
            return obj

    def put(self, obj):
        _id = obj["_id"]
        del obj["_id"]
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self._type_.__name__]
            ret = collection.update_one({"_id" : ObjectId(_id)}, {"$set": obj}, upsert=True)
            obj["_id"] = ret.upserted_id if ret.upserted_id != None else _id
            return obj 

    def delete(self, _id):
        obj = self.get(_id)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self._type_.__name__]
            ret = collection.delete_one({"_id" : ObjectId(_id)})
            return obj 
        
class ClientCollection(CollectionBase):
    def __init__(self):
        super().__init__(Client)

class CompanyCollection(CollectionBase):
    def __init__(self):
        super().__init__(Company)

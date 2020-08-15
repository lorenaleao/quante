from cryptography.fernet import Fernet
from bson.objectid import ObjectId
import pymongo as mg

class Collection():
    def __init__(self, _type):
        with open("db-login/key.bin", "r") as key, open("db-login/login-password.bin", "r") as login:
            fn = Fernet(key.read())
            encrypted = login.read()
            bin_msg = fn.decrypt(encrypted.encode()) 
            login_password = bin_msg.decode()
            login, password = login_password.split(";")
            self.mongo_url = f"mongodb+srv://quante:{password}@db-quante.dni24.gcp.mongodb.net/{login}?retryWrites=true&w=majority"
            print(self.mongo_url)
            self._type = _type
            
    def add(self, obj):
        del obj["_id"] 
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self._type.__name__]
            ret = collection.insert_one(obj)
            obj["_id"] = ObjectId(ret.inserted_id)
            return obj
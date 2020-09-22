# Third party imports
from bson.objectid import ObjectId
import pymongo as mg
from collections import OrderedDict

# Local application imports
from secrets.QuanteSecrets import get_login
import Objects as orm

class CollectionBase():
    def __init__(self, _type_):
        login, password = get_login()
        self.mongo_url = "mongodb+srv://quante:" + password + "@db-quante.dni24.gcp.mongodb.net/" + login + "?retryWrites=true&w=majority"
        self.collection_name = _type_.__name__
        self.convert = _type_.convert

    def post(self, obj):
        obj = self.convert(obj).__dict__
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
        obj = self.convert(obj).__dict__
        _id = obj.pop('_id', None)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            ret = collection.update_one({"_id" : ObjectId(_id)}, {"$set": obj}, upsert = True)
            if ret.upserted_id == None:
                obj["_id"] = _id
            else:
                obj["_id"] = ret.upserted_id
            return obj

    def delete(self, _id):
        obj = self.get(_id)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            collection.delete_one({"_id" : ObjectId(_id)})
            return obj
     
     
class ClientCollection(CollectionBase):
    def __init__(self):
        super().__init__(orm.Client)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            try:
                db_mongo["db-quante"].create_collection(self.collection_name)
                print("Criando collection:", self.collection_name)
            except Exception:
                print("Coleção", self.collection_name, "já existe")
            
            vexpr = {
                "$jsonSchema": {
                    "bsonType": "object",
                    "required": [ "name", "email", "password"],
                    "properties": {
                        "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "age": {
                        "bsonType": "int",
                        "minimum": 0,
                        "maximum": 160,
                        "exclusiveMaximum": False,
                        "description": "must be an integer in [ 0, 160 ] and is not required"
                        },
                        "cpf": {
                        "bsonType": "string",
                        "description": "must be a string and is not required"
                        },
                        "email": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "password": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        }
                    }
                }
            }
            cmd = OrderedDict([('collMod', self.collection_name),
                    ('validator', vexpr),
                    ('validationLevel', 'moderate')])

            db_mongo["db-quante"].command(cmd)
     
    def email_already_registered(self, email):
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            obj = collection.find_one({"email" : email})
            return obj != None


class CompanyCollection(CollectionBase):
    def __init__(self):
        super().__init__(orm.Company)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            try:
                db_mongo["db-quante"].create_collection(self.collection_name)
                print("Criando collection:", self.collection_name)
            except Exception:
                print("Coleção", self.collection_name, "já existe")
            
            vexpr = {
                "$jsonSchema": {
                    "bsonType": "object",
                    "required": [ "name", "cnpj", "address", "email", "password" ],
                    "properties": {
                        "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "cnpj": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "address": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "email": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "password": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        }
                    }
                }
            }

            cmd = OrderedDict([('collMod', self.collection_name),
                    ('validator', vexpr),
                    ('validationLevel', 'moderate')])

            db_mongo["db-quante"].command(cmd)

    def email_already_registered(self, email):
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            obj = collection.find_one({"email" : email})
            return obj != None


class ProductCollection(CollectionBase):
    def __init__(self):
        super().__init__(orm.Product)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            try:
                db_mongo["db-quante"].create_collection(self.collection_name) 
                print("Criando collection:", self.collection_name)
            except Exception:
                print("Coleção", self.collection_name, "já existe")

            vexpr = {
                "$jsonSchema": {
                    "bsonType": "object",
                    "required": [ "name", "prices" ],
                    "properties": {
                        "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "image": {
                        "bsonType": "string",
                        "description": "must be a string and is not required"
                        },
                        "description": {
                        "bsonType": "string",
                        "description": "must be a string and is not required"
                        },
                        "spec": {
                        "bsonType": "object"
                        },
                        "categories": {
                        "bsonType": "array"
                        },
                        "prices": {
                        "bsonType": "object"
                        },
                        "price_history": {
                        "bsonType": "array"
                        },
                        "reviews": {
                        "bsonType": "array"
                        }
                    }
                }
            }

            cmd = OrderedDict([('collMod', self.collection_name),
                    ('validator', vexpr),
                    ('validationLevel', 'moderate')])

            db_mongo["db-quante"].command(cmd)


class ReviewCollection(CollectionBase):
    def __init__(self):
        super().__init__(orm.Review)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            try:
                db_mongo["db-quante"].create_collection(self.collection_name) 
                print("Criando collection:", self.collection_name)
            except Exception:
                print("Coleção", self.collection_name, "já existe")
            
            vexpr = {
                "$jsonSchema": {
                    "bsonType": "object",
                    "required": [ "product_id", "review_author", "review_rating", "review_text", "published_date", "is_recommended" ],
                    "properties": {
                        "product_id": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "review_author": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "review_rating": {
                        "bsonType": "double",
                        "description": "must be a double and is required"
                        },
                        "review_text": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "published_date": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "is_recommended": {
                        "bsonType": "bool",
                        "description": "must be a boolean and is required"
                        },
                        "likes": {
                        "bsonType": "int",
                        "description": "must be an integer and is not required"
                        }
                    }
                }
            }

            cmd = OrderedDict([('collMod', self.collection_name),
                    ('validator', vexpr),
                    ('validationLevel', 'moderate')])

            db_mongo["db-quante"].command(cmd)

    def post(self, obj):
        productCollection = ProductCollection()
        product = productCollection.get(obj["product_id"])
        obj = orm.Review.convert(obj).__dict__

        if len(product["relevant_reviews"]) < 10:
            product["relevant_reviews"].append(obj)

        productCollection.put(product)
        return super().post(obj)
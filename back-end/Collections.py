# Third party imports
from bson.objectid import ObjectId
import pymongo as mg
from collections import OrderedDict
import re

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
            return self.convert(obj)

    def get(self, _id):
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            obj = collection.find_one({"_id" : ObjectId(_id)})
            return self.convert(obj)

    def get_by_name(self, name: str):
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            obj = collection.find_one({"name" : name})
            return obj
    
    def get_by_substring(self, substr: str):
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            regx = re.compile(substr, re.IGNORECASE)
            obj = collection.find({"name": regx})
            return list(obj)

    def get_list(self):
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            objs_list = []
            for obj in collection.find():
                objs_list.append(obj)
            return objs_list

    def put(self, obj):
        obj = {k : v for k, v in self.convert(obj).__dict__.items() if v is not None}
        _id = obj.pop('_id', None)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            ret = collection.update_one({"_id" : ObjectId(_id)}, {"$set": obj}, upsert = True)
            if ret.upserted_id == None:
                obj["_id"] = _id
            else:
                obj["_id"] = ret.upserted_id
            return self.convert(obj)

    def delete(self, _id):
        obj = self.get(_id)
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            collection.delete_one({"_id" : ObjectId(_id)})
            return self.convert(obj)
     
     
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
                        },
                        "create_date": {
                        "bsonType": "string",
                        "description": "must be a string and is not required"
                        },
                        "perfil_img": {
                        "bsonType": "string",
                        "description": "must be a string and is not required"
                        }
                    }
                }
            }
            cmd = OrderedDict([('collMod', self.collection_name),
                    ('validator', vexpr),
                    ('validationLevel', 'moderate')])

            db_mongo["db-quante"].command(cmd)
     
    def get_by_email(self, email):
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            obj = collection.find_one({"email" : email})
            return self.convert(obj)


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
                        "bsonType": "object",
                        "required": [ "city", "state" ],
                        "properties": {
                            "street": {
                                "bsonType": "string",
                                "description": "must be a string if the field exists"
                            },
                            "number": {
                                "bsonType": "int",
                                "minimum": 0,
                                "description": "must be an integer if the field exists"
                            },
                            "neighborhood": {
                                "bsonType": "string",
                                "description": "must be a string if the field exists"
                            },
                            "city": {
                                "bsonType": "string",
                                "description": "must be a string and is required"
                            },
                            "state": {
                                "bsonType": "string",
                                "description": "must be a string and is required"
                            }, 
                            "CEP": {
                                "bsonType": "string",
                                "description": "must be a string if the field exists"
                            },
                        },
                        },
                        "email": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "password": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                        },
                        "create_date": {
                        "bsonType": "string",
                        "description": "must be a string and is not required"
                        }
                    }
                }
            }

            cmd = OrderedDict([('collMod', self.collection_name),
                    ('validator', vexpr),
                    ('validationLevel', 'moderate')])

            db_mongo["db-quante"].command(cmd)

    def get_by_email(self, email):
        with mg.MongoClient(self.mongo_url) as db_mongo:
            collection = db_mongo["db-quante"][self.collection_name]
            obj = collection.find_one({"email" : email})
            return self.convert(obj)


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
                    "required": [ "name" ],
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
                        # since this is an object that can be very different for each type 
                        # of product, I will not define specific and required fields for it, 
                        # but here are some examples of fields that may exist: brand, model, 
                        # line, series, heigh, width, depth, weight...
                        #
                        # it will be essentially a dictionary, though
                        },
                        "categories": {
                        "bsonType": "array"
                        },
                        "prices": {
                        "bsonType": "object",
                        "description": "must be an object if the field exists"
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

    def get_by_name(self, name: str):
        raise Exception("Review doesn't have a field called name")

    def get_by_substring(self, substr: str):
        raise Exception("Review doesn't have a field called name")

    def post(self, obj):
        productCollection = ProductCollection()
        product = productCollection.get(obj["product_id"])
        obj = orm.Review.convert(obj).__dict__

        if len(product["relevant_reviews"]) < 10:
            product["relevant_reviews"].append(obj)

        productCollection.put(product)
        return super().post(obj)

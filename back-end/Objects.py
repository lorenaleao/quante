# Standart import
from typing import Union
from datetime import datetime as dt

class IObject():
    @staticmethod
    def convert(obj : Union['IObject', dict]) -> 'IObject':
        raise NotImplementedError

class Client(IObject):
    def __init__(self, _id, name, cpf, age, email, password, create_date = dt.now()):
        self._id = _id
        self.name = name
        self.cpf = cpf
        self.age = age
        self.email = email
        self.password = password
        self.create_date = create_date
        
    @staticmethod
    def convert(obj : Union['Client', dict]) -> 'Client':
        if isinstance(obj, Client):
            return obj
        elif isinstance(obj, dict):
            _id = obj.get("_id", None)
            name = obj.get("name", None)
            cpf = obj.get("cpf", None)
            age = obj.get("age", None)
            email = obj.get("email", None)
            password = obj.get("password", None)
            create_date = obj.get("create_date", None)
            return Client(_id, name, cpf, age, email, password, create_date)        
        else:
            raise TypeError("Type " + obj.__class__.__name__ + " must be a Dict or Client.")
    
class Company(IObject):
    def __init__(self, _id, name, cnpj, email, password, create_date = dt.now()):
        self._id = _id
        self.name = name
        self.cnpj = cnpj
        self.email = email
        self.password = password
        self.create_date = create_date

    @staticmethod
    def convert(obj : Union['Company', dict]) -> 'Company':
        if isinstance(obj, Company):
            return obj
        elif isinstance(obj, dict):
            _id = obj.get("_id", None)
            name = obj.get("name", None)
            cnpj = obj.get("cnpj", None)
            email = obj.get("email", None)
            password = obj.get("password", None)
            create_date = obj.get("create_date", None)
            return Company(_id, name, cnpj, email, password, create_date)        
        else:
            raise TypeError(f"Type " + obj.__class__.__name__ + " must be a Dict or Company.")

class Product(IObject):
    def __init__(self, _id, name, description, spec, categories, prices):
        self.relevant_reviews = []
        self.price_history = [] # (time, price)
        self.prices = prices # given a company, a pair containing the current price and a list with requests to change
        self._id = _id
        self.name = name
        self.description = description
        self.spec = spec
        self.categories = categories

    @staticmethod
    def convert(obj: Union['Product', dict]) -> 'Product':
        if isinstance(obj, Product):
            return obj
        elif isinstance(obj, dict):
            _id = obj.get("_id", None)
            name = obj.get("name", None)
            prices = obj.get("prices", None)
            description = obj.get("description", None)
            spec = obj.get("spec", None)
            categories = obj.get("categories", None)
            return Product(_id, name, description, spec, categories, prices)
        else:
            raise TypeError(f"Type " + obj.__class__.__name__ + " must be a Dict or Product")

class Review(IObject):
    def __init__(self, _id, product_id, author, rating, is_recommended, likes):
        self._id = _id
        self.product_id = product_id
        self.author = author
        self.rating = rating
        self.is_recommended = is_recommended
        self.likes = likes

    @staticmethod
    def convert(obj: Union['Review', dict]) -> 'Review':
        if isinstance(obj, Review):
            return obj
        elif isinstance(obj, dict):
            _id = obj.get("_id", None)
            product_id = obj.get("product_id", None)
            author = obj.get("author", None)
            rating = obj.get("rating", None)
            is_recommended = obj.get("is_recommended", None)
            likes = obj.get("likes", 0)
            return Review(_id, product_id, author, rating, is_recommended, likes)
        else:
            raise TypeError(f"Type " + obj.__class__.__name__ + " must be a Dict or Review")

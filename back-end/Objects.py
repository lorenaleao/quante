# Standart import
from typing import Union

class IObject():
    @staticmethod
    def convert(obj : Union['IObject', dict]) -> 'IObject':
        raise NotImplementedError


class Client(IObject):
    def __init__(self, _id, name, cpf, age, email, password, create_date, perfil_img):
        self._id = _id
        self.name = name
        self.cpf = cpf
        self.age = age
        self.email = email
        self.password = password
        self.create_date = create_date
        self.perfil_img = perfil_img
        
    @staticmethod
    def convert(obj : Union['Client', dict]) -> 'Client':
        if isinstance(obj, Client):
            return obj
        elif isinstance(obj, dict):
            return Client(
                obj.get("_id", None), 
                obj.get("name", None), 
                obj.get("cpf", None), 
                obj.get("age", None), 
                obj.get("email", None), 
                obj.get("password", None), 
                obj.get("create_date", None), 
                obj.get("perfil_img", None))        
        else:
            raise TypeError("Type " + obj.__class__.__name__ + " must be a Dict or Client.")
    
    
class Company(IObject):
    def __init__(self, _id, name, cnpj, email, password, create_date, address):
        self._id = _id
        self.name = name
        self.cnpj = cnpj
        self.email = email
        self.password = password
        self.create_date = create_date
        self.address = address

    @staticmethod
    def convert(obj : Union['Company', dict]) -> 'Company':
        if isinstance(obj, Company):
            return obj
        elif isinstance(obj, dict):
            return Company(
                obj.get("_id", None), 
                obj.get("name", None), 
                obj.get("cnpj", None), 
                obj.get("email", None), 
                obj.get("password", None), 
                obj.get("create_date", None), 
                obj.get("address", None))         
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
            return Product(
                obj.get("_id", None), 
                obj.get("name", None), 
                obj.get("description", None), 
                obj.get("spec", None), 
                obj.get("categories", None),
                obj.get("prices", None))
        else:
            raise TypeError(f"Type " + obj.__class__.__name__ + " must be a Dict or Product")

            
class Review(IObject):
    def __init__(self, _id, product_id, review_author, review_rating, review_text, published_date, is_recommended, likes):
        self._id = _id
        self.product_id = product_id
        self.review_author = review_author
        self.review_rating = review_rating
        self.review_text = review_text
        self.published_date = published_date
        self.is_recommended	= is_recommended	
        self.likes = likes

    @staticmethod
    def convert(obj: Union['Review', dict]) -> 'Review':
        if isinstance(obj, Review):
            return obj
        elif isinstance(obj, dict):
            return Review(
                obj.get("_id", None), 
                obj.get("product_id", None), 
                obj.get("review_author", None), 
                obj.get("review_rating", None), 
                obj.get("review_text", None),
                obj.get("published_date", None),
                obj.get("is_recommended", None),
                obj.get("likes", None))
        else:
            raise TypeError(f"Type " + obj.__class__.__name__ + " must be a Dict or Review")
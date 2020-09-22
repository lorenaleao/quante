from Collections import *
from Objects import IObject, Client, Review, Product

class BusinessBase():
    def __init__(self, collection):
        self.collection = collection()
    
    def post(self, obj):
        return self.collection.post(obj)

    def get(self, _id):
        return self.collection.get(_id)

    def getByName(self, name: str):
        return self.collection.getByName(name)

    def list(self):
        return self.collection.list()

    def put(self, obj):
        return self.collection.put(obj)

    def delete(self, _id):
        return self.collection.delete(_id)


class ClientBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ClientCollection)
        
    def email_already_registered(self, email):
        return self.collection.get_by_email(email) != None

    def get_by_email_password(self, email, password):
        client = self.collection.get_by_email(email)
        if client is None or client.password != password:
            return None
        else:
            return client
        
class CompanyBusiness(BusinessBase):
    def __init__(self):
        super().__init__(CompanyCollection)

    def email_already_registered(self, email):
        return self.collection.get_by_email(email) != None

    def get_by_email_password(self, email, password):
        company = self.collection.get_by_email(email)
        if company is None or company.password != password:
            return None
        else:
            return company


class ProductBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ProductCollection)

class ReviewBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ReviewCollection)

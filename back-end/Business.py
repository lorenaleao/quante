from Collections import *
from Objects import IObject, Client

class BusinessBase():
    def __init__(self, collection):
        self.collection = collection()
    
    def post(self, obj):
        return self.collection.post(obj)
        
    def get(self, _id):
        return self.collection.get(_id)

    def put(self, obj):
        return self.collection.put(obj)
    
    def delete(self, _id):
        return self.collection.delete(_id)

class ClientBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ClientCollection)

class CompanyBusiness(BusinessBase):
    def __init__(self):
        super().__init__(CompanyCollection)

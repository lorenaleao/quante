from Collections import *
from Objects import IObject, Client

class BusinessBase():
    def __init__(self, collection):
        self.collection = collection()

    def convert(self, obj):
        if obj == None:
            return None
        else:
            return self.collection._type_.convert(obj)
    
    def post(self, obj):
        obj = self.convert(obj)
        return self.collection.post(obj.__dict__)
        
    def get(self, _id):
        return self.collection.get(_id)

    def put(self, obj):
        obj = self.convert(obj)
        return self.collection.put(obj.__dict__)
    
    def delete(self, _id):
        return self.collection.delete(_id)

class ClientBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ClientCollection)

class CompanyBusiness(BusinessBase):
    def __init__(self):
        super().__init__(CompanyCollection)

from DataBase import ClientCollection
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
        obj = self.collection.post(obj.__dict__)
        return self.convert(obj)
        
    def get(self, _id):
        obj = self.collection.get(_id)
        return self.convert(obj)

    def put(self, obj):
        obj = self.convert(obj)
        obj = self.collection.put(obj.__dict__)
        return self.convert(obj)
    
    def delete(self, _id):
        obj = self.collection.delete(_id)
        return self.convert(obj)

class ClientBusiness(BusinessBase):
    def __init__(self):
        super().__init__(ClientCollection)

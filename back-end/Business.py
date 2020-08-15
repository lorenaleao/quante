from DataBase import Collection
from Objects import IObject, Client

class BusinessBase():
    def __init__(self, _type : IObject):
        self.collection = Collection(_type)
        self._type = _type

    def convert(self, obj):
        if obj == None:
            return None
        else:
            return self._type.convert(obj)
    
    def add(self, obj):
        obj = self.convert(obj)
        obj = self.collection.add(obj.__dict__)
        return self.convert(obj)
        
    def get(self, _id):
        obj = self.collection.get(_id)
        return self.convert(obj)

    def update(self, obj):
        obj = self.convert(obj)
        obj = self.collection.update(obj.__dict__)
        return self.convert(obj)
    
    def delete(self, _id):
        obj = self.collection.delete(_id)
        return self.convert(obj)
    
class ClientBusiness(BusinessBase):
    def __init__(self):
        super().__init__(Client)
from DataBase import Collection
from Objects import IObject, Client

class BusinessBase():
    def __init__(self, _type : IObject):
        self.collection = Collection(_type)
        self._type = _type
        
class ClientBusiness(BusinessBase):
    def __init__(self):
        super().__init__(Client)
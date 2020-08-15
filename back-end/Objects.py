from datetime import datetime as dt
import abc

class IObject(metaclass = abc.ABCMeta):
    @staticmethod
    @abc.abstractstaticmethod
    def convert(obj):
        raise NotImplementedError
    
class Client(IObject):
    def __init__(self, name, age, _id = None, email = None, password = None, create_date = dt.now()):
        self._id = _id
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.create_date = create_date
        
    @staticmethod
    def convert(obj):
        pass
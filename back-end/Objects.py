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
        if isinstance(obj, Client):
            return obj
        elif isinstance(obj, dict):
            name = obj.get("name", None)
            age = obj.get("age", None)
            _id = obj.get("_id", None)
            email = obj.get("email", None)
            password = obj.get("password", None)
            create_date = obj.get("create_date", None)
            return Client(name, age, _id, email, password, create_date)        
        else:
            raise TypeError(f"Type '{obj.__class__.__name__}' must be a Dict or Client.")
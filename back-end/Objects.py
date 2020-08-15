from datetime import datetime as dt
import MapObj as mp
import abc

class IObject(metaclass = abc.ABCMeta):
    @staticmethod
    @abc.abstractstaticmethod
    def convert(obj):
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
    def convert(obj):
        return mp.toClient(obj)
    
class Company(IObject):
    def __init__(self, _id, name, cnpj, email, password, create_date = dt.now()):
        self._id = _id
        self.name = name
        self.cnpj = cnpj
        self.email = email
        self.password = password
        self.create_date = create_date
 
    @staticmethod
    def convert(obj):
        return mp.toCompany(obj)   
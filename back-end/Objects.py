from datetime import datetime as dt
import Mapper as mp
import abc

class Client():
    def __init__(self, _id, name, cpf, age, email, password, create_date = dt.now()):
        self._id = _id
        self.name = name
        self.cpf = cpf
        self.age = age
        self.email = email
        self.password = password
        self.create_date = create_date
    
class Company():
    def __init__(self, _id, name, cnpj, email, password, create_date = dt.now()):
        self._id = _id
        self.name = name
        self.cnpj = cnpj
        self.email = email
        self.password = password
        self.create_date = create_date
from Objects import *

def toClient(obj):
    if isinstance(obj, Client):
        return obj
    elif isinstance(obj, dict):
        _id = obj.get("_id", None)
        name = obj.get("name", None)
        cpf = obj.get("cpf", None)
        age = obj.get("age", None)
        email = obj.get("email", None)
        password = obj.get("password", None)
        create_date = obj.get("create_date", None)
        return Client(_id, name, cpf, age, email, password, create_date)        
    else:
        raise TypeError(f"Type '{obj.__class__.__name__}' must be a Dict or Client.")

def toCompany(obj):
    if isinstance(obj, Company):
        return obj
    elif isinstance(obj, dict):
        _id = obj.get("_id", None)
        name = obj.get("name", None)
        cnpj = obj.get("cnpj", None)
        email = obj.get("email", None)
        password = obj.get("password", None)
        create_date = obj.get("create_date", None)
        return Company(_id, name, cnpj, email, password, create_date)        
    else:
        raise TypeError(f"Type '{obj.__class__.__name__}' must be a Dict or Company.")
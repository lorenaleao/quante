from Objects import Client
from Business import ClientBusiness
import typing

x  = Client(name = "Raphael", age = 10)
coll = ClientBusiness()
coll.add(x)
print(x.__dict__)

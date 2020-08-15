from Objects import Client
from DataBase import Collection
import typing

x  = Client(name = "Raphael", age = 10).__dict__
coll = Collection(Client)
coll.add(x)

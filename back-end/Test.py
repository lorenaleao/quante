from Objects import Client
import typing

x  = Client(name = "Raphael", age = 10).__dict__
coll = Collection(Client)
coll.add(x)

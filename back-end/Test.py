from Objects import Client
from Business import ClientBusiness
import typing

x  = Client(name = "Raphael", age = 10)
coll = ClientBusiness()
coll.post(x)
print(x.__dict__)

print("-----------")
y = coll.get(x._id)
print(y.__dict__)

print("------------")
y.name = "Marcos"
z = coll.put(y)

print("-----------")
w = coll.get(x._id)
print(w.__dict__)

print("-----------")
w = coll.delete(x._id)
print(w._id)


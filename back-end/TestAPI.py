import requests
import json

url = "http://localhost:5000/client/post/"
data = {"name" : "João", "age" : 23}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.content, r.status_code)

res = r.json()

url = f'http://localhost:5000/client/get/{res["_id"]}'
r = requests.get(url)
print(r.content, r.status_code)

print(res["_id"])

url = "http://localhost:5000/client/put/"
data = {"_id" : res["_id"], "name" : "João", "age" : 24}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.put(url, data=json.dumps(data), headers=headers)
print(r.content, r.status_code)

url = "http://localhost:5000/client/put/"
data = {"_id" : "9f377808d3f8420986695b21", "name" : "Maçã", "age" : 50}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.put(url, data=json.dumps(data), headers=headers)
print(r.content, r.status_code)

#url = f'http://localhost:5000/client/delete/{res["_id"]}'
#r = requests.delete(url)
#print(r.content, r.status_code)


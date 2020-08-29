import requests
import json

url = "https://handy-balancer-285321.rj.r.appspot.com/img/post/"
fin = open('brain.jpeg', 'rb')
files = {'file': fin}
try:
    print(requests.post(url, files=files).text)
finally:
	fin.close()

"""
url = "http://localhost:5000/client/post/"
data = {"name" : "Maria", "age" : 100}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.content, r.status_code) 

url = "http://localhost:5000/client/put/"
data = {"_id" : "5f37f76714c16b17381f90b5", "name" : "João", "age" : 50}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.put(url, data=json.dumps(data), headers=headers)
print(r.content, r.status_code) 

url = "http://localhost:5000/client/get/5f37f76714c16b17381f90b3"
r = requests.get(url)
print(r.content, r.status_code) 

url = "http://localhost:5000/client/delete/5f37f76714c16b17381f90b3"
r = requests.delete(url)
print(r.content, r.status_code) 
"""

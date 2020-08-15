import requests
import json

url = "http://localhost:5000/client/post/"
data = {"name" : "Raphael Augusto", "age" : 24}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.content, r.status_code)
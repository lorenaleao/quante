import requests
import json

url = f'http://localhost:5000/company/delete/5f3789a0c65ba73f96741e84'
r = requests.delete(url)
print(r.content, r.status_code)

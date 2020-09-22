# Standard python imports
from datetime import datetime
import requests
import json
# Third part import
from bson.objectid import ObjectId
# Cadastro de clientes
url = "http://localhost:5000/client/post/"
data = {"name" : "Maria", "age" : 30, "cpf" : "000.000.000-00", "email" : "maria@email.com", "password" : "123456", "create_date" : str(datetime.now())}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data = json.dumps(data), headers=headers)
print(r.content.decode(), "status: ", r.status_code) 
url = "http://localhost:5000/client/post/"
data = {"name" : "João", "age" : 40, "cpf" : "111.111.111-11", "email" : "joao@email.com", "password" : "1234556", "create_date" : str(datetime.now())}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data = json.dumps(data), headers=headers)
print(r.content.decode(), "status: ", r.status_code) 
# Cadastro de empresas
url = "http://localhost:5000/company/post/"
data = {"name" : "Boteco do Paulo", "cnpj" : "99.999.999/9999-99", "address" : { "city" : "BH", "state" : "MG" }, "email" : "boteco.paulo@email.com", "password" : "123456", "create_date" : str(datetime.now())}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r_boteco_paulo = requests.post(url, data = json.dumps(data), headers=headers)
print(r_boteco_paulo.content.decode(), "status: ", r_boteco_paulo.status_code) 
boteco_paulo = json.loads(r_boteco_paulo.text)
url = "http://localhost:5000/company/post/"
data = {"name" : "Padaria da Joana", "cnpj" : "66.666.666/6666-66", "address" : { "city" : "BH", "state" : "MG" }, "email" : "padaria.joana@email.com", "password" : "123456", "create_date" : str(datetime.now())}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r_padaria_joana = requests.post(url, data = json.dumps(data), headers=headers)
print(r_padaria_joana.content.decode(), "status: ", r_padaria_joana.status_code) 
padaria_joana = json.loads(r_padaria_joana.text)
# Cadastro de Produtos  
## Produtos do Boteco do Paulo
url = "http://localhost:5000/product/post/"
data = {
    "name" : "Dose Cachaça Sul de Minas",
    "image" : None, 
    "description" : "Dose da Cachaça Sul de Minas. A cachaça Sul de Minas é conecida pelo sabor amadeirado e por seguir uma receita tradicional desde de 1920.", 
    "spec" : {
        "marca" : "Cachaça Sul de Minas",
        "Quantidade (ml)" : 100,
        "Teor alcoólico (%)" : 38.12, 
        "Calorias (kcal) por 100ml" : 200
    },
    "categories" : ["bebida alcoólica", "bebida", "produto brasileiro", "deliciosa"],
    "prices" : {
        boteco_paulo["_id"] : (1.0, [1.0, 1.1, 1.0, 1.0])
    },
    "price_history" : [(str(datetime.now()), 1.00)],
    "reviews" : []
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data = json.dumps(data), headers=headers)
print(r.content.decode(), "status: ", r.status_code) 
url = "http://localhost:5000/product/post/"
data = {
    "name" : "Porção de Torresmo",
    "image" : None, 
    "description" : "Porção de 200g de torresmo. O pedido vem acompanhado de sachês de maionese, ketchup e mostarda.", 
    "spec" : {
        "Tamanho da porção (g)" : 200,
        "Acompanhamentos" : "maionese, ketchup e mostarda"
    },
    "categories" : ["comida", "tira gosto", "salgado", "fritura"],
    "prices" : {
        boteco_paulo["_id"] : (1.0, [1.0, 1.1, 1.0, 1.0])
    },
    "price_history" : [(str(datetime.now()), 1.00)],
    "reviews" : []
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data = json.dumps(data), headers=headers)
print(r.content.decode(), "status: ", r.status_code) 
## Associar esses produtos a padaria da Joana
url = "http://localhost:5000/product/post/"
data = {
    "name" : "Quilo de Pão de queijo",
    "image" : None, 
    "description" : "Pão de queijo receita da vovó.", 
    "spec" : {
        "Unidade" : "kg"
    },
    "categories" : ["lanche", "tradição mineira", "comida"],
    "prices" : {
        padaria_joana["_id"] : (10.0, [10.0, 10.1, 10.0, 10.0])
    },
    "price_history" : [(str(datetime.now()), 10.00)],
    "reviews" : []
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data = json.dumps(data), headers=headers)
print(r.content.decode(), "status: ", r.status_code) 
url = "http://localhost:5000/product/post/"
data = {
    "name" : "Pão Francês",
    "image" : None, 
    "description" : "Pão francês quetinho que acabou de sair do forno.", 
    "spec" : {
        "Unidade" : "kg"
    },
    "categories" : ["lanche", "comida"],
    "prices" : {
        padaria_joana["_id"] : (12.0, [12.0, 12.1, 12.0, 12.0])
    },
    "price_history" : [(str(datetime.now()), 12.00)],
    "reviews" : []
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data = json.dumps(data), headers=headers)
print(r.content.decode(), "status: ", r.status_code) 
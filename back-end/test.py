import requests
import json
import pymongo as mg
import datetime

from secrets.QuanteSecrets import get_login

login, password = get_login()
mongo_url = "mongodb+srv://quante:" + password + "@db-quante.dni24.gcp.mongodb.net/" + login + "?retryWrites=true&w=majority"
        
def testProductValidateSchema():
    with mg.MongoClient(mongo_url) as db_mongo:
        try:
            db_mongo["db-quante"].Product.insert_one({"x":1})
            print("NOT good; the insert above should have failed.")
        except Exception as e:
            print("OK. Expected exception:" + str(e))

        try:
            okdoc = {"name":"buzz", "image": "/img/a.jpg", "description":"Math", 
            "categories":["cellphone", "eletronics"], "prices": {"carrefour": (2.5, [3.1, 4.0])}}
            db_mongo["db-quante"].Product.insert_one(okdoc)
            print("All good.")
        except Exception as e:
            print("exc:" + str(e)) 
        try:
            okdoc = {"name":"buzz", "image": "/img/a.jpg", "description":"Math", 
            "categories":["cellphone", "eletronics"]}
            db_mongo["db-quante"].Product.insert_one(okdoc)
            print("NOT good; the insert above should have failed.")
        except Exception as e:
            print("OK. Expected exception: " + str(e))

def testReviewValidateSchema(): 
    with mg.MongoClient(mongo_url) as db_mongo:
        try:
            db_mongo["db-quante"].Review.insert_one({"x":1})
            print("NOT good; the insert above should have failed.")
        except Exception as e:
            print("OK. Expected exception:" + str(e))

        try:
            okdoc = {"product_id":"001", "review_author": "João", "review_rating": 4.5, 
            "review_text":"mais ou menos", "published_date": str(datetime.datetime.now().timestamp()), "is_recommended": False}
            db_mongo["db-quante"].Review.insert_one(okdoc)
            print("All good.")
        except Exception as e:
            print("exc:" + str(e)) 
        try:
            okdoc = {"product_id":"002", "review_author": "Maria", "review_rating": 4.5, 
            "review_text":"mais ou menos", "is_recommended": False}
            db_mongo["db-quante"].Review.insert_one(okdoc)
            print("NOT good; the insert above should have failed.")
        except Exception as e:
            print("OK. Expected exception: " + str(e))

def testInsertImage():
    url = "https://handy-balancer-285321.rj.r.appspot.com/img/post/"
    fin = open('brain.jpeg', 'rb')
    files = {'file': fin}
    try:
        print(requests.post(url, files=files).text)
    finally:
        fin.close()

def main():
    testProductValidateSchema()
    testReviewValidateSchema()

main()

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

from flask import Flask, request, jsonify
from Business import *
import logging
import json
import os

app = Flask(__name__)

format = "LEVEL %(levelname)s: %(asctime)s\n%(message)s\n"
logging.basicConfig(filename = "log/log_records.log", level = logging.ERROR, format = format)

os.makedirs("log", exist_ok=True)
os.makedirs("db-login", exist_ok=True)

_clientBusiness = ClientBusiness()
_companyBusiness = CompanyBusiness()

def convert(obj):
    return json.dumps(obj.__dict__, default = str) if obj!= None else "null"

@app.route("/")
def it_works():
    return "It works! :)", 200

@app.route("/client/post/", methods=["POST"])
def post_client():
    try:
        data = request.get_json()
        client = _clientBusiness.post(data)
        return convert(client), 201
    except Exception as e:
        logging.error(f"Local: API post_client\nException: {e}")
        return "Internal Server Error", 500

@app.route("/client/put/", methods=["PUT"])
def put_client():
    try:
        data = request.get_json()
        client = _clientBusiness.put(data)
        return convert(client), 200
    except Exception as e:
        logging.error(f"Local: API put_client\nException: {e}")
        return "Internal Server Error", 500

@app.route("/client/get/<string:id_client>", methods=["GET"])
def get_client(id_client):
    try:
        client = _clientBusiness.get(id_client) 
        return convert(client), 200
    except Exception as e:
        logging.error(f"Local: API get_client\nException: {e}")
        return "Internal Server Error", 500

@app.route("/client/delete/<string:id_client>", methods=["DELETE"])
def delete_client(id_client):
    try:
        client = _clientBusiness.delete(id_client)
        return convert(client), 200
    except Exception as e:
        logging.error(f"Local: API delete_client\nException: {e}")
        return "Internal Server Error", 500

@app.route("/company/post/", methods=["POST"])
def post_company():
    try:
        data = request.get_json()
        company = _companyBusiness.post(data)
        return convert(company), 201
    except Exception as e:
        logging.error(f"Local: API post_company\nException: {e}")
        return "Internal Server Error", 500

@app.route("/company/put/", methods=["PUT"])
def put_company():
    try:
        data = request.get_json()
        company = _companyBusiness.put(data)
        return convert(company), 200
    except Exception as e:
        logging.error(f"Local: API put_company\nException: {e}")
        return "Internal Server Error", 500

@app.route("/company/get/<string:id_company>", methods=["GET"])
def get_company(id_company):
    try:
        company = _companyBusiness.get(id_company) 
        return convert(company), 200
    except Exception as e:
        logging.error(f"Local: API get_company\nException: {e}")
        return "Internal Server Error", 500

@app.route("/company/delete/<string:id_company>", methods=["DELETE"])
def delete_company(id_company):
    try:
        company = _companyBusiness.delete(id_company)
        return convert(company), 200
    except Exception as e:
        logging.error(f"Local: API delete_company\nException: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(debug = True)
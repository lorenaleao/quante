from flask import Flask, request, jsonify
from Business import ClientBusiness
import logging
import json
import os

app = Flask(__name__)

global _clientBusiness 

def convert(obj):
    return json.dumps(obj.__dict__, default = str) if obj!= None else "null"

@app.route("/")
def it_works():
    return "It works! :)", 200

@app.route("/client/get/<string:id_client>", methods=["GET"])
def get_client(id_client):
    try:
        client = _clientBusiness.get(id_client) 
        return convert(client), 200
    except Exception as e:
        logging.error(f"Local: API get_client\nException: {e}")
        return "Internal Server Error", 500

@app.route("/client/post/", methods=["POST"])
def post_client():
    try:
        data = request.get_json()
        client = _clientBusiness.add(data)
        return convert(client), 201
    except Exception as e:
        logging.error(f"Local: API post_client\nException: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    os.makedirs("log", exist_ok=True)
    os.makedirs("db-login", exist_ok=True)

    _clientBusiness = ClientBusiness()

    format = "LEVEL %(levelname)s: %(asctime)s\n%(message)s\n"
    logging.basicConfig(filename = "log/log_records.log", level = logging.ERROR, format = format)
    app.run(debug = True)
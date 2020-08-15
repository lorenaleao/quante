from flask import Flask, request, jsonify
from Business import ClientBusiness
import logging
import json

app = Flask(__name__)

_clientBusiness = ClientBusiness()

format = "LEVEL %(levelname)s: %(asctime)s\n%(message)s\n"
logging.basicConfig(filename = "log/log_records.log", level = logging.ERROR, format = format)

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

if __name__ == "__main__":
    app.run(debug = True)
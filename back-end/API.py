from flask import Flask, request, jsonify
from Business import *
import logging
import json
import os

app = Flask(__name__)

format = "LEVEL %(levelname)s: %(asctime)s\n%(message)s\n"
logging.basicConfig(filename = "log/log_records.log", level = logging.ERROR, format = format)

os.makedirs("log", exist_ok=True)

objects = {
    "client" : ClientBusiness(),
    "company" : CompanyBusiness()
}

def convert(obj):
    return json.dumps(obj, default = str) if obj!= None else "null"

@app.route("/")
def it_works():
    return "It works! :)", 200

@app.route("/<string:obj_key>/post/", methods=["POST"])
def post(obj_key):
    try:
        data = request.get_json()
        data = objects[obj_key].post(data)
        return convert(data), 201
    except Exception as e:
        logging.error(f"Local: API post {obj_key}\nException: {e}")
        return "Internal Server Error", 500

@app.route("/<string:obj_key>/put/", methods=["PUT"])
def put(obj_key):
    try:
        data = request.get_json()
        data = objects[obj_key].put(data)
        return convert(data), 200
    except Exception as e:
        logging.error(f"Local: API put {obj_key}\nException: {e}")
        return "Internal Server Error", 500

@app.route("/<string:obj_key>/get/<string:_id>", methods=["GET"])
def get(obj_key, _id):
    try:
        data = objects[obj_key].get(_id)
        return convert(data), 200
    except Exception as e:
        logging.error(f"Local: API get {obj_key} id: {_id} \nException: {e}")
        return "Internal Server Error", 500

@app.route("/<string:obj_key>/delete/<string:_id>", methods=["DELETE"])
def delete(obj_key, _id):
    try:
        data = objects[obj_key].delete(_id)
        return convert(data), 200
    except Exception as e:
        logging.error(f"Local: API delete {obj_key} id: {_id} \nException: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(debug = True)
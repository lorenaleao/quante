from flask import Flask, request, jsonify
from Business import *
import json
import os

app = Flask(__name__)

business = {
    "client" : ClientBusiness(),
    "company" : CompanyBusiness()
}

def convert(obj):
    return json.dumps(obj, default = str) if obj!= None else "null"

@app.route("/")
def it_works():
    return "It works! :)", 200

@app.route("/<string:key>/post/", methods=["POST"])
def post(key):
    try:
        data = request.get_json()
        data = business[key].post(data)
        return convert(data), 201
    except Exception as e:
        logging.error(f"Local: API post {key}\nException: {e}")
        return "Internal Server Error", 500

@app.route("/<string:key>/put/", methods=["PUT"])
def put(key):
    try:
        data = request.get_json()
        data = business[key].put(data)
        return convert(data), 200
    except Exception as e:
        logging.error(f"Local: API put {key}\nException: {e}")
        return "Internal Server Error", 500

@app.route("/<string:key>/get/<string:_id>", methods=["GET"])
def get(key, _id):
    try:
        data = business[key].get(_id)
        return convert(data), 200
    except Exception as e:
        logging.error(f"Local: API get {key} id: {_id} \nException: {e}")
        return "Internal Server Error", 500

@app.route("/<string:key>/delete/<string:_id>", methods=["DELETE"])
def delete(key, _id):
    try:
        data = business[key].delete(_id)
        return convert(data), 200
    except Exception as e:
        logging.error(f"Local: API delete {key} id: {_id} \nException: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(debug = True)
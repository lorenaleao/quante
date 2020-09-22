# Standart import
import json
import os

# Third part import
from flask import Flask, request, jsonify, send_file

# Local application imports
from Business import *
from Repository import LocalRepository

app = Flask(__name__)

image_repository = LocalRepository("img/")

business = {
    "client" : ClientBusiness(),
    "company" : CompanyBusiness(),
    "product": ProductBusiness(),
    "review": ReviewBusiness()
}

def convert(obj):
    return json.dumps(obj, default = str) if obj != None else "null"

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
        return f"Internal Server Error: {e}", 500

@app.route("/<string:key>/put/", methods=["PUT"])
def put(key):
    try:
        data = request.get_json()
        data = business[key].put(data)
        return convert(data), 201
    except Exception as e:
        return f"Internal Server Error: {e}", 500

@app.route("/<string:key>/get/<string:_id>", methods=["GET"])
def get(key, _id):
    try:
        data = business[key].get(_id)
        return convert(data), 200
    except Exception as e:
        return f"Internal Server Error: {e}", 500

@app.route("/<string:key>/delete/<string:_id>", methods=["DELETE"])
def delete(key, _id):
    try:
        data = business[key].delete(_id)
        return convert(data), 200
    except Exception as e:
        return f"Internal Server Error: {e}", 500

@app.route("/img/post/", methods=["POST"])
def post_img():
    try:
        url = image_repository.save(request.files["file"])
        return url, 201
    except Exception as e:
        return "Internal Server Error: " + str(e), 500

@app.route("/img/get/<string:img_name>", methods=["GET"])
def get_img(img_name):
    try:
        return image_repository.load(img_name), 200
    except Exception as e:
        return f"Internal Server Error: {e}", 500

@app.route("/login/email_already_registered/<string:email>", methods=["GET"])
def email_already_registered(email):
    try:
        val_cli = business["client"].email_already_registered(email)
        val_comp = business["company"].email_already_registered(email)
        return convert(val_cli or val_comp), 200
    except Exception as e:
        return f"Internal Server Error: {e}", 500

if __name__ == "__main__":
    app.run(debug = True)
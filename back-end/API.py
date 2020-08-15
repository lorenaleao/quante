from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

format = "LEVEL %(levelname)s: %(asctime)s\n%(message)s\n"
logging.basicConfig(filename = "log/log_records.log", level = logging.ERROR, format = format)

@app.route("/")
def it_works():
    return "It works! :)", 200

if __name__ == "__main__":
    app.run(debug = True)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def it_works():
    return "It works! :)", 200

if __name__ == "__main__":
    app.run(debug = True)
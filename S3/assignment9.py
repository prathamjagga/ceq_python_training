# This file contains solutions to assignment 9

# A simple Flask REST API with different methods

from flask import Flask, jsonify, make_response

app = Flask(__name__)

logs = []


@app.route("/", methods=["GET"])
def home():
    return make_response(
        jsonify({"success": "true", "message": "welcome to pratham's rest api"}), 200
    )


@app.route("/add-log", methods=["POST"])
def log():
    logs.append("POST called on /add-log --> 200")
    return make_response(
        jsonify({"success": "true", "message": "successfully posted the log."}), 200
    )


@app.route("/get-logs", methods=["GET"])
def get_logs():
    return make_response(jsonify(logs), 200)


app.run()

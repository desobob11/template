from flask import Flask
from flask import Response
from flask import jsonify
import requests

app = Flask(__name__)

def corsify(res):
        res.headers['Access-Control-Allow-Origin'] =  '*'
        res.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
        res.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        res.headers['Access-Control-Allow-Credentials'] = "true"


@app.route("/", methods=["GET"])
def root():
    headers = { "accept": "application/json", 'X-API-Key': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJic2Rvc3AiLCJpYXQiOjE3MDY1ODUzNTV9.o5hhN68_ab7t115fsvx3cb4EmDYVkO1FwU1CyqOVaH8'}
    req = requests.get("https://api.aeso.ca/report/v1/meritOrder/energy?startDate=2023-01-01", headers=headers)

    response = jsonify(req.json())
    corsify(response)

    return response






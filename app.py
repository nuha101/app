from flask import Flask, request, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

data = []

# GET API 
@app.route('/user', methods=['GET'])
def get_user():
    return jsonify(data)

# POST API 
@app.route('/user', methods=['POST'])
def add_user():
    new_item = request.get_json()  
    data.append(new_item)  
    return jsonify(new_item), 201  

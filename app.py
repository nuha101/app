from flask import Flask, request, jsonify
import os

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
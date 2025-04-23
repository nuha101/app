from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
messages = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/api/messages', methods=['POST'])
def post_message():
    data = request.get_json()
    message = data.get('message', '')
    if message:
        messages.append(message)
        return jsonify({'status': 'success', 'message': message}), 201
    return jsonify({'status': 'fail', 'error': 'No message provided'}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

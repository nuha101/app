from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage
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
    app.run(debug=True)

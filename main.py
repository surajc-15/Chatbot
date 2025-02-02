from flask import Flask, jsonify, request

app = Flask(__name__)

# Route 1: Health check
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "UP"}), 200

# Route 2: Get users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    return jsonify(users), 200

# Route 3: Add user
@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({"error": "Invalid input"}), 400
    new_user = {"id": 3, "name": data["name"]}
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)

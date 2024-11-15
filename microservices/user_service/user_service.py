from flask import Flask, request, jsonify

app = Flask(__name__)
users = []

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/add-user', methods=['POST'])
def add_user():
    data = request.get_json()
    user = {
        "userId": len(users) + 1,
        "firstName": data["firstName"],
        "lastName": data["lastName"],
        "email": data["email"],
        "cell": data["cell"]
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/api/authenticate-user', methods=['POST'])
def authenticate_user():
    data = request.get_json()
    user = next((u for u in users if u["email"] == data["email"] and u.get("password") == data.get("password")), None)
    if user:
        return jsonify({"message": "Authentication successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/api/update-user', methods=['POST'])
def update_user():
    data = request.get_json()
    user = next((u for u in users if u["email"] == data["email"]), None)
    if user:
        user.update(data)
        return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/api/get-user-info', methods=['GET'])
def get_user_info():
    lname = request.args.get("lname")
    email = request.args.get("email")
    user = next((u for u in users if u["lastName"] == lname or u["email"] == email), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

from flask import Flask, request, jsonify

app = Flask(__name__)
carts = {}

@app.route('/api/add-to-cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data["userId"]
    product_id = data["productId"]
    quantity = data["quantity"]

    if user_id not in carts:
        carts[user_id] = []
    carts[user_id].append({"productId": product_id, "quantity": quantity})
    return jsonify({"message": "Item added to cart"}), 200

@app.route('/api/remove-from-cart', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    user_id = data["userId"]
    product_id = data["productId"]
    
    if user_id in carts:
        carts[user_id] = [item for item in carts[user_id] if item["productId"] != product_id]
        return jsonify({"message": "Item removed from cart"}), 200
    return jsonify({"error": "Cart not found"}), 404

@app.route('/api/update-cart', methods=['POST'])
def update_cart():
    data = request.get_json()
    user_id = data["userId"]
    product_id = data["productId"]
    quantity = data["quantity"]

    if user_id in carts:
        for item in carts[user_id]:
            if item["productId"] == product_id:
                item["quantity"] = quantity
                return jsonify({"message": "Cart updated successfully"}), 200
    return jsonify({"error": "Item not found in cart"}), 404

@app.route('/api/get-cart-by-user/<int:user_id>', methods=['GET'])
def get_cart_by_user(user_id):
    cart = carts.get(user_id, [])
    return jsonify(cart), 200

if __name__ == '__main__':
    app.run(port=5003)

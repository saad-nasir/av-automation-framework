from flask import Flask, request, jsonify

app = Flask(__name__)
orders = []

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/place-order', methods=['POST'])
def place_order():
    data = request.get_json()
    order = {
        "orderId": len(orders) + 1,
        "userId": data["userId"],
        "status": "OrderPlaced"
    }
    orders.append(order)
    # Simulate sending email
    print(f"Order placed for user {data['userId']}")
    return jsonify(order), 201

@app.route('/api/process-payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    order = next((o for o in orders if o["orderId"] == data["orderId"]), None)
    if order:
        order["status"] = "Processing"
        return jsonify({"message": "Payment processed successfully"}), 200
    return jsonify({"error": "Order not found"}), 404

@app.route('/api/fulfill-order', methods=['POST'])
def fulfill_order():
    data = request.get_json()
    order = next((o for o in orders if o["orderId"] == data["orderId"]), None)
    if order:
        order["status"] = "Shipped"
        # Simulate sending shipment email
        print(f"Order {data['orderId']} shipped")
        return jsonify({"message": "Order fulfilled and shipped"}), 200
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(port=5004)

from flask import Flask, request, jsonify

app = Flask(__name__)
notifications = []
order_status_enum = ["OrderPlaced", "Processing", "Shipped", "Delivered"]

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/send-email', methods=['POST'])
def send_email_to_user():
    data = request.get_json()
    notification = {
        "userId": data["userId"],
        "email": data["email"],
        "orderId": data["orderId"],
        "status": "OrderPlaced"
    }
    notifications.append(notification)
    return jsonify({"message": "Email sent for order confirmation"}), 200

@app.route('/api/order-status-updates', methods=['GET'])
def get_order_status_updates():
    user_id = request.args.get("userId")
    order_id = request.args.get("orderId")
    status_updates = [n for n in notifications if n["userId"] == int(user_id) and n["orderId"] == int(order_id)]
    return jsonify(status_updates), 200

def send_status_email(order_id, user_id, status):
    if status in order_status_enum:
        # Logic to send email based on the order status
        print(f"Sending {status} email to user {user_id} for order {order_id}")

if __name__ == '__main__':
    app.run(port=5005)

from flask import Flask, request, jsonify

app = Flask(__name__)
products = []

@app.route('/api/add-product', methods=['POST'])
def add_product():
    data = request.get_json()
    product = {
        "productId": len(products) + 1,
        "name": data["name"],
        "price": data["price"],
        "details": data["details"]
    }
    products.append(product)
    return jsonify(product), 201

@app.route('/api/manage-product-price', methods=['POST'])
def manage_product_price():
    data = request.get_json()
    product = next((p for p in products if p["productId"] == data["productId"]), None)
    if product:
        product["price"] = data["price"]
        return jsonify({"message": "Product price updated successfully"}), 200
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/manage-product-details', methods=['POST'])
def manage_product_details():
    data = request.get_json()
    product = next((p for p in products if p["productId"] == data["productId"]), None)
    if product:
        product["details"] = data["details"]
        return jsonify({"message": "Product details updated successfully"}), 200
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(port=5002)

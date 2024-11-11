import pytest
import requests

# Base URLs for the microservices
USER_SERVICE_URL = "http://localhost:5001/api"
PRODUCT_CATALOG_URL = "http://localhost:5002/api"
SHOPPING_CART_URL = "http://localhost:5003/api"
ORDER_PROCESSING_URL = "http://localhost:5004/api"
NOTIFICATION_SERVICE_URL = "http://localhost:5005/api"

### User Service Tests ###
def test_add_user():
    response = requests.post(f"{USER_SERVICE_URL}/add-user", json={
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "cell": "1234567890"
    })
    assert response.status_code == 201
    assert "userId" in response.json()

def test_authenticate_user():
    # Add user first
    requests.post(f"{USER_SERVICE_URL}/add-user", json={
        "firstName": "Jane",
        "lastName": "Smith",
        "email": "jane.smith@example.com",
        "cell": "0987654321"
    })
    # Attempt to authenticate
    response = requests.post(f"{USER_SERVICE_URL}/authenticate-user", json={
        "email": "jane.smith@example.com",
        "password": "password123"  # This should match the password used during user creation
    })
    assert response.status_code in [200, 401]  # Depending on whether the password matches

### Product Catalog Service Tests ###
def test_add_product():
    response = requests.post(f"{PRODUCT_CATALOG_URL}/add-product", json={
        "name": "Test Product",
        "price": 50.0,
        "details": "A test product description"
    })
    assert response.status_code == 201
    assert "productId" in response.json()

def test_manage_product_price():
    # Add product first
    add_response = requests.post(f"{PRODUCT_CATALOG_URL}/add-product", json={
        "name": "Price Update Product",
        "price": 100.0,
        "details": "Product for price update test"
    })
    product_id = add_response.json()["productId"]

    # Update product price
    response = requests.post(f"{PRODUCT_CATALOG_URL}/manage-product-price", json={
        "productId": product_id,
        "price": 150.0
    })
    assert response.status_code == 200

### Shopping Cart Service Tests ###
def test_add_to_cart():
    # Add user and product first
    user_response = requests.post(f"{USER_SERVICE_URL}/add-user", json={
        "firstName": "Cart",
        "lastName": "User",
        "email": "cart.user@example.com",
        "cell": "1112223333"
    })
    user_id = user_response.json()["userId"]

    product_response = requests.post(f"{PRODUCT_CATALOG_URL}/add-product", json={
        "name": "Cart Product",
        "price": 20.0,
        "details": "Product for cart test"
    })
    product_id = product_response.json()["productId"]

    # Add item to cart
    response = requests.post(f"{SHOPPING_CART_URL}/add-to-cart", json={
        "userId": user_id,
        "productId": product_id,
        "quantity": 2
    })
    assert response.status_code == 200

def test_get_cart_by_user():
    # Add user and product to cart
    user_response = requests.post(f"{USER_SERVICE_URL}/add-user", json={
        "firstName": "Retrieve",
        "lastName": "CartUser",
        "email": "retrieve.cart@example.com",
        "cell": "4445556666"
    })
    user_id = user_response.json()["userId"]

    product_response = requests.post(f"{PRODUCT_CATALOG_URL}/add-product", json={
        "name": "Retrieve Cart Product",
        "price": 30.0,
        "details": "Product for retrieve cart test"
    })
    product_id = product_response.json()["productId"]

    # Add item to cart
    requests.post(f"{SHOPPING_CART_URL}/add-to-cart", json={
        "userId": user_id,
        "productId": product_id,
        "quantity": 3
    })

    # Retrieve cart
    response = requests.get(f"{SHOPPING_CART_URL}/get-cart-by-user/{user_id}")
    assert response.status_code == 200
    assert len(response.json()) > 0

### Order Processing Service Tests ###
def test_place_order():
    # Add user and product to cart
    user_response = requests.post(f"{USER_SERVICE_URL}/add-user", json={
        "firstName": "Order",
        "lastName": "Placer",
        "email": "order.placer@example.com",
        "cell": "7778889999"
    })
    user_id = user_response.json()["userId"]

    response = requests.post(f"{ORDER_PROCESSING_URL}/place-order", json={
        "userId": user_id
    })
    assert response.status_code == 201
    assert "orderId" in response.json()

### Notification Service Tests ###
def test_send_email_notification():
    response = requests.post(f"{NOTIFICATION_SERVICE_URL}/send-email", json={
        "userId": 1,
        "email": "notification.user@example.com",
        "orderId": 123
    })
    assert response.status_code == 200
    assert "Email sent" in response.json()["message"]

### Running All Tests ###
if __name__ == "__main__":
    pytest.main()

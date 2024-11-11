from locust import HttpUser, TaskSet, task, between

# Define user behavior for User Service
class UserServiceBehavior(TaskSet):
    @task(1)
    def add_user(self):
        self.client.post("/api/add-user", json={
            "firstName": "Load",
            "lastName": "Tester",
            "email": "load.tester@example.com",
            "cell": "1234567890"
        })

    @task(1)
    def get_user_info(self):
        self.client.get("/api/get-user-info", params={
            "email": "load.tester@example.com"
        })

# Define user behavior for Product Catalog Service
class ProductCatalogServiceBehavior(TaskSet):
    @task(1)
    def add_product(self):
        self.client.post("/api/add-product", json={
            "name": "Load Test Product",
            "price": 100.0,
            "details": "A product for load testing"
        })

    @task(1)
    def manage_product_price(self):
        self.client.post("/api/manage-product-price", json={
            "productId": 1,
            "price": 150.0
        })

# Define user behavior for Shopping Cart Service
class ShoppingCartServiceBehavior(TaskSet):
    @task(1)
    def add_to_cart(self):
        self.client.post("/api/add-to-cart", json={
            "userId": 1,
            "productId": 1,
            "quantity": 2
        })

    @task(1)
    def get_cart_by_user(self):
        self.client.get("/api/get-cart-by-user/1")

# Define user behavior for Order Processing Service
class OrderProcessingServiceBehavior(TaskSet):
    @task(1)
    def place_order(self):
        self.client.post("/api/place-order", json={
            "userId": 1
        })

    @task(1)
    def process_payment(self):
        self.client.post("/api/process-payment", json={
            "orderId": 1
        })

    @task(1)
    def fulfill_order(self):
        self.client.post("/api/fulfill-order", json={
            "orderId": 1
        })

# Define user behavior for Notification Service
class NotificationServiceBehavior(TaskSet):
    @task(1)
    def send_email(self):
        self.client.post("/api/send-email", json={
            "userId": 1,
            "email": "user@example.com",
            "orderId": 123
        })

    @task(1)
    def get_order_status_updates(self):
        self.client.get("/api/order-status-updates", params={
            "userId": 1,
            "orderId": 123
        })

# Main user class that simulates load across all microservices
class EcommerceUser(HttpUser):
    tasks = [
        UserServiceBehavior,
        ProductCatalogServiceBehavior,
        ShoppingCartServiceBehavior,
        OrderProcessingServiceBehavior,
        NotificationServiceBehavior
    ]
    wait_time = between(1, 5)  # Wait between 1 and 5 seconds between tasks
    host = "http://localhost:5001"  # Change the port number as needed for each microservice

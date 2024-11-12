---

# Test Automation Framework for an E-commerce Microservices Project

This project is an e-commerce application built using a microservice architecture. The application includes multiple microservices for handling different parts of the e-commerce flow, such as user management, product catalog, shopping cart, order processing, and notifications. It features a robust testing framework using Pytest for unit and integration tests, Locust for performance testing, and a CI/CD pipeline implemented with GitHub Actions.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Microservices](#microservices)
- [Testing Framework](#testing-framework)
- [Performance Testing](#performance-testing)
- [CI/CD Pipeline](#cicd-pipeline)
- [Setup Instructions](#setup-instructions)
- [Running the Microservices](#running-the-microservices)
- [Running Tests](#running-tests)
- [Performance Testing with Locust](#performance-testing-with-locust)
- [Future Enhancements](#future-enhancements)

---

## Project Overview
The e-commerce application is built using the Flask framework for each microservice. The project is structured to enable easy development, testing, and deployment. The core functionalities of the e-commerce workflow, from user registration to order processing and notifications, are covered.

---

## Microservices
### 1. User Service
- **Responsibilities**: Handles user registration, authentication, and profile management.
- **Endpoints**:
  - `POST /api/add-user`
  - `POST /api/authenticate-user`
  - `POST /api/update-user`
  - `GET /api/get-user-info`

### 2. Product Catalog Service
- **Responsibilities**: Manages the product catalog, including product details, categories, and pricing.
- **Endpoints**:
  - `POST /api/add-product`
  - `POST /api/manage-product-price`
  - `POST /api/manage-product-details`

### 3. Shopping Cart Service
- **Responsibilities**: Allows users to add, update, and remove items from their shopping cart.
- **Endpoints**:
  - `POST /api/add-to-cart`
  - `POST /api/remove-from-cart`
  - `POST /api/update-cart`
  - `GET /api/get-cart-by-user`

### 4. Order Processing Service
- **Responsibilities**: Handles order placement, payment processing, and order fulfillment.
- **Endpoints**:
  - `POST /api/place-order`
  - `POST /api/process-payment`
  - `POST /api/fulfill-order`

### 5. Notification Service
- **Responsibilities**: Sends email notifications to users for order confirmations and status updates.
- **Endpoints**:
  - `POST /api/send-email`
  - `GET /api/order-status-updates`

---

## Testing Framework
- **Unit and Integration Tests**: 
  - Implemented using **Pytest** and embedded within each microservice file.
  - Tests cover core functionality and ensure interactions between microservices work as expected.

- **End-to-End Tests**: 
  - Simulate the complete user journey from registration to order placement and notifications.

- **Test Results**: 
  - Test results are generated in XML format and uploaded as artifacts in the CI/CD pipeline.

---

## Performance Testing
- **Tool**: **Locust** is used for performance testing.
- **Coverage**: Each microservice is tested individually under load to evaluate performance and scalability.
- **Test Duration**: Locust tests are configured to run for a specified duration (e.g., 2 minutes per microservice).

---

## CI/CD Pipeline
- **Platform**: **GitHub Actions** is used to automate testing and deployment.
- **Features**:
  - Runs unit, integration, and performance tests on every commit and pull request.
  - Uploads test reports as artifacts for easy review.
  - Uses `continue-on-error` to ensure all performance tests run even if one fails.

---

## Setup Instructions
### Prerequisites
- **Python**: Version 3.8 or higher
- **Pip**: Package manager for Python
- **Virtual Environment**: Recommended to isolate dependencies

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/saad-nasir/av-automation-framework.git
   cd av-automation-framework
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On macOS/Linux
   myenv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Microservices
1. Navigate to the `microservices/` directory and start each microservice:
   ```bash
   python user_service.py
   python product_catalog_service.py
   python shopping_cart_service.py
   python order_processing_service.py
   python notification_service.py
   ```
2. Each microservice will run on a different port (e.g., `5001`, `5002`, etc.).

---

## Running Tests
### Unit and Integration Tests
- Run all tests using Pytest:
  ```bash
  pytest --junitxml=test-reports/results.xml
  ```

### Viewing Test Results
- Test results are saved in `test-reports/results.xml` and can be viewed using any XML viewer.

---

## Performance Testing with Locust
1. Ensure the microservices are running.
2. Run Locust tests for each microservice:
   ```bash
   locust -f performance_tests/locustfile.py --headless -u 10 -r 2 --host=http://localhost:5001 --run-time 2m
   ```

---

## Future Enhancements
1. **Security Testing**: Integrate tools like **Bandit** or **OWASP ZAP** for automated security checks.
2. **Infrastructure as Code (IaC)**: Use tools like **Terraform** to automate the provisioning of testing environments.
3. **Database Integration**: Replace in-memory data storage with a real database for production use.
4. **Monitoring and Logging**: Integrate monitoring tools like **Datadog** or **Prometheus** to track performance in real time.

---


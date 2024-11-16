#!/bin/bash

# Wait for services to be ready
echo "Waiting for services to be ready..."

# Wait for each service
for service in user_service:5001 product_catalog_service:5002 shopping_cart_service:5003 order_processing_service:5004 notification_service:5005; do
    echo "Waiting for $service..."
    until curl -s "http://$service/health" > /dev/null; do
        echo -n "."
        sleep 1
    done
    echo "$service is ready!"
done

echo "All services are ready. Running tests..."

# Run the tests
pytest tests/ --junitxml=test-reports/results.xml
import unittest
from microservices.order_processing_service import app

class OrderProcessingServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_place_order(self):
        response = self.app.post('/api/place-order', json={
            "userId": 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("orderId", response.get_json())

    def test_process_payment(self):
        self.app.post('/api/place-order', json={"userId": 1})
        response = self.app.post('/api/process-payment', json={"orderId": 1})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

import unittest
from microservices.notification_service import app

class NotificationServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_send_email_to_user(self):
        response = self.app.post('/api/send-email', json={
            "userId": 1,
            "email": "user@example.com",
            "orderId": 123
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Email sent", response.get_json()["message"])

    def test_get_order_status_updates(self):
        self.app.post('/api/send-email', json={
            "userId": 1,
            "email": "user@example.com",
            "orderId": 123
        })
        response = self.app.get('/api/order-status-updates', query_string={
            "userId": 1,
            "orderId": 123
        })
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.get_json()), 0)

if __name__ == '__main__':
    unittest.main()

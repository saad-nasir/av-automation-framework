import unittest
from microservices.user_service import app

class UserServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_user(self):
        response = self.app.post('/api/add-user', json={
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "cell": "1234567890"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("userId", response.get_json())

    def test_get_user_info(self):
        self.app.post('/api/add-user', json={
            "firstName": "Jane",
            "lastName": "Smith",
            "email": "jane.smith@example.com",
            "cell": "0987654321"
        })
        response = self.app.get('/api/get-user-info', query_string={"email": "jane.smith@example.com"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["email"], "jane.smith@example.com")

if __name__ == '__main__':
    unittest.main()

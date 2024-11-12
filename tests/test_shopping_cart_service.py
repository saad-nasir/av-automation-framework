import unittest
from microservices.shopping_cart_service import app

class ShoppingCartServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_to_cart(self):
        response = self.app.post('/api/add-to-cart', json={
            "userId": 1,
            "productId": 1,
            "quantity": 2
        })
        self.assertEqual(response.status_code, 200)

    def test_get_cart_by_user(self):
        self.app.post('/api/add-to-cart', json={
            "userId": 1,
            "productId": 1,
            "quantity": 2
        })
        response = self.app.get('/api/get-cart-by-user/1')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.get_json()), 0)

if __name__ == '__main__':
    unittest.main()

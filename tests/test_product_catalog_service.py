import unittest
from microservices.product_catalog_service import app

class ProductCatalogServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_product(self):
        response = self.app.post('/api/add-product', json={
            "name": "Test Product",
            "price": 50.0,
            "details": "Test product details"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("productId", response.get_json())

    def test_manage_product_price(self):
        self.app.post('/api/add-product', json={
            "name": "Price Test Product",
            "price": 100.0,
            "details": "Product for testing price update"
        })
        response = self.app.post('/api/manage-product-price', json={
            "productId": 1,
            "price": 150.0
        })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

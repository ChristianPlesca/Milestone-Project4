from django.test import TestCase
from products.models import Product
from datetime import datetime
# Create your tests here.

class TestProductsViews(TestCase):
    def setUp(self):
        Product.objects.create(
            name='Test Product',
            description='Product description',
            price=28600.000,
            bid_price = 20000.000,
            author="Leonardo Davinci",
            date_made=1732,
            country_made_in="England",
            height=323.0,
            width=123.5,
            past_owners="Bruce Dikinson",
            date_created=datetime.now(),  
        )    
    def test_product_template(self):
        url = self.client.get('/products/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed('index.html')

    def test_product_info(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, 'Product description')
        self.assertEqual(str(product.name), 'Test Product')
        self.assertEqual(float(product.price), 28600.000)
        self.assertTemplateUsed('products_detail.html')
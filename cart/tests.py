from django.test import TestCase


def test_view_cart_template(self):
        url = self.client.get('/cart/')

        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'cart.html')
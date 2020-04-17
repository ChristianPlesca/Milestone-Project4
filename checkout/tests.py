from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from checkout.forms import MakePaymentForm, OrderForm
from datetime import datetime


# VIEWS 
class CheckoutViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            email='christian@test.com',
            username='christian',
            password='1234qwer',
            first_name='Christian',
            last_name='Plesca'
        )

        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10000.994,
            bid_price=10000.994,
            height=10.2,
            width=12.4,
            date_created=datetime.now(),
            
        )

    def test_checkout_template(self):
        url = self.client.get('/checkout/')

        self.assertTrue(url.status_code, 200)

    def test_checkout_payment_valid_credentials(self):
        self.client.login(email='christian@test.com', password='1234qwer')
        product = Product.objects.get(id=1)
        url = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '8',
            'expiry_year': '2020',
            'stripe_id': 'tok_visa',
        })

        self.assertTrue(url.status_code, 200)

    def test_checkout_payment_with_declined_card(self):
        self.client.login(email='christian@test.com', password='1234qwer')
        product = Product.objects.get(id=1)
        url = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '6',
            'expiry_year': '2025',
            'stripe_id': 'tok_chargeDeclined',
        }, follow=True)

        self.assertTemplateNotUsed('index.html')

# FORMS

class CheckoutFormsTests(TestCase):

    def test_valid_payment_form(self):
        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '6',
            'expiry_year': '2025',
            'stripe_id': 'fgd456',
        })

        self.assertTrue(form.is_valid())

def test_valid_order_form(self):
        form = OrderForm({
            "full_name": "Christian Plesca",
            "house_number": "143 ",
            "address1": "143 Bertram Road",
            "city": "London",
            "county": "Enfield",
            "post_code": "EN1 1LS",
            "country": "United Kingdom",
            "phone_number": "08745677",
        })

        self.assertTrue(form.is_valid())

def test_invalid_order_form(self):
        form = OrderForm({
            "full_name": "Christian Plesca",
            "house_number": "12",
            "address1": "143 Bertram Road",
            "county": "Enfield",
            "post_code": "EN1 1LS",
            "country": "United Kingdom",
        })

        self.assertFalse(form.is_valid())
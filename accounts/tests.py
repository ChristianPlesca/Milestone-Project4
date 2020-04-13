from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm

class TestAccountViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='ville@yahoo.com',
            username='ville',
            password='vallo',
            first_name='Ville',
            last_name='Vallo'
        )
    def test_login_template(self):
        url = self.client.get('/accounts/login/')

        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'login.html')

    def test_valid_credentials(self):
        url = self.client.post('/accounts/login/', {
            'username': 'ville',
            'password': 'vallo'
        })
        user = User.objects.get(email='ville@yahoo.com')

        self.assertEqual(url.status_code, 200)
        self.assertTrue(user.is_authenticated)

    def test_register_template(self):
        url = self.client.get('/accounts/register/')

        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'register.html')
    

class TestAccountsForms(TestCase):
    def test_valid_registration_form(self):
        form = UserRegistrationForm({
            'username': 'ville',
            'email': 'ville@gmail.com',
            'password1': 'villevalo123',
            'password2': 'villevalo123'
        })

        self.assertTrue(form.is_valid())

    def test_valid_login(self):
        form = UserLoginForm({
            'username_or_email': 'christian',
            'password': '1234mama',
        })

        self.assertTrue(form.is_valid())
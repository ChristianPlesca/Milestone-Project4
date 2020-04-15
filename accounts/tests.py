from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm

"""Test Views"""
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
    

"""Test Forms"""
class TestAccountsForms(TestCase):
    def test_valid_registration_form(self):
        form = UserRegistrationForm({
            'username': 'ville',
            'email': 'ville@gmail.com',
            'password1': 'villevalo123',
            'password2': 'villevalo123'
        })

        self.assertTrue(form.is_valid())
    
    def test_invalid_registration_password_dont_match(self):
        form = UserRegistrationForm({
            'username': 'ville',
            'email': 'ville@gmail.com',
            'password1': 'villevalo123',
            'password2': 'villevalo12'
        })
        self.assertFalse(form.is_valid())

    def test_valid_login(self):
        form = UserLoginForm({
            'username_or_email': 'christian',
            'password': '1234mama',
        })

        self.assertTrue(form.is_valid())

    def test_password_required_on_login(self):
        form = UserLoginForm({'username': 'christian'})
        self.assertFalse(form.is_valid())
        
    
    def test_username_required_on_login(self):
        form = UserLoginForm({'password': '1234qwer'})
        self.assertFalse(form.is_valid())

    def test_registration_email_must_be_unique(self):
        User.objects.create_user(
            username='christian',
            email='cristi@yahoo.com')

        form = UserRegistrationForm({
            'username': 'christian',
            'email': 'cristi@yahoo.com',
            'password1': '1234qwer',
            'password2': '1234qwer'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],
                         ['Email address must be unique!'])
        
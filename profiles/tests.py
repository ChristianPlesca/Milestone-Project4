from django.test import TestCase
from django.contrib.auth.models import User

class TestProfilesApp(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email='christian@gmail.com',
            username='christian',
            password='4321qwer',
            first_name='Christian',
            last_name='Plesca'
        )

    def test_profile_template(self):
        user = User.objects.get(id=1)
        url = self.client.get('/profile/')

        self.assertEqual(url.status_code, 302)
        self.assertTemplateUsed('profiles.html')
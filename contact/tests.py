from django.test import TestCase
from contact.forms import ContactForm

# VIEWS 
class TestContactViews(TestCase):

    def test_contact_template(self):
        page = self.client.get('/contact-us/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed('contact.html')

    def test_contact_post_method(self):
        page = self.client.post('/contact-us/', {
            'contact_name': 'Christian Plesca',
            'contact_email': 'cristi@gmail.com',
            'phone_number': '08573632',
            'message_subject': 'Subject',
            'message_content': 'Content',
        })

        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, '/contact-us/')

# FORMS 
class TestContactForms(TestCase):

    def test_valid_contact_form(self):
        form = ContactForm({
            'contact_name': 'Christian Plesca',
            'contact_email': 'cristi@gmail.com',
            'phone_number' : '074567788',
            'message_subject': 'Subject',
            'message_content': 'Content',
        })

        self.assertTrue(form.is_valid())

    def test_invalid_contact_form(self):
        form = ContactForm({
            'contact_name': 'Christian Plesca',
            'message_subject': 'Subject',
        })

        self.assertFalse(form.is_valid())
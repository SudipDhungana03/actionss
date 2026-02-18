from django.test import TestCase
from .utils import add 
from django.urls import reverse

class AddFunctionTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

class RegistrationViewTestCase(TestCase):
    def test_registration_contains_input_user(self):
        response = self.client.get(reverse('form'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Name')
       
        self.assertContains(response, 'Email')
       
        self.assertContains(response, 'Password')
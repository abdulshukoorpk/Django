from django.test import TestCase
from django.contrib.auth.models import User

from apps.accounts.forms import RegistrationForm


class RegisterFormTest(TestCase):

    def setUp(self):
        self.data = {
            'username': 'test2',
            'email': 'test2@test.com',
            'password': 'abcd1234',
            'password_confirm': 'abcd1234'
        }

    def test_0_valid_form(self):
        form = RegistrationForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_1_invalid_form(self):
        self.data['password_confirm'] = 'Abcd1234'
        form = RegistrationForm(data=self.data)
        self.assertFalse(form.is_valid())

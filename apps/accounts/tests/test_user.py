from django.contrib.auth.models import User
from django.test import TestCase

from model_mommy import mommy

class RegisterTestCase(TestCase):

    """
    Test case for generating a user using model-mommy
    """

    def setUp(self):
        self.user = mommy.make(User)
        print self.user.email

    def test_user(self):
        self.assertEquals(isinstance(self.user, User), True)

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful"""
        email = 'test@testmail.com'
        password = 'Testp4ssw0rd'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a newuser is normalized """
        email = 'test@UPPERCASE.COM'
        user = get_user_model().objects.create_user(email, 'Testp4ssw0rd')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Testp4ssw0rd')

    def test_create_new_superuser(self):
        """ Test create new superuser """
        user = get_user_model().objects.create_superuser(
            'test@testuser.com',
            'Testp4ssw0rd'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

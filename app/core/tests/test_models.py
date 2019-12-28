from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful"""
        email = 'testd@yopmail.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Test if the user email is normalized"""
        email = 'test@YAHOO.com'
        user = get_user_model().objects.create_user(email=email,password='test123')

        self.assertEqual(user.email,email.lower())


    def test_new_user_invalid_email(self):
        """Test if user with no email raises value error"""

        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            'test@yopmail.com',
            'test123'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
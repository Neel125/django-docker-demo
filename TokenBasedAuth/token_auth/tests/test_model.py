from django.test import TestCase
from django.contrib.auth import get_user_model


def sample_user(email="test@gmail.com", password="Test123"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email=email, password=password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = "neelgajjar125@gmail.com"
        password = "Test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "Test123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')

    def test_create_new_superuser(self):
        """Createing new superuesr"""
        user = get_user_model().objects.create_superuser(
            "neelgajjar125@gmail.com",
            "Test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

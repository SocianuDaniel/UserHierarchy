"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Owner


class ModelTest(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_has_normalise_email(self):
        email_checks = [
            ['test@EXAMPLE.com', 'test@example.com'],
            ['test1@example.COM', 'test1@example.com'],
            ['test2@EXAMPLE.COM', 'test2@example.com'],
            ['Test3@Example.Com', 'Test3@example.com']
        ]
        for email, expect in email_checks:
            user = get_user_model().objects.create_user(
                email=email,
                password="pass123"
                )
            self.assertEqual(user.email, expect)

    def test_input_email_is_empty(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password="pass123"
            )

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email="test123@email.com",
            password="pass123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_owner(self):
        payload = {
                "email": "testowner@example.com",
                "password": "pass123"
        }
        owner = Owner.objects.create_owner(
            email=payload['email'],
            password=payload['password']
        )
        ownerUser = get_user_model().objects.get(email=payload['email'])
        self.assertEqual(owner.user, ownerUser)
        self.assertEqual(owner.level, 1)

    def test_owner_is_not_superuser(self):
        payload = {
                "email": "testowner@example.com",
                "password": "pass123"
        }
        owner = Owner.objects.create_owner(
            email=payload['email'],
            password=payload['password']
        )
        self.assertFalse(owner.user.is_superuser)
        self.assertFalse(owner.user.is_staff)

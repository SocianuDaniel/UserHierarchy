from django.test import TestCase
from django.contrib.auth import get_user_model
# from core.models import Owner
from core import forms


class OwnerTest(TestCase):
    """ Test for owner """

    def test_error_if_user_exists(self):
        """ Test if throw error if user exists """
        payload = {
            'email': "test123@email.com",
            'password1': 'pass123',
            'password2': 'pass123'
        }
        user = get_user_model().objects.create_user(
            email=payload['email'],
            password=payload['password1']
            )
        form = forms.CreateOwnerForm(data=payload)

        self.assertFormError(
            form=form,
            field='email',
            errors='user allready in the database')

    def test_success_create_owner(self):
        payload = {
            'email': "test123@email.com",
            'password1': 'pass123',
            'password2': 'pass123'
        }
        form = forms.CreateOwnerForm(data=payload)
        self.assertTrue(form.is_valid())

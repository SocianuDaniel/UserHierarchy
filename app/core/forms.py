from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
# from . import models


class CreateOwnerForm(forms.Form):
    """
    Form to create a Owner
    """
    email = forms.EmailField()
    password1 = forms.CharField(
        help_text=_('password'),
        max_length=16, widget=forms.PasswordInput()
        )
    password2 = forms.CharField(
        help_text=_('password confirmation'),
        max_length=16,
        widget=forms.PasswordInput()
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        user = get_user_model().objects.all().filter(email=email)
        print(user)
        if user:
            raise ValidationError(_('user allready in the database'))
        return email

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password1')
        pass2 = cleaned_data.get('password2')
        if pass1 != pass2:
            raise ValidationError(_('password1 in not equal with password2'))

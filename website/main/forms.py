from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from .models import IdentityModel


class TestForm(ModelForm):
    class Meta:
        model = IdentityModel
        fields = ['choice', 'eduChoice', 'fparent', 'socialStatus']
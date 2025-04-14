from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )

    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserSigninForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")
        
    username = forms.CharField()
    password = forms.CharField()

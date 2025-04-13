from django import forms
from django.contrib.auth.forms import UserCreationForm

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

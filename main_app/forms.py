from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.forms import Form
from .models import User

class NewSignUpForm(forms.Form):
    email = forms.CharField(label="Email", max_length=100, required=True)
    password = forms.CharField(label="Password", max_length=50, required=True)

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email','username')
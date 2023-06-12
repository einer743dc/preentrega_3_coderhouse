from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Agregado reciente
# class UserLoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

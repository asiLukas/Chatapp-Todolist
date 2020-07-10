from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={
        'placeholder': '*Not required*'
    }))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': '*Not required*'
    }))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': '*Not required*'
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        ]

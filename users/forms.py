from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import *

class Userloginform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'parol'}))

    class Meta:
        model = User
        fields = ('username', 'password',)






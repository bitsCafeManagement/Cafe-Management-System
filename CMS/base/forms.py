from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    full_name = forms.CharField(max_length=60)
    
    class Meta:
        model = User
        fields = ['full_name','username', 'email', 'password1', 'password2']
        
class AuthenticateForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(max_length=60, label= 'Email/Username')
        model = User
        fields = ['username', 'password']
    
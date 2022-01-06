from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields
from django.forms import ModelForm
from  cafe.models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class AuthenticateForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class UpdateProfile(ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
class UpdateProfilePhoto(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']
        
class AddContactInfo(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address']
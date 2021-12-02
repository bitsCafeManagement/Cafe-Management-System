from django.http import request
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(request):
    form = UserCreationForm()
    return render(request, 'base/register.html', {'form':form})

def login(request):
    form = AuthenticationForm()
    return render(request, 'base/login.html', {'form':form})


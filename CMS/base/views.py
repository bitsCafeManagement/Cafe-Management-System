from django.http import request
from .forms import RegistrationForm, AuthenticateForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'base/register.html', {'form':form, 'title':'Register'})

def home(request):
    context = {
        'title':'Home'
    }
    return render(request, 'base/home.html', context)

def contact(request):
    context = {
        'title':'Contact'
    }
    return render(request, 'base/contact.html', context)


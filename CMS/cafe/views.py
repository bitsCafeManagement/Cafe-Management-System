from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

@login_required
def homecafe(request):
    context = {
        'title':'Home'
    }
    return render(request, 'cafe/home.html', context)
@login_required
def profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'cafe/profile.html', context)
@login_required
def menu(request):
    context = {
        'title':'Menu'
    }
    return render(request, 'cafe/menu.html', context)
@login_required
def community(request):
    context = {
        'title':'Community'
    }
    return render(request, 'cafe/community.html', context)


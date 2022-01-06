from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from  base.forms import UpdateProfile, UpdateProfilePhoto, AddContactInfo

# Create your views here.

@login_required
def homecafe(request):
    context = {
        'title':'Home'
    }
    return render(request, 'cafe/home.html', context)
@login_required
def profile(request):
    if request.method == 'POST':
        U_form = UpdateProfile(request.POST, instance = request.user)
        P_form = UpdateProfilePhoto(request.POST,request.FILES ,instance= request.user.profile)
        C_form = AddContactInfo(request.POST, instance = request.user.profile)
        
        if U_form.is_valid() and P_form.is_valid():
            U_form.save()
            P_form.save()
            return redirect('profile')
        if C_form.is_valid():
            C_form.save()
            return redirect('profile')
        
    else:
        U_form = UpdateProfile(instance = request.user)
        P_form = UpdateProfilePhoto(instance= request.user.profile)
        C_form = AddContactInfo(instance = request.user.profile)
    return render(request, 'cafe/profile.html', {'title': 'Profile','Uform':U_form, 'Pform':P_form, 'Cform':C_form})
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


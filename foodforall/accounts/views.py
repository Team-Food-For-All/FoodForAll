from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import (
    RegistrationForm, 
    EditProfileForm, 
    EditProfilePhoto
)
from django.contrib.auth.models import User
# from accounts.models import UserProfile, User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.
# def home(request):
#     return render (request, 'home.html')

# def login(request):
#     return render (request, 'login.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = RegistrationForm()

        args = {'form': form}
        return render(request,'reg_form.html', args)
       
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request,'reg_form.html', args)
        
@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = { 'user': user}
    return render(request, 'profile.html', args)

# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#         profile_form = EditProfilePhoto(request.POST, instance=request.user.UserProfile)

#         if form.is_valid():
#             form.save()
#             profile_form.save()
#             return redirect('/account/profile')

#     else:
#         form = EditProfileForm(instance=request.user)
#         profile_form = EditProfilePhoto(instance=request.user)
#         args = {'form':form}
#         return render(request, 'edit_profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        u_form = EditProfileForm(request.POST,instance=request.user)
        p_form = EditProfilePhoto(request.POST, request.FILES, instance=request.user.userprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('/account/profile')
    else:
        u_form = EditProfileForm(instance=request.user)
        p_form = EditProfilePhoto(instance=request.user.userprofile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'edit_profile.html',context)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'change_password.html', args)



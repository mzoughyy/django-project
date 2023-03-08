from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib import messages
from .forms import UserRegisterForm,UserProfileForm,UserUpdateForm,UpdateProfileForm
from django.contrib.auth import logout
from django.contrib import auth
from django.views import View
from django.contrib.auth.models import User
from .models import profile
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required   
from django.views import generic
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.urls import reverse
from .utils  import send_sms

from django.conf import settings
from django.http import JsonResponse
from twilio.rest import Client

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile = UserProfileForm(request.POST,request.FILES)
        if form.is_valid() and profile.is_valid():
            user = form.save(commit=False)
            user.is_active = False # set is_active to False by default
            user.save()
            profil = profile.save(commit=False)
            profil.user = user
            profil.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile = UserProfileForm()
    return render(request, 'authentication/register.html', {'form':form, 'profile':profile})
class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request,"you've been logged out")
        return redirect('login')
@login_required
def profile_page(request):
    user_profile = request.user.profile
    return render(request, 'Resident/profile/profile.html', {'user_profile': user_profile})
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=UserUpdateForm(instance=request.user)
        profile=UpdateProfileForm(instance=request.user)
        args={'form':form,'profile':profile}
        return render(request, 'Resident/profile/profileEdit.html',args)


@staff_member_required
def send_sms_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        user_ids = request.POST.getlist('users')
        users = User.objects.filter(id__in=user_ids)
        send_sms(None, request, users, message)
        messages.success(request, "SMS sent successfully!")
        return redirect(reverse('admin:auth_user_changelist'))
    else:
        users = User.objects.all()
        return render(request, 'send_sms.html', {'users': users})

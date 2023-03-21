from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required   
from .models import contact
from authentication.models import profile
from django.contrib import messages
from .models import TravauxPAyment,SendMail
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

@login_required
def home(request):
    return render(request,'Resident/home.html')
def contactus(request):
    if request.method == 'POST':    
        cnt = contact()  # assuming you have a model named Contact
        cnt.user=request.user
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        cnt.subject = subject
        cnt.message = message
          # set the user field to the current user

        cnt.save()
        messages.success(request, 'Message envoyé avec succès')

    return render(request, 'Resident/contact/contact.html')

def profilePage(request):
    profile_list=profile.objects.all()
    return render(request,'Resident/profile/profile.html',{'profile_list':profile_list})


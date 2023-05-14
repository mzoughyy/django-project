from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required   
from .models import contact
from authentication.models import profile,Fournisseurs
from django.contrib import messages
from .models import TravauxPAyment,SendMail
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import Creditpayment
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from authentication.forms import EmailUs
from django.urls import reverse


from django.core.mail import send_mail, BadHeaderError

def send(request):
    if request.method == 'POST':
        mail = EmailUs(request.POST)
        if mail.is_valid():
            name = mail.cleaned_data['name']
            email = mail.cleaned_data['email']
            phone = mail.cleaned_data['phone']

            from_email = email  # use visitor's email as the sender
            recipient_list = ['smartlivingservice@gmail.com']

            try:
                send_mail(
                    subject='Client Request',  # set a subject for the email
                    message=f'Name: {name}\nEmail: {email} \nphone: {phone}',  # compose the message with the visitor's name and email
                    from_email=from_email,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
            except BadHeaderError:
                # handle the exception here
                return HttpResponse('Invalid header found.')
            return render(request,'homePage.html')
    else:
        mail = EmailUs()
    return render(request, 'homePage.html', {'mail': mail})

@login_required
def home(request):
    return render(request,'Resident/home.html')
def contactus(request):
    if request.method == 'POST':
        cnt = contact() 
        cnt.user=request.user
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        cnt.subject = subject
        cnt.message = message

        images = request.FILES.getlist('image')
        for image in images:
            cnt_image = contact.objects.create(user=request.user, subject=subject, message=message, image=image)
            cnt_image.save()     

        messages.success(request, 'Message envoyé avec succès')

    return render(request, 'Resident/contact/contact.html')

def profilePage(request):
    profile_list=profile.objects.all()
    return render(request,'Resident/profile/profile.html',{'profile_list':profile_list})
def travauxPage(request):
    travaux = Fournisseurs.objects.all().order_by('-date')    
    return render(request,'Resident/travaux/travaux.html', {'travaux': travaux})
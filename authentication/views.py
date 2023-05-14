from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib import messages
from .forms import UserRegisterForm,UserProfileForm,UserUpdateForm,UpdateProfileForm,EmailForm   
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
from Resident.models import TravauxPAyment,Creditpayment
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from cgi import print_arguments
from django.shortcuts import render, redirect
from .models import ChatMessage, profile
from .forms import ChatMessageForm
from django.http import JsonResponse
import json
from django.http import HttpResponseBadRequest
from django.db.models import Q

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
            messages.success(request, 'Account created successfully, Please wait for the admin to activate your account')
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
        profile = UpdateProfileForm(instance=request.user.profile, data=request.POST)

        if form.is_valid() and profile.is_valid():
            form.save()
            profile.save()
            return redirect('profile')
        else:
            error_message = "Please correct the following errors: " + str(form.errors) + str(profile.errors)
            return HttpResponseBadRequest(error_message)
    else:
        form=UserUpdateForm(instance=request.user)
        profile=UpdateProfileForm(instance=request.user.profile)
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
    
def send_mail_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                subject,
                message,
                'smartlivingservice@gmail.com',
                [user.email for user in User.objects.filter(is_active=True)],
                fail_silently=False
            )
            return redirect(reverse('admin:auth_user_changelist'))
    else:
        form = EmailForm()
    return render(request, 'admin/send_email.html', {'form': form})
def send_email_admin(request):
    return redirect('send_email')





def index(request):
    user = request.user.profile
    profiles = profile.objects.exclude(id=user.id)
    context = {"user": user, "profiles": profiles}
    return render(request, "mychatapp/index.html", context)


def detail(request, pk):
    selected_profile = profile.objects.get(id=pk)
    user = request.user.profile
    chats = ChatMessage.objects.filter(
        Q(msg_sender=user, msg_receiver=selected_profile) |
        Q(msg_sender=selected_profile, msg_receiver=user))
    rec_chats = chats.filter(msg_sender=selected_profile, seen=False)
    rec_chats.update(seen=True)
    form = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = selected_profile
            chat_message.save()
            return redirect("detail", pk=selected_profile.id)
    context = {"selected_profile": selected_profile, "form": form, "user": user, 
           "chats": chats, "num": rec_chats.count(), "recipient": selected_profile.user}

    return render(request, "mychatapp/detail.html", context)

import json

def sentMessages(request, pk):
    print(request.body) # Print the contents of the request body
    user = request.user.profile
    selected_profile = profile.objects.get(id=pk)
    data = json.loads(request.body)
    print(data) # Print the contents of the JSON object
    if "msg" not in data:
        return JsonResponse({"status": "error", "message": "Invalid data provided."})
    new_chat = data["msg"]
    new_chat_message = ChatMessage.objects.create(body=new_chat, msg_sender=user, msg_receiver=selected_profile, seen=False)
    return JsonResponse({"status": "success", "message": new_chat_message.body})
def receivedMessages(request, pk):
    user = request.user.profile
    selected_profile = profile.objects.get(id=pk)
    arr = []
    chats = ChatMessage.objects.filter(Q(msg_sender=selected_profile, msg_receiver=user) | Q(msg_sender=user, msg_receiver=selected_profile))
    for chat in chats:
        arr.append(chat.body)
    return JsonResponse(arr, safe=False)


def chatNotification(request):
    user = request.user.profile
    profiles = profile.objects.exclude(id=user.id)
    arr = []
    for profil in profiles:
        chats = ChatMessage.objects.filter(msg_sender=profil, msg_receiver=user, seen=False)
        arr.append(chats.count())
    return JsonResponse(arr, safe=False)


@login_required
def view_payments(request):
    user_profile = request.user.profile
    credit_payments = Creditpayment.objects.filter(profile=user_profile).order_by('-paid_at')
    travaux_payment = TravauxPAyment.objects.filter(profile=user_profile).order_by('-paid_at')

    context = {
        'credit_payments': credit_payments,
        'travaux_payment': travaux_payment,
    }

    return render(request, 'Resident/payment/payments.html', context)

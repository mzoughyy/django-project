from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from .models import profile,personel,Appartment
from .views import send_sms_view
from .utils import send_sms

def redirect_to_send_sms(modeladmin, request, queryset):
    url = reverse('send_sms')
    return redirect(url)

redirect_to_send_sms.short_description = "Send SMS to selected users"

class ProfileInline(admin.StackedInline):
    model = profile
    can_delete = False
    verbose_name_plural = 'Resident Data'


class CustomizedUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    actions = [redirect_to_send_sms]

class personelAdmin(admin.ModelAdmin):
    list_display = ('name', 'contart', 'congée')
class AppAdmin(admin.ModelAdmin):
    list_display = ('User', 'name','number')    
admin.site.register(Appartment,AppAdmin)
admin.site.register(personel, personelAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

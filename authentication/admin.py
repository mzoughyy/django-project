from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from .models import profile,personel,Appartment,Fournisseurs
from .views import send_sms_view
from .utils import send_sms
from django.utils.html import format_html
from .forms import EmailForm
def redirect_to_send_sms(modeladmin, request, queryset):
    url = reverse('send_sms')
    return redirect(url)

redirect_to_send_sms.short_description = "Send email to all users"
def redirect_to_send_email(modeladmin, request, queryset):
    url = reverse('send_email')
    return redirect(url)
redirect_to_send_email.acts_on_all = True
redirect_to_send_email.short_description = "Send email to selected users"
redirect_to_send_sms.short_description = "Send SMS to selected users"



class ProfileInline(admin.StackedInline):
    model = profile
    can_delete = False
    verbose_name_plural = 'Resident Data'

class CustomizedUserAdmin(UserAdmin):
    
    inlines = (ProfileInline,)
    actions = [redirect_to_send_sms,redirect_to_send_email]

    list_display = ('username','first_name','last_name', 'email', 'is_active')
    ordering = ('-is_active', 'username')  # Order by is_active field (active first)
    list_per_page = 10
    list_max_show_all = 20
    def changelist_view(self, request, extra_context=None):
        if not extra_context:
            extra_context = {}
        active_users = self.get_queryset(request).filter(is_active=True)
        inactive_users = self.get_queryset(request).filter(is_active=False)
        extra_context['active_users'] = active_users
        extra_context['inactive_users'] = inactive_users
        return super().changelist_view(request, extra_context=extra_context)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.select_related('profile')  # Optional: prefetch related data
        qs = qs.order_by('is_active')  # Order by is_active field (inactive first)
        return qs
class personelAdmin(admin.ModelAdmin):
    list_display = ('name', 'contrat', 'congée','date_joined')
    list_per_page = 10
    list_max_show_all = 20
class AppAdmin(admin.ModelAdmin):
    list_display = ('User', 'name','number')  
    list_per_page = 10
    list_max_show_all = 20
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.order_by('name','number')  # Order by is_active field (inactive first)
        return qs
class FourAdmin(admin.ModelAdmin):
    list_display = ('name', 'travaux_type','frais','contract')
    list_per_page = 10
    list_max_show_all = 20
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.order_by('-date')  # Order by is_active field (inactive first)
        return qs

admin.site.register(Fournisseurs,FourAdmin) 
admin.site.register(Appartment,AppAdmin)
admin.site.register(personel, personelAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

from django.contrib import admin
from .models  import contact,Creditpayment,TravauxPAyment
from django.utils.html import format_html

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('profile','payment','recu','paid_at','appartments')
    def appartments(self, obj):
        return obj.profile.appartment
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject','sent_at')
class TravPayAdmin(admin.ModelAdmin):
    list_display = ('profile','payment','recu','paid_at','traveaux')
admin.site.register(TravauxPAyment,TravPayAdmin)
admin.site.register(Creditpayment, PaymentAdmin)
admin.site.register(contact, ContactAdmin)
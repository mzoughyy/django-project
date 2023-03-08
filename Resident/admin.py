from django.contrib import admin
from .models  import contact,payment
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject')
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('profile','payment','recu','paid_at')
admin.site.register(payment, PaymentAdmin)
admin.site.register(contact, ContactAdmin)
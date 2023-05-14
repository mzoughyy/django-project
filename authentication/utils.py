from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

def send_sms(modeladmin, request, queryset, message):
    account_sid = 'xxx'
    auth_token = 'xx'
    client = Client(account_sid, auth_token)

    for user in queryset:
        # Get the profile associated with the user
        profile = user.profile

        # Add the '+' prefix to the phone number
        to_number = '+' + '216' + str(profile.phone)

        try:
            message = client.messages.create(
                body=message,
                from_='+xxxx',  # Replace with your Twilio number
                to=to_number
            )
            print(message.sid)
        except TwilioRestException as e:
            print(e)
            messages.error(request, f"Failed to send SMS to {to_number}: {e.msg}")

send_sms.short_description = "Send SMS to selected users"

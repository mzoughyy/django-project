from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from django.contrib import messages

def send_sms(modeladmin, request, queryset, message):
    account_sid = 'AC91dcce99836434151f6893f7f2e14890'
    auth_token = 'b2d29a941478abdf664325ff564d8804'
    client = Client(account_sid, auth_token)

    for user in queryset:
        # Get the profile associated with the user
        profile = user.profile

        # Add the '+' prefix to the phone number
        to_number = '+' + str(profile.phone)

        try:
            message = client.messages.create(
                body=message,
                from_='+12763294190',  # Replace with your Twilio number
                to=to_number
            )
            print(message.sid)
        except TwilioRestException as e:
            print(e)
            messages.error(request, f"Failed to send SMS to {to_number}: {e.msg}")

send_sms.short_description = "Send SMS to selected users"

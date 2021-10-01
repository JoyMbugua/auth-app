from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from twilio.rest import Client
from decouple import config
import pyotp
import base64

from .models import MagicLink

# set as env variables
account_sid = config('ACCOUNT_SID')
auth_token = config('AUTH_TOKEN')
client = Client(account_sid, auth_token)


def send_otp_mail(name,receiver, code, link):
    # Creating message subject and sender
    subject = 'Your login details'
    sender = config('EMAIL_HOST_USER')

    # passing in the context variables
    text_content = render_to_string('email/msg.txt',{"name": name, "code": code, "link": link})
    html_content = render_to_string('email/msg.html',{"name": name, "code": code, "link": link})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


def send_sms(user_code, phone_number):
    global client
    print("SENDING...")
    message = client.messages \
                .create(
                     body = f"Hey there! Your login verification code is {user_code}",
                     from_ = '+16154478531',
                     to = phone_number
                )
    print("SID",message.sid)


def send_operations(request, user):
        """
        general function to generate otp and magic links and send the sms or email to user
        """
    # generate otp code with username
        key = base64.b32encode(user.username.encode())
        hotp = pyotp.HOTP(key).at(user.counter)
        print("USER",user)
        # sending otp to phone signups
        if request.data.get('phone_number') is not None:
            phone = request.data['phone_number']
            send_sms(hotp, phone)
        else:
            if request.data.get('email') is not None:
                email = request.data['email']
                magiclink = MagicLink.objects.create(user=user, email=user.email, code=hotp)
                link = magiclink.generate_url(request)
                send_otp_mail(user.username, email, hotp, link)
        return
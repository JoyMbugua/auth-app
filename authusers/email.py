from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from decouple import config

def send_otp_mail(name,receiver, code):
    # Creating message subject and sender
    subject = 'Your login details'
    sender = config('EMAIL_HOST_USER')

    #passing in the context vairables
    text_content = render_to_string('email/msg.txt',{"name": name, "code": code})
    html_content = render_to_string('email/msg.html',{"name": name, "code": code})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()



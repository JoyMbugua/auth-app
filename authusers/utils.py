import os
from twilio.rest import Client
from decouple import config

# set as env variables
account_sid = config('ACCOUNT_SID')
auth_token = config('AUTH_TOKEN')
client = Client(account_sid, auth_token)

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
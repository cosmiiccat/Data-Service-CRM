# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

from . import MongoClient

TWILIO_ACCOUNT_SID = "AC798f77c5bd10d4f7b70c7d6c374eff3a"
TWILIO_AUTH_TOKEN = "07a544ff59dd346de0ae7e9c09143ca7"

def sms_message(text, customer_number):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=text,
            from_='+15105926655',
            to=customer_number
        )

    print(message.sid)

def sms_confirmation(response_id):
    response = MongoClient.find_one({"type": "response", "id": response_id})
    customer_id = response["customer-id"]
    customer = MongoClient.find_one({"type": "customer", "id": customer_id})
    customer_number = "+91" + customer["ph-no"]

    verification_msg = "Your response has been received"

    sms_message(verification_msg, customer_number)


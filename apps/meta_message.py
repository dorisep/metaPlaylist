# Download the helper library from https://www.twilio.com/docs/python/install
import os
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, contacts
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)
numbers_to_message = contacts
for number in numbers_to_message:
    message = client.messages \
                    .create(
                        body='''Week 27 scrape
                        
                        https://open.spotify.com/playlist/4Tdv6vMcqraqxpaRJpC7Pa?si=a59c6bd472994d1f

                        Reply STOP to unsubscribe.
                        ''',
                        from_='+16367336278',
                        to=number
                    )

print(message.sid)


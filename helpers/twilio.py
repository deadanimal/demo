from decouple import config
from twilio.rest import Client

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


def send_message(number, mesej):
    message = client.messages \
        .create(
            from_='whatsapp:+14155238886',
            body=mesej,
            to='whatsapp:+' + number
        )

    print(message.sid)
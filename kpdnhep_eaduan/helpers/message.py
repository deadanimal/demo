from decouple import config
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


def send_message(number, message):
    message = client.messages \
        .create(
            from_='whatsapp:+15005550006',
            body='Hi, Joe! Thanks for placing an order with us. We’ll let you know once your order has been processed and delivered. Your order number is O12235234',
            to='whatsapp:+14155238886'
        )

    print(message.sid)
import os
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.client = Client(account_sid, auth_token)

    def send_message(self,currency,price,departure,destination,date):
        message = self.client.messages.create(
            body=f"Low price alert! Only {currency} {price} to fly from {departure} to {destination}, on {date}",
            from_= "+17753643697",
            to=os.environ["TO"],
        )

        return message.body


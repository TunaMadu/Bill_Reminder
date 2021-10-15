from datetime import date
from twilio.rest import Client

# Replace the values inside ""  with your twilio phone number
twilio_number = "xxxxxxxxxxxxxxxx"

# Replace the values inside the "" with your phone number 
my_number = "xxxxxxxxxxx"

# Repalace the values inside the "" with twilio's account sid 
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Replace the values inside the "" with twilio's auth token
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)

# Will return the day of the month
todays_date = date.today().day

# Reminder dates
utility_bills = [15, 26]
car_payment = [10, 8]


for dates in utility_bills:

    if todays_date == dates:
        # This will create the text message
        message = client.messages \
            .create(
                # Message
                body="Utility bills are due soon!",
                to=my_number,
                from_=twilio_number
            )

for dates in car_payment:

    if todays_date == dates:
        # This will create a text message
        message = client.messages \
            .create(
                # Message
                body="Car payment is due soon",
                to=my_number,
                from_=twilio_number
            )

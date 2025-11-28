from twilio.rest import Client
ACCOUNT_SID ="enter sid"
AUTH_TOKEN = "enter token"
TWILIO_NUMMER= "enter twilio number"
RECIVER_NUMBER= "enter receiver number"
Client= Client(ACCOUNT_SID, AUTH_TOKEN)
message = Client.messages.create(body ="hello,ram i am sending to myself ", from_= TWILIO_NUMBER,to= RECIVER_NUMBER )
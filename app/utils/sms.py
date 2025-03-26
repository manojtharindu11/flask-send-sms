from flask import jsonify
from twilio.rest import Client
import os

# Twilio credentials
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(to_number,message_body):
    try:

        if not to_number or not message_body:
            return jsonify({'status': 'error', 'message': 'Please provide to number, message body'}), 400

        # sending sms
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )

        return jsonify({'status': 'success', 'message': message.sid})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
from twilio.rest import Client

def send_whatsapp_message():
    account_sid = 'AC579ab71b24af61e3263cb19eee3e7531'  # Your Account SID
    auth_token = 'c096283206184273647a66a7bad084e8'      # Your Auth Token
    client = Client(account_sid, auth_token)

    twilio_whatsapp_number = 'whatsapp:+14155238886'  # Your Twilio number
    recipient_whatsapp_number = 'whatsapp:+923069822189'  # Your number

    message_body = "Do your work at time and Don't waste your time that is a message from your Soul."

    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_whatsapp_number,
            to=recipient_whatsapp_number
        )
        print(f"Message sent! Message SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {str(e)}")

if __name__ == "__main__":
    send_whatsapp_message()

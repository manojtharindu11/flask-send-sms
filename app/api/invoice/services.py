from app.utils import sms

def sending_invoice_service(to_number,message_body):
    return sms.send_sms(to_number,message_body)

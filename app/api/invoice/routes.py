from flask import Blueprint, request, jsonify
from .services import sending_invoice_service

invoice_blueprint = Blueprint('invoice', __name__, url_prefix='/invoice')

@invoice_blueprint.route('/send_sms', methods=['POST'])
def sending_invoice():
    try:
        data = request.json
        to_number = data.get('to')
        message_body = data.get('message')

        if not to_number or not message_body:
            return jsonify({'status': 'error', 'message': 'Please provide to number, message body'}), 400

        return sending_invoice_service(to_number, message_body)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

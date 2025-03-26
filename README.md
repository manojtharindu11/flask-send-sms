# Flask SMS Sender with Twilio

This project is a simple Flask application that allows sending SMS messages using the Twilio API.

## 🚀 Features
- Send SMS messages via Twilio
- Simple Flask-based API
- Easy setup and configuration

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/manojtharindu11/flask-twilio-sms.git
   cd flask-twilio-sms
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Twilio credentials**
   - Sign up at [Twilio](https://www.twilio.com/)
   - Get your **Account SID**, **Auth Token**, and **Twilio Phone Number**
   - Create a `.env` file and add:
     ```ini
     TWILIO_ACCOUNT_SID=your_account_sid
     TWILIO_AUTH_TOKEN=your_auth_token
     TWILIO_PHONE_NUMBER=your_twilio_number
     ```

5. **Run the Flask application**
   ```bash
   flask run
   ```

6. **Send an SMS**  
   Use Postman or `curl` to send a request:  
   ```bash
   curl -X POST http://127.0.0.1:5000/send_sms -H "Content-Type: application/json" -d '{"to":"+94771234567", "message":"Hello from Flask!"}'
   ```

## 📜 API Endpoints
| Method | Endpoint      | Description      |
|--------|-------------|------------------|
| POST   | `/send_sms` | Send an SMS message |

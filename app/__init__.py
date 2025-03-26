from flask import Flask
from flask.logging import create_logger
app = Flask(__name__)
logger = create_logger(app)

def create_app():

    from app.api.invoice.routes import invoice_blueprint
    app.register_blueprint(invoice_blueprint)

    return app

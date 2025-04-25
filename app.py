from flask import Flask
from flask_cors import CORS
from api.click import click_bp
from api.order import order_bp
from api.export import export_bp

app = Flask(__name__)

# Thêm CORS cho tất cả routes
CORS(app)

# Register Blueprints
app.register_blueprint(click_bp, url_prefix="/api/click")
app.register_blueprint(order_bp, url_prefix="/api/order")
app.register_blueprint(export_bp, url_prefix="/api/export")

@app.route("/")
def index():
    return "Tracking API for muataiday.store is running."
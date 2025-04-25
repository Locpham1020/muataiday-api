from flask import Flask, request, jsonify
from flask_cors import CORS
from api.click import click_bp
from api.order import order_bp
from api.export import export_bp

app = Flask(__name__)

# Thêm CORS cho toàn bộ ứng dụng
CORS(app)

# Đăng ký các Blueprint
app.register_blueprint(click_bp, url_prefix="/api/click")
app.register_blueprint(order_bp, url_prefix="/api/order")
app.register_blueprint(export_bp, url_prefix="/api/export")

# Thêm CORS headers thủ công để đảm bảo
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

@app.route("/")
def index():
    return "Tracking API for muataiday.store is running."

# Xử lý OPTIONS requests cho toàn bộ ứng dụng
@app.route('/', defaults={'path': ''}, methods=['OPTIONS'])
@app.route('/<path:path>', methods=['OPTIONS'])
def options_handler(path):
    return jsonify({}), 200
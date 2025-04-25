from flask import Flask, request, jsonify, send_file
from api.click import click_bp
import os

app = Flask(__name__)
app.register_blueprint(click_bp, url_prefix="/api/click")

@app.route("/")
def index():
    return "Tracking API for muataiday.store is running."

@app.route("/view")
def view_clicks():
    return send_file("view_clicks.html")

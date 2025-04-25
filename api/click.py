from flask import Blueprint, request, jsonify
import json
import os
from datetime import datetime

click_bp = Blueprint("click", __name__)
DATA_FILE = "data/clicks.json"

@click_bp.route("/", methods=["POST"])
def log_click():
    data = request.get_json()
    data["timestamp"] = datetime.utcnow().isoformat()

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            records = json.load(f)
    else:
        records = []

    records.append(data)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

    return jsonify({"status": "success", "data": data}), 200

@click_bp.route("/", methods=["GET"])
def get_clicks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            records = json.load(f)
    else:
        records = []

    return jsonify(records)

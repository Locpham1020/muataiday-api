from flask import Blueprint, request, jsonify
import json
import os
from datetime import datetime

click_bp = Blueprint("click_bp", __name__)

@click_bp.route("/", methods=["POST", "OPTIONS"])
def log_click():
    # Handle preflight request
    if request.method == "OPTIONS":
        return "", 200
        
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No JSON data"}), 400

    # Đảm bảo thư mục tồn tại
    os.makedirs("airtable_data", exist_ok=True)
    
    file_path = "airtable_data/goiphubac_clicks.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            current = json.load(f)
    else:
        current = []

    data["timestamp"] = datetime.utcnow().isoformat()
    current.append(data)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(current, f, ensure_ascii=False, indent=2)

    return jsonify({"status": "success", "data": data})
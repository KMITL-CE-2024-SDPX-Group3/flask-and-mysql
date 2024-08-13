from flask import Blueprint, request, jsonify
from ..config.database import get_database_connection

playground_blueprint = Blueprint("playground", __name__, url_prefix="/playground")


@playground_blueprint.route("/test", methods=["POST"])
def handle_request():
    # Ensure data is provided
    if not request.data:
        return jsonify({"error": "No data provided"}), 400

    try:
        # Parse JSON data
        data = request.get_json()

        # Validate data (example: check if 'key' is in the data)
        if "key" not in data:
            return jsonify({"error": "'key' is required"}), 400

        # Process data
        # Example: Echo back the received data
        return jsonify({"status": "success", "received": data}), 200
    except Exception as e:
        # Handle JSON parsing errors
        return jsonify({"error": "Invalid JSON format"}), 400

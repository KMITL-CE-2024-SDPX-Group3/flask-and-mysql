from flask import Blueprint, request, jsonify
from ..config.database import get_database_connection
import mysql.connector

playground_blueprint = Blueprint("playground", __name__, url_prefix="/playground")


@playground_blueprint.route("/my-req", methods=["POST"])
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


@playground_blueprint.route("/")
def test_query():
    # get_database_names("localhost", "test-user", "test-password")
    hello("localhost", "test-user", "test-password")

    return "END TEST"


def get_database_names(host, user, password):
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host=host, user=user, password=password, database="ce_sdpx"
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the SQL query to get all database names
        cursor.execute("SHOW DATABASES")

        # Fetch all results
        databases = cursor.fetchall()

        # Extract database names from the results
        database_names = [db[0] for db in databases]

        if databases:
            print("Databases found:")
        for db in databases:
            print(db)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return "HELLO"


def hello(host, user, password):
    connection = mysql.connector.connect(
        host=host, user=user, password=password, database="ce_sdpx"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT DATABASE();")
    current_db = cursor.fetchone()
    print(f"Currently connected to database: {current_db[0]}")

from flask import Blueprint, request

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/all-user", methods=["GET"])
def get_all_user():
    return "test get all user 555555"


@users_blueprint.route("/user")
def get_user():
    user_id = request.args.get("user-id")
    return f"test get user${user_id}"

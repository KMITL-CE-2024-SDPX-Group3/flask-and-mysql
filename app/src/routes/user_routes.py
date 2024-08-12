from flask import Blueprint, request, jsonify
from ..config.database import get_database_connection
from ..dao.user_dao import UserDAO
from ..repository.user_repository import UserRepository
from ..models.user import User

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.route("/all-user", methods=["GET"])
def get_all_user():
    return "test get all user 555555"


@user_blueprint.route("/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    print(f"[GET] - enter {get_user.__name__}")
    connection = get_database_connection()
    user_dao = UserDAO(connection)
    user_repo = UserRepository(user_dao)
    user = user_repo.find_user(user_id)
    connection.close()

    if user:
        return jsonify({"id": user.id, "name": user.name, "age": user.age})

    return jsonify({"error": "User not found"}), 404


@user_blueprint.route("/", methods=["POST"])
def create_user():
    print(f"[CREATE] - enter {create_user.__name__}")
    data = request.json
    name = data.get("name")
    age = data.get("age")
    new_user = User(id=None, name=name, age=age)

    connection = get_database_connection()
    user_dao = UserDAO(connection)
    user_repo = UserRepository(user_dao)
    user_id = user_repo.add_user(new_user)
    connection.close()

    return jsonify({"id": user_id, "name": name, "age": age}), 201

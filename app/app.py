from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import Config
from db import mysql, init_db
from users import users_blueprint
from playground import playground_blueprint


app = Flask(__name__)
app.config.from_object(Config)
init_db(app)

# register blueprint
app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(playground_blueprint, url_prefix="/playground")


@app.route("/")
def hello():
    return "Hello World! - WOOOW"


@app.route("/config")
def show_config():
    config_values = {key: value for key, value in app.config.items()}
    return jsonify(config_values)


if __name__ == "__main__":
    app.run()

# Add comment: check mount volume

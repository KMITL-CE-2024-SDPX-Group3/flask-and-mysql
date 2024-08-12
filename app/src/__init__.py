from flask import Flask
from .routes.user_routes import user_blueprint
from .routes.playground_routes import playground_blueprint
from .config.init_db import initialize_database


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")
    # app.config.from_object("config.DevelopmentConfig")

    # Print configuration for debugging
    print(
        f"Database Configuration: {{'user': '{app.config['MYSQL_USER']}', 'password': '{app.config['MYSQL_PASSWORD']}', 'host': '{app.config['MYSQL_HOST']}', 'database': '{app.config['MYSQL_DB']}'}}"
    )

    # Initialize the database
    with app.app_context():
        initialize_database()

    # Register blueprints
    app.register_blueprint(user_blueprint)
    app.register_blueprint(playground_blueprint)
    return app

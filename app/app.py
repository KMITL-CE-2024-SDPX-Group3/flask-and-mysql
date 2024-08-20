import os
from src import create_app
from dotenv import load_dotenv


def check_environment():
    print("Checking environment")
    env_name = os.getenv("ENV_NAME")
    if env_name == "local":
        load_dotenv(".env.local")
    elif env_name == "dev":
        print("Development environment detected")


load_dotenv()
check_environment()


app = create_app()


@app.route("/")
def hello():
    return "Hello World! - WOOOW"


if __name__ == "__main__":
    print("Running app")
    app.run()

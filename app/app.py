from src import create_app
from dotenv import load_dotenv

app = create_app()
load_dotenv()


@app.route("/")
def hello():
    return "Hello World! - WOOOW"


if __name__ == "__main__":
    app.run()

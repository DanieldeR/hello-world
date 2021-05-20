from flask import Flask
from flask.blueprints import Blueprint

app = Flask(__name__)


@app.route("/")
def home_route():
    return "Hello World"


if __name__ == "__main__":
    app.run()

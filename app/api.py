from flask import Flask
from flask.blueprints import Blueprint

api_app = Blueprint("api", __name__)


@api_app.route("/")
def home_route():
    return "Hello World"


if __name__ == "__main__":
    api_app.run()

from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import api

    app.register_blueprint(api.api_app)
    app.add_url_rule("/", endpoint="index")

    return app

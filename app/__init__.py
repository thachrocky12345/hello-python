from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from app.controllers import register_blueprints
    register_blueprints(app)

    return app


if __name__ == "__main__":
    create_app()

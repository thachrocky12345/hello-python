from flask import Flask


def register_blueprints(app: Flask):
    from . import investors, main

    for controller in [investors, main]:
        app.register_blueprint(controller.bp)

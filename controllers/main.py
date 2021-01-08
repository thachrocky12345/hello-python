from flask import Blueprint, render_template
import json
bp = Blueprint('main', __name__)
from config import Config


@bp.route('/')
def index():
    return json.dumps({"result": "main",
                       "env": "{}-{}".format(Config.FLASK_ENV, Config.RABBITMQ_ROUTING_KEY)})

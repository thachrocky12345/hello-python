from flask import Blueprint, render_template
import json
bp = Blueprint('main', __name__)
from config import Config
#from logging_lib import logger

@bp.route('/')
def index():
    #logger.info(f"Raw Request: {request.dict()}")
    return json.dumps({"result": "main",
                       "env": "{}-{}".format(Config.FLASK_ENV, Config.RABBITMQ_ROUTING_KEY)})

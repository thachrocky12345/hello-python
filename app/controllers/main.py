from flask import Blueprint, render_template
import json
bp = Blueprint('main', __name__)



@bp.route('/')
def index():
    return json.dumps({"result": "main"})

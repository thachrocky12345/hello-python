from flask import Blueprint, request, render_template
import json

bp = Blueprint('investors', __name__, url_prefix='/investors')


@bp.route('/')
def index():
    raise ValueError("testing")

    return "investors"

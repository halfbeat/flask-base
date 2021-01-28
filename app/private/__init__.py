from flask import Blueprint

private_bp = Blueprint('private', __name__, template_folder='templates')

from . import routes
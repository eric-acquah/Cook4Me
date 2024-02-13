"""
Here is where the bluprint for the api is defined

"""

from flask import Blueprint


app_bp = Blueprint('app_bp', __name__, url_prefix='/api/v1')

from api.v1.resources.clients import *
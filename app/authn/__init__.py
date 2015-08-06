from flask import Blueprint
from app.authn import routes


def blueprint():
    _blueprint = Blueprint('authn', __name__)
    routes.register_routes(_blueprint)

    return _blueprint

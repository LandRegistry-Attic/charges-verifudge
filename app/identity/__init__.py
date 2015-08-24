from flask import Blueprint
from app.identity.routes import register_routes


def blueprint():
    _blueprint = Blueprint('identity', __name__)

    register_routes(_blueprint)

    return _blueprint

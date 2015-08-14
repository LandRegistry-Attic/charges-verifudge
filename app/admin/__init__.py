from flask import Blueprint


def blueprint():
    _blueprint = Blueprint('admin', __name__)
    return _blueprint

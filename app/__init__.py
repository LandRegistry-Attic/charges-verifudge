from flask import Flask
from flask.ext.script import Manager
from app import helloworld, static, admin
from govuk_template.flask import assets


def create_manager():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)

    static.register_assets(app)

    app.register_blueprint(helloworld.blueprint)
    app.register_blueprint(assets.govuk_template, url_prefix='/template')
    app.register_blueprint(admin.blueprint())

    return manager

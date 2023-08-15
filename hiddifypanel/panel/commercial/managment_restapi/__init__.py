from flask import Blueprint
from flask_restful import Api
from .manager import *
bp = Blueprint("management", __name__, url_prefix="/<proxy_path>/<user_secret>/api/manage/v1")
api = Api(bp)


def init_app(app):

    api.add_resource(Manager, "/test/")

    # with app.app_context():
    #     register_bot()
    app.register_blueprint(bp)

from flask import Flask, Blueprint
from app.config.config import config
from app.view.home import home
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    print("mode : " + str(config_name))
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # 跨域
    CORS(app)

    @app.route('/')
    def index():
        return 'This is index, ' + app.config['TYPE']

    def register_blueprints(app):
        """Register blueprints with the Flask application."""
        from app.myblog.api import myapi
        app.register_blueprint(myapi, url_prefix='/')

    def register_extensions(app):
        """Register extensions with the Flask application."""
        db.init_app(app)

    app.register_blueprint(home)

    register_blueprints(app)    # blueprint
    register_extensions(app)    # database
    return app
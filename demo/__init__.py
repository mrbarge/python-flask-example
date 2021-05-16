import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_table import Table, Col

# add DB
db = SQLAlchemy(engine_options={"pool_pre_ping": True})
migrate = Migrate()
metrics = None

def create_app():
    global metrics
    app = Flask(__name__)

    if app.config['ENV'] == 'production':
        app.config.from_object('config.ProductionConfig')
    elif app.config['ENV'] == 'test':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    if 'APP_CONFIG_FILE' in os.environ:
        app.config.from_envvar('APP_CONFIG_FILE')

    from demo.models import Thing

    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap = Bootstrap(app)

    with app.app_context():
        from demo.thing.thing import thing_bp
        # from demo.base import base_bp

        # add blueprints
        # app.register_blueprint(base_bp, url_prefix='/')
        app.register_blueprint(thing_bp, url_prefix='/thing')

        return app

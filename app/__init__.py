from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_oidc import OpenIDConnect
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
oidc = OpenIDConnect()
ma = Marshmallow()


def create_app(settings_module='config.local'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings_module)
    app.config.from_pyfile('config.py', silent=True)


    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.refresh_view = 'auth.relogin'

    db.init_app(app)
    migrate.init_app(app, db)
    oidc.init_app(app)

    # Registro de los Blueprints

    from .private import private_bp
    app.register_blueprint(private_bp)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)

    from .proyectos import proyectos_bp
    app.register_blueprint(proyectos_bp)

    from .api_v1_0 import api_v1_0_bp
    app.register_blueprint(api_v1_0_bp)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html', title = '404'), 404  

    @app.context_processor
    def inject_stage_and_region():
        return dict(nombreAplicacion="Gestor de aplicaciones", version="0.0.1")

    from datetime import timedelta
    from flask import session

    @app.before_request
    def make_session_permanent():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=1)

    return app

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_oidc import OpenIDConnect

login_manager = LoginManager()
db = SQLAlchemy()
oidc = OpenIDConnect()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:testing@localhost:5432/miniblog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.update({
        'TESTING': True,
        'DEBUG': True,
        'OIDC_CLIENT_SECRETS': 'client_secrets.json',
        'OIDC_ID_TOKEN_COOKIE_SECURE': False,
        'OIDC_REQUIRE_VERIFIED_EMAIL': False,
        'OIDC_USER_INFO_ENABLED': True,
        'OIDC_OPENID_REALM': 'flask-demo',
        'OIDC_SCOPES': ['openid', 'email', 'profile'],
        'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
        'OVERWRITE_REDIRECT_URI': 'http://localhost:5000/custom_callback'        
    })

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.refresh_view = 'auth.relogin'

    db.init_app(app)
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


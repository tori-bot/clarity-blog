from sys import prefix
from flask import Flask
from config import config_options
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES
from werkzeug import secure_filename,FileStorage


login_manager=LoginManager()
login_manager.session='strong'
login_manager.login_view='auth.login'

db=SQLAlchemy()
bootstrap=Bootstrap()
mail=Mail()
photos=UploadSet('photos',IMAGES)

def create_app(config_name):
    app=Flask(__name__)

    app.config.from_object(config_options[config_name])

    configure_uploads(app,photos)
    
    
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,prefix='authenticate')

    return app
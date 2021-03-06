import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    API_URL=os.environ.get('API_URL')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)
    # .replace("://", "ql://", 1)
    DEBUG=True

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://elvis:moraaelvis@localhost/blog'
    # DEBUG=True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elvis:moraaelvis@localhost/blog_test'

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
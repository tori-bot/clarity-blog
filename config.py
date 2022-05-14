import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://elvis:moraaelvis@localhost/blog'
    DEBUG=True


config_options={
    'development':DevConfig,
    'production':ProdConfig
}
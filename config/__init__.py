class Config(object):
    SECRET_KEY = 'secret_key'

    SQLALCHEMY_DATABASE_URI =  "postgresql://postgres:123456@localhost:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = 'jwt_secret_key'

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


configs = {"dev": DevelopmentConfig, "prod": ProductionConfig}
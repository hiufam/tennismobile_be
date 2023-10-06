from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

from config import DevelopmentConfig

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

jwt = JWTManager(app)
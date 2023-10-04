import sys
import os

from flask import Flask
from flask_jwt_extended import JWTManager

from api.controllers.registration import registration
from api.controllers.auth import auth
from api.controllers.verification import verification
from api.database import session
from api.models import User

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, PROJECT_PATH)

def create_app():
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = "secret"

    app.register_blueprint(registration)
    app.register_blueprint(auth)
    app.register_blueprint(verification)

    jwt = JWTManager(app)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        phone_number = jwt_data["sub"]
        return session.query(User).filter(User.phone_number == phone_number).scalar()

    app.run(debug=True)
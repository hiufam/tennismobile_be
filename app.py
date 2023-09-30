import sys
import os

from flask import Flask

from api.controllers.registration import registration
from api.controllers.auth import auth
from api.controllers.verification import verification

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, PROJECT_PATH)

def create_app():
    app = Flask(__name__)

    app.register_blueprint(registration)
    app.register_blueprint(auth)
    app.register_blueprint(verification)

    app.run(debug=True)
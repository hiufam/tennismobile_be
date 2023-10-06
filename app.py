from api import app, jwt
from api.controllers.registration import registration
from api.controllers.auth import auth
from api.controllers.verification import verification

app.register_blueprint(registration)
app.register_blueprint(auth)
app.register_blueprint(verification)
from api import app, jwt
from api.controllers.registration import registration
from api.controllers.auth import auth
from api.controllers.verification import verification
from api.controllers.images import images
from api.controllers.user_equipment import user_equipments

app.register_blueprint(registration)
app.register_blueprint(auth)
app.register_blueprint(verification)
app.register_blueprint(images)
app.register_blueprint(user_equipments)
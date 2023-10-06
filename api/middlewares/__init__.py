from api.database import session
from api.models import User
from api import jwt

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    phone_number = jwt_data["sub"]
    return session.query(User).filter(User.phone_number == phone_number).scalar()

from typing import Dict

from api.database import session
from api.models import User

def get_current_user(jwt_data : Dict):
    phone_number = jwt_data["sub"]
    
    return session.query(User).filter(User.phone_number == phone_number).scalar()
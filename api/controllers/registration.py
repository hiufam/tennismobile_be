from flask import Blueprint, request, jsonify

from ..models.user import User
from ..database import session

registration = Blueprint('registration', __name__, url_prefix='/api/registration')

@registration.post('/phone-number')
def register_phone_number():
    
    phone_number = request.json['phone_number']

    new_user = User()
    new_user.phone_number = phone_number

    session.add(new_user)
    session.commit()

    return jsonify({
        'user': {
            'phone_number': phone_number
        }
    }), 200
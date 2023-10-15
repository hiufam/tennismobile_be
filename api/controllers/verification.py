from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt

from ..middlewares import get_current_user
from ..models.user import User
from ..database import session

verification = Blueprint('verification', __name__, url_prefix='/api/verification')

@verification.post('/')
@jwt_required()
def verfiy_user_profile():
    user : User = get_current_user(get_jwt())

    avatar_id = request.json['image_id']
    full_name = request.json['full_name']
    date_of_birth = request.json['date_of_birth']
    gender = request.json['gender']
    singles_skill = request.json['singles_skill']
    doubles_skill = request.json['doubles_skill']

    user.avatar_id = avatar_id
    user.full_name = full_name
    user.date_of_birth = date_of_birth
    user.gender = gender
    user.singles_skill = singles_skill
    user.doubles_skill = doubles_skill

    session.commit()

    return jsonify({
        'user': {
            'phone_number': user.phone_number,
            'avatar_id': user.avatar_id,
            'full_name': user.full_name,
            'date_of_birth': user.date_of_birth,
            'gender': user.gender.name,
            'singles_skill': user.singles_skill,
            'doubles_skill': user.doubles_skill,
        }
    }), 200
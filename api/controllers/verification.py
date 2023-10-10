import base64, io, os
from uuid import uuid1

from flask import Blueprint, request, jsonify
from flask_jwt_extended import current_user, jwt_required
from PIL import Image
from sqlalchemy import null

from ..middlewares import user_lookup_callback
from ..models.user import User
from ..database import session

verification = Blueprint('verification', __name__, url_prefix='/api/verification')

@verification.post('/')
@jwt_required()
def verfiy_user_profile():
    user : User = current_user

    avatar_string = request.json['avatar'] # Must be encoded in base64
    full_name = request.json['full_name']
    date_of_birth = request.json['date_of_birth']
    gender = request.json['gender']
    singles_skill = request.json['singles_skill']
    doubles_skill = request.json['doubles_skill']

    if not avatar_string:
        return jsonify({
            'error': 'Avatar image not found'
        }), 400

    avatar_image = base64.b64decode(avatar_string)
    avatar = Image.open(io.BytesIO(avatar_image))

    if avatar.format not in ["JPG", "JPEG", "PNG"]: 
        return jsonify({
            'error': 'Invalid avatar image'
        }), 400

    if user.avatar: # Remove avatar if exist
        if os.path.exists(user.avatar):
            os.remove(user.avatar) 
        user.avatar = null
    
    avatar.thumbnail(size=(128, 128)) # Reside image, keep ratio
    avatar_name = uuid1()
    avatar_path = f'./avatars/{avatar_name}.{avatar.format.lower()}'
    
    avatar.save(avatar_path) 
    avatar.close()

    user.avatar = avatar_path # Add avatar path to user db
    user.full_name = full_name
    user.date_of_birth = date_of_birth
    user.gender = gender
    user.singles_skill = singles_skill
    user.doubles_skill = doubles_skill

    session.commit()

    return jsonify({
        'user': {
            'phone_number': user.phone_number,
            'avatar': user.avatar,
            'full_name': user.full_name,
            'date_of_birth': user.date_of_birth,
            'gender': user.gender.name,
            'singles_skill': user.singles_skill,
            'doubles_skill': user.doubles_skill,
        }
    }), 200
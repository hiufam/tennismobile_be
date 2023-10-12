import base64, io, os
from uuid import uuid1

from flask import Blueprint, request, jsonify
from flask_jwt_extended import current_user, jwt_required

from ..middlewares import user_lookup_callback
from ..models.user import User
from ..models.image import Image
from ..database import session

verification = Blueprint('verification', __name__, url_prefix='/api/verification')

@verification.post('/images') # might need seperation
@jwt_required()
def upload_image():
    user : User = current_user
    image_file = request.files['image'] #form-data

    if not Image.allowed_image(image_file.filename):
        return jsonify({
            'error': 'Invalid image file'
        }), 400

    image_base64 = base64.b64encode(image_file.read())

    new_image = Image(
        base64=image_base64
    )

    # check if user already have avatar
    if user.avatar_id:
        image_id = int(user.avatar_id)
        new_image = session.query(Image).filter(Image.id == image_id).scalar()

        new_image.base64 = image_base64

    else:
        session.add(new_image)
    
    session.commit()

    return jsonify({
        'image': {
            'image_id': new_image.id,
            'user_id': user.id,
        }
    }), 200

@verification.post('/')
@jwt_required()
def verfiy_user_profile():
    user : User = current_user

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
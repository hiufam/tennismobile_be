import base64, io, os
from uuid import uuid1

from flask import Blueprint, request, jsonify
from PIL import Image
from sqlalchemy import null

from ..models.user import User
from ..database import session

verification = Blueprint('verification', __name__, url_prefix='/api/verification')

@verification.post('/avatar')
def verify_avatar():
    phone_number = request.json['phone_number']
    user = User.find_user_by_phonenumber(phone_number)

    if not user:
        return jsonify({
            'error': 'User not found'
        }), 404
    
    avatar_string = request.json['avatar'] # Must be encoded in base64

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
            os.remove(user.avatar) 
            user.avatar = null
    
    avatar.thumbnail(size=(128, 128)) # Reside image, keep ratio
    avatar_name = uuid1()
    avatar_path = f'./avatars/{avatar_name}.{avatar.format.lower()}'
    
    avatar.save(avatar_path) 
    avatar.close()

    user.avatar = avatar_path # Add avatar path to user db
    session.commit()

    return jsonify(), 200

@verification.post('/full-name')
def verify_full_name():
    phone_number = request.json['phone_number']
    user = User.find_user_by_phonenumber(phone_number)

    if not user:
        return jsonify({
            'error': 'User not found'
        }), 404
    
    full_name = request.json['full_name']

    user.full_name = full_name
    session.commit()

    return jsonify({
        'user': {
            'phone_number': phone_number,
            'full_name': full_name
        }
    }), 200

@verification.post('/date-of-birth')
def verify_date_of_birth():
    phone_number = request.json['phone_number']
    user = User.find_user_by_phonenumber(phone_number)

    if not user:
        return jsonify({
            'error': 'User not found'
        }), 404
    
    date_of_birth = request.json['date_of_birth']
    user.date_of_birth = date_of_birth
    session.commit()

    return jsonify({
        'user': {
            'phone_number': phone_number,
            'date_of_birth': date_of_birth
        }
    }), 200

@verification.post('/gender')
def verify_gender():
    phone_number = request.json['phone_number']
    user = User.find_user_by_phonenumber(phone_number)

    if not user:
        return jsonify({
            'error': 'User not found'
        }), 404
    
    gender = request.json['gender']
    user.gender = gender
    session.commit()

    return jsonify({
        'user': {
            'phone_number': phone_number,
            'gender': gender
        }
    }), 200

@verification.post('/singles-skill')
def verify_singles_skill():
    phone_number = request.json['phone_number']
    user = User.find_user_by_phonenumber(phone_number)

    if not user:
        return jsonify({
            'error': 'User not found'
        }), 404
    
    singles_skill = request.json['singles_skill']
    user.singles_skill = singles_skill
    session.commit()

    return jsonify({
        'user': {
            'phone_number': phone_number,
            'singles_skill': singles_skill
        }
    }), 200

@verification.post('/doubles-skill')
def verify_doubles_skill():
    phone_number = request.json['phone_number']
    user = User.find_user_by_phonenumber(phone_number)

    if not user:
        return jsonify({
            'error': 'User not found'
        }), 404
    
    doubles_skill = request.json['doubles_skill']
    user.doubles_skill = doubles_skill
    session.commit()

    return jsonify({
        'user': {
            'phone_number': phone_number,
            'doubles_skill': doubles_skill
        }
    }), 200
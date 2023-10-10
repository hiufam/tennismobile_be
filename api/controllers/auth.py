from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from ..models.user import User
from ..database import session

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth.get('/otp/create')
def get_otp():
    phone_number = request.json['phone_number']

    user : User = session.query(User).filter(User.phone_number == phone_number).scalar()

    if not user:
        return jsonify(), 200

    user.generate_otp()
    
    return jsonify({
        'user': {
            'phone_number': user.phone_number,
            'registration_otp': user.registration_otp
        }
    }), 200


@auth.post('/otp/verify')
def verify_otp(): 
    otp_code = request.json['otp_code']
    phone_number = request.json['phone_number']
    
    user : User = session.query(User).filter(User.phone_number == phone_number).scalar()

    if not user:
        return jsonify({
            'error': 'Invalid OTP'
        }), 400

    if not user.have_valid_otp(otp_code):
        return jsonify({
            'error': 'Invalid OTP'
        }), 400
    
    access_token = create_access_token(identity=user.phone_number)

    user.is_verify = True
    session.commit()

    return jsonify({
        'user': {
            'phone_number': user.phone_number,
            'access_token': access_token,
        }
    }), 200
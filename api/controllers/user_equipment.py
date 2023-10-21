from flask import Blueprint, jsonify, request, session
from flask_jwt_extended import get_jwt, jwt_required

from ..middlewares import get_current_user
from ..database import session
from ..models.user_equipment import UserEquipment
from ..models.user import User

user_equipments = Blueprint('user_equipments', __name__, url_prefix='/api/equipments')

@user_equipments.post('/edit')
@jwt_required()
def edit_equipment():
    user : User = get_current_user(get_jwt())

    backhand = request.json['backhand']
    forehand = request.json['forehand']
    dominant_hand = request.json['dominant_hand']
    clothing_size = request.json['clothing_size']
    shoes_size = request.json['shoes_size']

    racket_brand_id = request.json['racket_brand_id']
    racket_parameter_id = request.json['racket_parameter_id']
    racket_string_id = request.json['racket_string_id']
    ball_brand_id = request.json['ball_brand_id']
    clothing_brand_id = request.json['clothing_brand_id']
    shoes_brand_id = request.json['shoes_brand_id']

    new_equipment = UserEquipment(
        user_id=user.id,
        racket_brand_id=racket_brand_id,
        racket_parameter_id=racket_parameter_id,
        racket_string_id=racket_string_id,
        backhand=backhand,
        forehand=forehand,
        dominant_hand=dominant_hand,
        ball_brand_id=ball_brand_id,
        clothing_brand_id=clothing_brand_id,
        clothing_size=clothing_size,
        shoes_brand_id=shoes_brand_id,
        shoes_size=shoes_size
    )

    user_equipment : UserEquipment = session.query(UserEquipment).filter(User.id == user.id).scalar()
    if (user_equipment is None):
        session.add(new_equipment)

    session.commit()

    return jsonify({
        'user_equipment': {
            'user_id': new_equipment.user_id,
            'racket_brand_id': new_equipment.racket_brand_id,
            'racket_parameter_id': new_equipment.racket_parameter_id,
            'racket_string_id': new_equipment.racket_string_id,   
            'backhand': new_equipment.backhand, 
            'forehand': new_equipment.forehand, 
            'dominant_hand': new_equipment.dominant_hand,        
            'ball_brand_id': new_equipment.ball_brand_id, 
            'clothing_brand_id': new_equipment.clothing_brand_id, 
            'clothing_size': new_equipment.clothing_size, 
            'shoes_brand_id': new_equipment.shoes_brand_id,
            'shoes_size': new_equipment.shoes_size,  
        }
    }), 200

@user_equipments.get('/get')
@jwt_required()
def get_equipment():
    user : User = get_current_user(get_jwt())
    equipment : UserEquipment = session.query(UserEquipment).filter(User.id == user.id).scalar()

    if (equipment is None):
        return jsonify({
            'error': 'User have no equipment'
        }), 400
    
    return jsonify({
        'equipment': {
            'user_id': equipment.user_id,
            'racket_brand_id': equipment.racket_brand_id,
            'racket_parameter_id': equipment.racket_parameter_id,
            'racket_string_id': equipment.racket_string_id,   
            'backhand': equipment.backhand.name, 
            'forehand': equipment.forehand.name, 
            'dominant_hand': equipment.dominant_hand.name,        
            'ball_brand_id': equipment.ball_brand_id, 
            'clothing_brand_id': equipment.clothing_brand_id, 
            'clothing_size': equipment.clothing_size.name, 
            'shoes_brand_id': equipment.shoes_brand_id,
            'shoes_size': equipment.shoes_size,  
        }
    }), 200

        
    
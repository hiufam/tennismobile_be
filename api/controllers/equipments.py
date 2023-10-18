from flask import Blueprint, jsonify, request, session
from flask_jwt_extended import get_jwt, jwt_required

from ..middlewares import get_current_user
from ..database import session
from ..models.equipment import Equipment
from ..models.user import User
from api.models import equipment

equipments = Blueprint('equipments', __name__, url_prefix='/api/equipments')

@equipments.post('/edit')
@jwt_required()
def edit_equipment():
    user : User = get_current_user(get_jwt())

    racket_brand = request.json['racket_brand']
    racket_parameter = request.json['racket_parameter']
    racket_string = request.json['racket_string']
    backhand = request.json['backhand']
    forehand = request.json['forehand']
    dominant_hand = request.json['dominant_hand']
    ball_brand = request.json['ball_brand']
    clothing_brand = request.json['clothing_brand']
    clothing_size = request.json['clothing_size']
    shoes_brand = request.json['shoes_brand']
    shoes_size = request.json['shoes_size']

    new_equipment = Equipment(
        user_id=user.id,
        racket_brand=racket_brand,
        racket_parameter=racket_parameter,
        racket_string=racket_string,
        backhand=backhand,
        forehand=forehand,
        dominant_hand=dominant_hand,
        ball_brand=ball_brand,
        clothing_brand=clothing_brand,
        clothing_size=clothing_size,
        shoes_brand=shoes_brand,
        shoes_size=shoes_size
    )

    user_equipment : Equipment = session.query(Equipment).filter(User.id == user.id).scalar()
    if (user_equipment is None):
        session.add(new_equipment)

    session.commit()

    return jsonify({
        'equipment': {
            'equipment_id': user_equipment.id,
            'user_id': new_equipment.user_id,
            'racket_brand': new_equipment.racket_brand,
            'racket_parameter': new_equipment.racket_parameter,
            'racket_string': new_equipment.racket_string,   
            'backhand': new_equipment.backhand, 
            'forehand': new_equipment.forehand, 
            'dominant_hand': new_equipment.dominant_hand,        
            'ball_brand': new_equipment.ball_brand, 
            'clothing_brand': new_equipment.clothing_brand, 
            'clothing_size': new_equipment.clothing_size, 
            'shoes_brand': new_equipment.shoes_brand,
            'shoes_size': new_equipment.shoes_size,  
        }
    }), 200

@equipments.get('/get')
@jwt_required()
def get_equipment():
    user : User = get_current_user(get_jwt())
    equipment : Equipment = session.query(Equipment).filter(User.id == user.id).scalar()

    if (equipment is None):
        return jsonify({
            'error': 'User have no equipment'
        }), 400
    
    return jsonify({
        'equipment': {
            'equipment_id': equipment.id,
            'user_id': equipment.user_id,
            'racket_brand': equipment.racket_brand,
            'racket_parameter': equipment.racket_parameter,
            'racket_string': equipment.racket_string,   
            'backhand': equipment.backhand, 
            'forehand': equipment.forehand, 
            'dominant_hand': equipment.dominant_hand,        
            'ball_brand': equipment.ball_brand, 
            'clothing_brand': equipment.clothing_brand, 
            'clothing_size': equipment.clothing_size, 
            'shoes_brand': equipment.shoes_brand,
            'shoes_size': equipment.shoes_size,  
        }
    }), 200

        
    
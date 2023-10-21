import enum

from sqlalchemy import Column, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.models import BaseModel
import api.models.master

class Backhand(enum.Enum):
    ONE_HANDED = 1
    TWO_HANDED = 2

class Forehand(enum.Enum):
    DOMINANT_HAND = 1
    NON_DOMINANT_HAND = 2

class DominatHand(enum.Enum):
    LEFT_HAND = 1
    RIGHT_HAND = 2

class ClothingSize(enum.Enum):
    XS = 1
    S = 2
    M = 3
    L = 4
    XL = 5
    XLL = 6

class UserEquipment(BaseModel):
    __tablename__ = 'user_equipments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    backhand = Column(Enum(Backhand))
    forehand = Column(Enum(Forehand))
    dominant_hand = Column(Enum(DominatHand))
    clothing_size = Column(Enum(ClothingSize))
    shoes_size = Column(Integer)

    racket_brand_id = Column(Integer)
    racket_parameter_id = Column(Integer)
    racket_string_id = Column(Integer)
    ball_brand_id = Column(Integer)
    clothing_brand_id = Column(Integer)
    shoes_brand_id = Column(Integer)
    
    user = relationship('User', back_populates='user_equipment')
    
    #TODO validation
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.models import BaseModel

class Equipment(BaseModel):
    __tablename__ = 'equipments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    racket_brand = Column(String)
    racket_parameter = Column(String)
    racket_string = Column(String)
    backhand = Column(String)
    forehand = Column(String)
    dominant_hand = Column(String)
    ball_brand = Column(String)
    clothing_brand = Column(String)
    clothing_size = Column(String)
    shoes_brand = Column(String)
    shoes_size = Column(String)
    
    # relationship
    user = relationship('User', back_populates='equipment')
    
    #TODO validation
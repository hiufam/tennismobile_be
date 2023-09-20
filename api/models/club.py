from sqlalchemy.orm import validates, relationship
from sqlalchemy import Column, Date, Integer, String, DateTime, Boolean

from ..models import BaseModel

class Club(BaseModel):
    __tablename__ ='clubs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)

    users = relationship('User', back_populates='club')

    def __repr__(self):
        return f'<Club:{self.name}>'
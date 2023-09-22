import datetime
import re
import random
import string

from sqlalchemy.orm import validates, relationship
from sqlalchemy import Column, Date, ForeignKey, Integer, String, DateTime, Boolean

from ..database import engine, session
from ..models import BaseModel

class User(BaseModel):
    __tablename__ ='users'

    id = Column(Integer, primary_key=True)
    phone_number = Column(Integer, nullable=False, unique=True)
    facebook_account = Column(String(50), nullable=True)
    google_account = Column(String(50), nullable=True)
    full_name = Column(String, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    singles_skill = Column(Integer, nullable=False, default=0)
    doubles_skill = Column(Integer, nullable=False, default=0)
    avatar = Column(String, nullable=True)
    club_id = Column(Integer, ForeignKey('clubs.id'))

    club = relationship('Club', back_populates='users')
    
    registration_otp = Column(String, nullable=True)
    registration_otp_expiration = Column(DateTime, nullable=True)
    is_verify = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<UserID={self.id}FullName={self.full_name}>'
    

    def generate_otp(self, digits=6):
        otp = ''
        for _ in range(digits):
            otp += random.choice(string.digits)

        self.registration_otp_expiration = datetime.datetime.now() + datetime.timedelta(seconds=1)
        self.registration_otp = otp

        session.commit()

        return otp
    
    def isValidOtp(self, otp_code):
        if self.registration_otp_expiration > datetime.datetime.now() and otp_code == self.registration_otp:
            return True

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if not phone_number:
            raise AssertionError('No phone number provided')

        if session.query(User).filter(User.phone_number == phone_number).scalar() is not None:
            print(type(User))
            raise AssertionError('Phone number has already been registered') 
        
        if not str(phone_number).isdigit():
            raise AssertionError('Phone number contains character')

        if len(str(phone_number)) != 10:
            raise ValueError('Phone number requires 10 digits') 
        
        return phone_number


    # @validates('facebook_account')
    # def validate_facebook_account(self, key, facebook_account):
    #     if not facebook_account:
    #         raise AssertionError('No facebook account provided')
        
    #     return facebook_account
    
    # @validates('google_account')
    # def validate_email(self, key, google_account):
    #     if not google_account:
    #         raise AssertionError('No google account provided')
        
    #     if not re.match("[^@]+@[^@]+\.[^@]+", google_account):
    #         raise AssertionError('Provided google account is not an google account address') 
        
    #     return google_account
    
    # @validates('full_name')
    # def validate_username(self, key, full_name):
    #     if not full_name or not len(full_name) > 0:
    #         raise AssertionError('No full_name provided')
        
    #     return full_name
        
    # @validates('date_of_birth')
    # def validate_date_of_birth(self, key, date_of_birth):
    #     if not date_of_birth:
    #         raise AssertionError('No date of birth provided')
        
    #     if type(date_of_birth) is str:
    #         date_of_birth = datetime.datetime.strptime(date_of_birth, "%m/%d/%Y").date()

    #     if date_of_birth > datetime.datetime.now().date():
    #         raise AssertionError("Date of birth cannot pass the next day")
        
    #     return date_of_birth

    # @validates('gender')
    # def validate_gender(self, key, gender):
    #     if not gender:
    #         raise AssertionError('No gender provided')
        
    #     if not gender == 'Male' or not gender == 'Female':
    #         raise ValueError('No such gender exist')
        
    #     return gender
        
    # @validates('singles_skill')
    # def validate_singles_skill(self, key, singles_skill):
    #     if not singles_skill:
    #         raise AssertionError('No singles skill provided')
        
    #     if singles_skill < 0 and singles_skill > 10:
    #         raise ValueError('Singles skill can only range from 0 to 10')
        
    #     return singles_skill
        
    # @validates('doubles_skill')
    # def validate_singles_skill(self, key, doubles_skill):
    #     if not doubles_skill:
    #         raise AssertionError('No doubles skill provided')
        
    #     if doubles_skill < 0 and doubles_skill > 10:
    #         raise ValueError('doubles skill can only range from 0 to 10')
        
    #     return doubles_skill
    
    # @validates('avatar')
    # def validate_avatar(self, key, avatar):
    #     if not avatar:
    #         raise AssertionError('No avatar provided')
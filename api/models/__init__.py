from sqlalchemy.orm import DeclarativeBase
from ..database import engine

class BaseModel(DeclarativeBase):
    pass

from .user import User
# from .club import Club
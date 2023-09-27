from sqlalchemy.orm import DeclarativeBase
from ..database import engine

class BaseModel(DeclarativeBase):
    pass

# Have to import in order to create table 
# And import first to avoid circular import
from .user import User
# from .club import Club

# Comment out to create table with alembic
# BaseModel.metadata.create_all(engine) 
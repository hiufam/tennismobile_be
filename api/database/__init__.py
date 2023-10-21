from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config

# Create database engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False)

# Create database session
Session = sessionmaker(bind=engine)
session = Session()
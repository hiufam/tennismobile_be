from sqlalchemy import Column, Integer, String

from api.models import BaseModel

IMAGE_EXTENSIONS = {'jpg', 'png', 'jpeg'}

class Image(BaseModel):
    __tablename__ ='images'

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)

    def __repr__(self):
        return f'<Image:{self.id}>'
    
    @staticmethod
    def allowed_image(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMAGE_EXTENSIONS

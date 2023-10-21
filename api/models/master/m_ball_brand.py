from sqlalchemy import Column, String, Integer

from ...models import BaseModel

class BallBrand(BaseModel):
    __tablename__ ='m_ball_brand'

    id = Column(Integer, primary_key=True)
    brand_name = Column(String, nullable=False)
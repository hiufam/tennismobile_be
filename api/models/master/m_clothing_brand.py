from sqlalchemy import Column, String, Integer

from ...models import BaseModel

class ClothingBrand(BaseModel):
    __tablename__ ='m_clothing_brand'

    id = Column(Integer, primary_key=True)
    brand_name = Column(String, nullable=False)
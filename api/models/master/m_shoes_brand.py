from sqlalchemy import Column, String, Integer

from ...models import BaseModel

class ShoesBrand(BaseModel):
    __tablename__ ='m_shoes_brand'

    id = Column(Integer, primary_key=True)
    brand_name = Column(String, nullable=False)
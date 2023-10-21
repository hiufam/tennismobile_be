from sqlalchemy import Column, String, Integer

from ...models import BaseModel

class RacketString(BaseModel):
    __tablename__ ='m_racket_string'

    id = Column(Integer, primary_key=True)
    brand_name = Column(String, nullable=False)
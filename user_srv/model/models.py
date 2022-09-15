from sqlalchemy import Column
from sqlalchemy import String, Integer
from db import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

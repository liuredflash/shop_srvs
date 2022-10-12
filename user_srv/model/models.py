from tabnanny import verbose
from sqlalchemy import Column
from sqlalchemy import String, Integer, Date, Text
from passlib.hash import pbkdf2_sha256
from db import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    mobile = Column(String(11), unique=True, nullable=False)
    _password = Column(String(100), name="password")
    nick_name = Column(String(20), nullable=True)
    head_url = Column(String(200), nullable=True)
    birthday = Column(Date, nullable=True)
    address = Column(String(200), nullable=True)
    desc = Column(Text, nullable=True)
    gender = Column(String(20), nullable=True)
    role = Column(Integer)

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = pbkdf2_sha256.hash(password)
    
    def verify_passwd(self, password):
        return pbkdf2_sha256.verify(password, self._password)

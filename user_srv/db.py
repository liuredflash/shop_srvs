from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base
from settings import settings
from sqlalchemy import create_engine

Base = declarative_base()
Session = scoped_session(sessionmaker()) #scoped_session会生成一个线程安全的session，并且会在线程中重复使用，要用remove彻底删去这个sessioon

def init_db(db_config):
    Session.remove()  # 先清除session，便于动态更新配置
    engine = create_engine(db_config)
    Session.configure(bind=engine)

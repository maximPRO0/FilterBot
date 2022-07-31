from sqlalchemy.orm import sessionmaker
from sqlalchemy import String, BigInteger, Column
from sqlalchemy import create_engine
from data import config
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine(config.POSTGRESURI)
Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    full_name = Column(String)
    username = Column(String, primary_key=True, unique=True)
    user_id = Column(BigInteger, unique=True)

class Worlds(Base):
    __tablename__ = 'Worlds'
    id =  Column(BigInteger, primary_key=True, autoincrement=True)
    word = Column(String, unique=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
    

# coding=utf-8
"""Help connect the database"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE_PATH = os.path.split(os.path.realpath(__file__))[0]
DB_CONNECT_STRING = 'sqlite:///'+ BASE_PATH +'/testDB.db'
BASE_DIR = BASE_PATH+'/'
if os.name == 'nt':
    DB_CONNECT_STRING = 'sqlite:///'+BASE_PATH+'\\testDB.db'
    BASE_DIR = BASE_PATH+'\\'
ENGINE = create_engine(DB_CONNECT_STRING, echo=True)
BaseModel = declarative_base()
def init_db():
    """Initilize the database

    """
    BaseModel.metadata.create_all(ENGINE)
    db_session = sessionmaker(bind=ENGINE)
    session = db_session()
    return session

def drop_db():
    """Drop all the tables

    """
    BaseModel.metadata.drop_all(ENGINE)



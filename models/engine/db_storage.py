#!/usr/bin/python3
"""This is our database storage engine
for the hbnb project
"""
from models.base_model import BaseModel
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import MySQLdb
import os

Base = declarative_base()

class DBStorage(BaseModel, Base):
    """ Schema/Class for our db storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Init method that setup a new engine"""
        USERNAME = os.getenv('HBNB_MYSQL_USER')
        PASSWORD = os.getenv('HBNB_MYSQL_PWD')
        DATABASE = os.getenv('HBNB_MYSQL_DB')
        HOST = os.getenv('HBNN_MYSQL_HOST')
        ENV_VAR = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USERNAME, PASSWORD, HOST, DATABASE), pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()


    def all(self, cls=None):



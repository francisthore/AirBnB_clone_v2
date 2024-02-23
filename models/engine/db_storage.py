#!/usr/bin/python3
"""This is our database storage engine
for the hbnb project
"""
from models.base_model import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
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


    def all(self, cls=None):
        """Perfoms query on db for all objects
        depending on cls name"""
        if cls:
            return self.__session.query(cls).all()
        else:
            return self.__session.query(self.__engine.table_names()).all()

    def new(self, obj):
        """Adds the object to the current db"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from current db"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """Creates all tables in the db"""
        from models.city import City
        from models.state import State

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        



#!/usr/bin/python3
"""This is our database storage engine
for the hbnb project
"""
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """ Schema/Class for our db storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Init method that setup a new engine"""
        USERNAME = os.getenv('HBNB_MYSQL_USER')
        PASSWORD = os.getenv('HBNB_MYSQL_PWD')
        DATABASE = os.getenv('HBNB_MYSQL_DB')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        ENV_VAR = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USERNAME,
                                             PASSWORD,
                                             HOST,
                                             DATABASE),
                                      pool_pre_ping=True)
        if ENV_VAR == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Perfoms query on db for all objects
        depending on cls name"""
        res_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query_res = self.__session.query(cls).all()
            for item in query_res:
                if hasattr(item, 'id'):
                    key = "{}.{}".format(item.__class__.__name__,
                                         item.id)
                    res_dict[key] = item
        return res_dict

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
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes session"""
        self.__session.close()

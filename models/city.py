#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__= 'cities'
    state_id = Column(String(60), nullable=False,foreign_key= True )
    name = Column(String(128), nullable= False)

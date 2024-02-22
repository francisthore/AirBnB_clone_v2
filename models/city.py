#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__= 'cities'
    name = Column(String(128), nullable= False)
    state_id = Column(String(60), nullable=False, foreign_key=True )
    state = relationship("State", back_populates="cities")

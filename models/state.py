#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base, relationship

from models.engine.file_storage import FileStorage

Base = declarative_base()

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable= False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """Getter for the states cities"""
        return [city for city in State.cities if city.state_id == State.id]

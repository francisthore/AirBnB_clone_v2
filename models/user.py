#!/usr/bin/python3
"""User model for our AirBnB Clone
Project"""

from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Defines the model User"""

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref='user',
                          cascade='all, delete, delete-orphan')
    reviews = relationship("Review", backref='user',
                           cascade="all, delete, delete-orphan")

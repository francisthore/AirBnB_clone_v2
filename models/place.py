#!/usr/bin/python3
"""Place model for our AirBnB Clone
Project"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv


class Place(BaseModel, Base):
    """Class definition for a place model"""
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = relationship("Review", backref='place',
                           cascade="all, delete, delete-orphan")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Getter for reviews"""
            from models import storage
            return [review for review in storage.all(Review).values()
                    if review.place_id == self.id]

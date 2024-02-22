#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

from models.engine.file_storage import FileStorage

Base = declarative_base()

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable= False)

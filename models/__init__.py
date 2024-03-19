#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
and DBStorage"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()

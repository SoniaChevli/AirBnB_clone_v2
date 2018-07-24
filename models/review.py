#!/usr/bin/python3
'''
    Implementation of the Review class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    place_id = ""
    user_id = ""
    text = ""

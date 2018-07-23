#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class State(BaseModel):
    '''
        Implementation for the State.
    '''
    name = Column(String(128), nullable=False)
    __table_name__ = "states"

    #come back and add DBStorage and FileStorage 
    #things
    


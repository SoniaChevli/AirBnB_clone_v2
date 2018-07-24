#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import os
from models import storage
from models.city import City


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __table_name__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            a = []
            for i in storage.all(City).values():
                if i.state_id == self.id:
                    a.append(i)
            return a
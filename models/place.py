#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table('place_amenity', Base.metadata, Column("place_id", String(60), ForeignKey('places.id'), nullable=False), Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False))

class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []


    #should this be wrapped in an if see end of number 9??
    if os.getenv("HBNB_TYPE_STORAGE")  == 'db':
        reviews = relationship("Review", cascade='all, delete', backref='place')
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    else:
        @property
        def reviews(self):
            from models import storage
            nl = []
            for i in storage.all(Review).values():
                if i.place_id == self.id:
                    nl.append(i)
            return nl
        
        @property
        def amenities(self):
            a = []
            from models import storage
            objs = storage.all(Amenity)
            for i in objs:
                if i.id in amenity_ids:
                    a.append(i)
            return a

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
                
                
            





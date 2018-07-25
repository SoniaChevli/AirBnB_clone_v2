#!/usr/bin/python3
'''
Testing the db_storage module.
'''

import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel, Base
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.review import Review
import os

@unittest.skipIf(os.getenv('HBNB_HBNB_TYPE_STORAGE' != "db"))

class testDBStorage(unittest.TestCase):
    '''
    Testing the DBStorage class
    '''
    def test_user(self):
        ''' testing if user was properly created '''
        new_user = User(email="sc@hbtn.io",
                        password="sccpwd",
                        first_name="Sonia",
                        last_name="Chevli")
        new_user.save()
        self.assertTrue(new_user.email, "sc@hbtn.io")
        self.assertTrue(new_user.password, "sccpwd")
        self.assertTrue(new_user.first_name, "Sonia")
        self.assertTrue(new_user.last_name, "Chevli")


    def test_state(self):
        ''' testing state '''
        new_state = State(name="New York")
        new_state.save()
        self.assertTrue(new_state.name, "New York")


    def test_city(self):
        ''' testing city '''
        new_city = City(name="Buffalo")
        new_city.save()
        self.assertTrue(new_city.name, "Buffalo")

    def test_amenity(self):
        ''' testing amenity '''
        new_amenity = Amenity(name="Air Conditiioning")
        new_amenity.save()
        self.assertTrue(new_amenity.name, "Air Conditioning")

    def test_place(self):
        ''' testing place '''
        new_place = Place(name="Lovely_place")
        new_place.save()
        self.assertTrue(new_place.name, "Lovely_place")

    def test_review(self):
        ''' testing review '''
        new_review = Review(text="Great")
        new_review.save()
        self.assertTrue(new_review.text, "Great")


from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
import os
import models
from models import State, User, Review, Place, City, Amenity
class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        #change to environmental variables
        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB"),
        pool_pre_ping=True)
        Base.metadata.create_all(self.__engine) #maybe not necessary?
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        "query the current db for all objects depending on cls type"
        a = {}
        if cls:
        for i in self.__session.query(cls).all():
            a["{}.{}".format(i.__class__.__name__, i.id)] = i
        else:
            for i in self.__session(User, State, City, Amenity, Place, Review).all():
            a["{}.{}".format(i.__class__.__name__, i.id)] = i
        return a
    
    def new(self, obj):
        "add the object to the current database session"
        self.__session.add(obj)
    
    def save(self):
        "commit all changes of the current db session"
        self.__session.commit()
    
    def delete(self, obj=None):
        "delete obj from the current db session if not none"
        if obj:
            cls = models.classes[obj.__class__.__name__]
            query = self.__session.query(cls).filter(cls.id == obj.id).first()
            query.delete(synchronize_session=False)
    
    def reload(self):
        "create all tables in the db"




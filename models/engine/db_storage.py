#!/usr/bin/python3


"""Database storage"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """Class Db storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage instance"""
        self.__engine = create_engine('mysql+mysqldb://user:pwd@localhost/db_name', pool_pre_ping=True)
        self.reload()

    def all(self, cls=None):
        """Query all objects of a given class or all classes"""
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(User).all()
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(State).all())
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Review).all())
        return {obj.to_dict()['__class__'] + '.' + obj.id: obj for obj in objs}

    def new(self, obj):
        """Add a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.remove()

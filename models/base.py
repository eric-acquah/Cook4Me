"""
This module defines the base class for all created classes
 
"""

from datetime import datetime
from importlib import import_module
from uuid import uuid4

class BaseModel:
    """
    Defines common basic methods and attributes
    of all classes

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes all object instances with basic attributes

        Args:
            args (tuple): takes in a variable lenght of initialization details
            kwargs (dict): represents key-value pairs for recreating instances
                            from already existing ones.

        """
        
        if kwargs:
            # Recreate an object from a dictionary representation of that object
            for key in kwargs:
                if key != "__class__": # recreate all except this attribute

                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(kwargs.get(key),
                         "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = kwargs.get(key)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    
    def __str__(self):
        # Returns descriptive info of the instance
        
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    

    def dictify(self):
        """
        Converts instances into dictionary representation

        Return:
            dictionary representation of object

        """

        clone = self.__dict__.copy()
        clone['__class__'] = self.__class__.__name__

        # convert datetime object into string format
        if isinstance(clone['updated_at'], datetime) and isinstance(
            clone['created_at'], datetime):
            clone['updated_at'] = clone['updated_at'].isoformat()
            clone['created_at'] = clone['created_at'].isoformat()

        return clone
    
    
    def save(self, db=False):
        """
        Save object to memory or database

        Return:
            True if successful else return False

        """
        storage = import_module("__init__", package="Cook4Me")
        storage = storage.storage

        if db is True: #  load object to database
            stats = storage.load(self, todb=True)

        else:
            stats = storage.load(self) #  load object to memory only

        return stats
    
    def fetch(self, fetch_id=None):
        """
        Retrive data from database

        Args:
            fetch_id (str): id of object if querying for specific object 

        Return:
            Document if a specific object id is specified.
            Else return all documents within a database collection
            with the name of collection equal to the classname
            of the object.
        """
        storage = import_module("__init__", package="Cook4Me")
        storage = storage.storage

        if fetch_id is not None:
            found = storage.reload(self, fetch_id)

        else:
            found = storage.reload(self)

        return found
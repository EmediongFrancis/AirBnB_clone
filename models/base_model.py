#!/usr/bin/python3

"""
    Base class that defines common attributes/methods
    for other classes.
"""
from datetime import datetime
import uuid



class BaseModel:
    """
        Definition of Basemodel class.
    """
    def __init__(self):
        """
            Initializes an instance of BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

       
    def __str__(self):
        """
            Prints a string representation of the
            class name, id, and dictionary.
        """
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
            Updates the public instance attribute `updated_at` with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values 
            of __dict__ of the instance.
        """
        myDict = dict(self.__dict__)
        myDict["__class__"] = self.__class__.__name__
        myDict["created_at"] = self.created_at.isoformat()
        myDict["updated_at"] = self.updated_at.isoformat()
        return myDict

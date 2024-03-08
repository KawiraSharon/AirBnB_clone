#!/usr/bin/python3
"""Definition of class BaseModel"""

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """BaseModel that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """constructor"""

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs):
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            #TODO: solve
            return

    def __str__(self):
        """__str__"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dictObjects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dictObjects[key] = value.isoformat()
            else:
                dictObjects[key] = value
            dictObjects["__class__"] = self.__class__.__name__
            return dictObjects

        
    

#!/usr/bin/python3
"""import required modules"""
from datetime import datetime, date
from uuid import uuid4
import models


class BaseModel:
    """class that defines all common attributes and methods"""

    def __init__(self):
        """initialization of instance attributes
            Args:
                id - user id
                created_at - time instance is created
                uodated_at - time an instance is updated
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """prints the name of the class, id and dict"""
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated at with current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionart containing all key, values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

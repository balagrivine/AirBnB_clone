#!/usr/bin/python3
"""import required libraries"""
import json


class FileStorage:
    """class that seializes and deserializes instances to and from JSON"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """initialization of attributes"""
    
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with <obj class name>.id
            Args:
                obj: object to be added
        """
        class_name =obj.__class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        obj_dict = {}
        for key, value in self.__objects.items():
            dict_val = value.to_dict()
            obj_dict.update({key: dict_val})
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
            deserializes the JSON file to __objects
            only if the JSON file exists.
            otherwise do nithing"""
        try:
            with open(self.__file_path, "r") as file:
                obj_elem = json.load(file)
                for key, value in obj_elem.items():
                    clas = value["__class__"]
                    clas = eval(clas)
                    self.new(clas(**value))
        except FileNotFoundError:
            pass

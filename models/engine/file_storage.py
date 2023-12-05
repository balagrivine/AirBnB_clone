#!/usr/bin/python3
"""import required libraries"""
import json
import os.path


class FileStorage:
    """class that seializes and deserializes instances to and from JSON"""

    __file_path = "file.json"
    __objects = {}
    
    def __init__(self):
        """instantiation of public instance attributes"""
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with <obj class name>.id
            Args:
                obj: object to be added
        """
        class_name = __class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
            deserializes the JSON file to __objects
            only if the JSON file exists.
            otherwise do nithing"""
        try:
            with open (self.__file_path, "r") as file:
                file_cont = file.read()
                if file_cont:
                    obj_dict = json.loads(file_cont)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split(".")
                        self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass

#!/usr/bin/python3
"""import required libraries"""
import json
import os.path


class FileStorage:
    """class that seializes and deserializes instances to and from JSON"""

    '''directory_path = "models"
    file_name = "file.json"
    __file_path = os.path.join(directory_path, file_name)'''
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
        class_name = __class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
            deserializes the JSON file to __objects
            only if the JSON file exists.
            otherwise do nithing"""
        if os.path.exists(self.__file_path) is True:
            with open (self.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_elem = json.load(file)
                    for key, value in obj_elem.items():
                        class_name, obj_id = key.split(".")
                        self.__objects[key] = globals()[class_name](**value)
                except json.JSONDecodeError as e:
                    print("Error decoding JSON file {}" .format(e))
        """print("Path does not exist")"""

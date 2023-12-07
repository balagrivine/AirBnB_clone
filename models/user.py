#!/usr/bin/python3
"""import required modules"""


from models.base_model import BaseModel

class User(BaseModel):
    """instantiation of class attributes"""
    email = str(" ")
    password = str(" ")
    first_name = str(" ")
    last_name = str(" ")

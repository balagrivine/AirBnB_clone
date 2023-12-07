#!/usr/bin/python3
"""import required modules"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """class definition for our line-oriented interpreter"""

    prompt = "(hbnb)"
    clslist = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
            }

    def do_EOF(self, text):
        """Quit command to exit the program
        """
        return True
    def emptyline(self):
        """This command does not execute anything when an empty line is passed"""
        pass

    do_quit = do_EOF

    def do_create(self, class_name):
        """Creates a  new instance of BseModel, saves it
            to JSON file and prints the id
        """
        if not class_name:
            print('** class name missing **')
        if class_name not in self.clslist:
            print("** class doesn\'t exist **")
        base_model = BaseModel(self)
        base_model.save()

    def do_show(self, arg):
        """Prints the string rep of an instance
        based on the class name and id
        """
        class_name, obj_id = None, None
        args = arg.split(" ")
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if not class_name:
            print("** class name missing **")
        elif not obj_id:
            print("** instance id missing **")
        else:
            k = class_name + "." + obj_id
            obj = models.storage.all().get(k)
            if not obj:
                print("** no instance found **")
            else:
                print(obj)

if __name__ == "__main__":
    HBNBCommand().cmdloop()

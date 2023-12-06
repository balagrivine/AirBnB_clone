#!/usr/bin/python3
"""import required modules"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """class definition for our line-oriented interpreter"""

    prompt = "(hbnb)"
    class_list = {
    "BaseModel": BaseModel,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
    "User": User}

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
        elif class_name not in self.class_list:
            print('** class name does\'t exist **')
        else:
            obj = self.class_list[class_name]()
            models.storage.save()
            print(obj.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

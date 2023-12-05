#!/usr/bin/python3
"""import required modules"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class definition for our line-oriented interpreter"""

    prompt = "(hbnb)"

    def do_EOF(self, text):
        """Quit command to exit the program
        """
        return True
    def emptyline(self):
        """This command does not execute anything when an empty line is passed"""
        pass

    do_quit = do_EOF

if __name__ == "__main__":
    HBNBCommand().cmdloop()

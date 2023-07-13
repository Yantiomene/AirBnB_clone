#!/usr/bin/python3
"""Console Program for command interpreter
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command line class"""
    prompt = '(hbnb)'

    classes = {
            "BaseModel": BaseModel}

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0 or arg is None:
            print("** class name missing **")
        else:
            if len(args) == 1 and args[0] in self.classes:
                created_instance = self.classes.get(args[0])()
                print(create_instance.id)
            else:
                print("** class doesn't exist **")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """No command received"""
        return False

    def do_EOF(self, line):
        """End of file and close"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

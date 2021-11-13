#!/usr/bin/python3
"""
Building a command interpreter.
"""

from models.base_model import BaseModel
from models import storage
import cmd
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB console.
    """
    prompt = "(hbnb)"
#     intro = '''
#     |+------------------------------------------------------+|
#     |                                                        |
#     | Welcome to Collins & Francis' HBNB Console!            |
#     | Enter 'help' to see a list of commands.                |
#     |                                                        |
#     |+------------------------------------------------------+|
#     |                                                        |
#     |                                                        |
#    '''

    classes = {"BaseModel", "User", "State", "City", "Amenity", "Place"}

    def do_quit(self, line):
        """Quit command to exit the program."""
        raise SystemExit

    def do_EOF(self, line):
        """Exit with Ctrl-D."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, line):
        """
            Creates a new instance of BaseModel, saves it
            to disk, and prints the id.
            Usage: create <class name>
        """
        if not line:
            print("** class name missing **")
        else:
            if line in HBNBCommand.classes:
                new_instance = HBNBCommand.classes[line]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
            Prints the string representation of an instance
            based on the class name and id.
            Usage: show <class name> <id>
        """
        clargs = line.split()
        if len(clargs) == 0:
            print("** class name missing **")
        elif clargs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(clargs) == 1:
            print("** instance id missing **")
        else:
            key_id = "{}.{}".format(clargs[0], clargs[1])
            try:
                print(storage.all()[key_id])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """
            Deletes an instance based on the class name and id.
            Usage: destroy <class name> <id>
        """
        clargs = line.split()
        if len(clargs) == 0:
            print("** class name missing **")
        elif clargs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(clargs) == 1:
            print("** instance id missing **")
        else:
            key_id = "{}.{}".format(clargs[0], clargs[1])
            try:
                del storage.all()[key_id]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """
            Prints string representations of all instances
            based or not based on the class name.
            Usage: all <class name>
        """
        clargs = line.split()
        new_list = []
        if len(clargs) == 1:
            if clargs[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for key in storage.all().keys():
                    name = key.split(".")
                    if name[0] == clargs[0]:
                        new_list.append(storage.all()[key])
                    else:
                        continue
                print(new_list)
        else:
            for key, value in storage.all().items():
                new_list.append(str(storage.all()[key]))
            print(new_list)

    def do_update(self, line):
        """
            Updates an instance based on the class name and id
            by adding or updating attribute.
            Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        clargs = shlex.split(line)
        storage.reload()
        nova_dict = storage.all()
        if len(clargs) == 0:
            print("** class name missing **")
        elif clargs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(clargs) == 1:
            print("** instance id missing **")
        elif clargs[0] + "." + clargs[1] not in nova_dict.keys():
            print("** no instance found **")
        elif len(clargs) == 2:
            print("** attribute name missing **")
        elif len(clargs) == 3:
            print("** value missing **")
        else:
            key_id = "{}.{}".format(clargs[0], clargs[1])
            if hasattr(nova_dict[key_id], clargs[2]):
                binder = type(getattr(nova_dict[key_id], clargs[2]))
                setattr(nova_dict[key_id], clargs[2], binder(clargs[3]))
                storage.save()
            else:
                setattr(nova_dict[key_id], clargs[2], clargs[3])
                storage.save()   

    def do_help(self, line):
        """
            Get help on commands.
            Usage: help <command>
        """
        cmd.Cmd.do_help(self, line)


# def parse(line):
#    """Helper method to parse user-typed input."""
#   return tuple(line.split())


if __name__ == "__main__":
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""
Building a command interpreter.
"""
import shlex
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB console.
    """
    prompt = "(hbnb) "
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

    classes = {"BaseModel": BaseModel, "User": User, "State": State,
    "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

    def do_quit(self, line):
        """Quit command to exit the program."""
        raise SystemExit

    def do_EOF(self, line):
        """Exit with Ctrl-D."""
        return True

    def do_help(self, line):
        """
            Get help on commands.
            Usage: help <command>
        """
        cmd.Cmd.do_help(self, line)

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
            if line in HBNBCommand.classes.keys():
                new_instance = eval(line)()
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
        elif clargs[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(clargs) == 1:
            print("** instance id missing **")
        else:
            key_id = "{}.{}".format(clargs[0], clargs[1])
            try:
                print(models.storage.all()[key_id])
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
        elif clargs[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(clargs) == 1:
            print("** instance id missing **")
        else:
            key_id = "{}.{}".format(clargs[0], clargs[1])
            try:
                del models.storage.all()[key_id]
                models.storage.save()
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
            if clargs[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                for key in models.storage.all().keys():
                    name = key.split(".")
                    if name[0] == clargs[0]:
                        new_list.append(str(models.storage.all()[key]))
                    else:
                        continue
                print(new_list)
        else:
            for key, value in models.storage.all().items():
                new_list.append(str(models.storage.all()[key]))
            print(new_list)

    def do_update(self, line):
        """
            Updates an instance based on the class name and id
            by adding or updating attribute.
            Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        clargs = shlex.split(line)
        models.storage.reload()
        nova_dict = models.storage.all()
        if len(clargs) == 0:
            print("** class name missing **")
        elif clargs[0] not in HBNBCommand.classes.keys():
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
                models.storage.save()
            else:
                setattr(nova_dict[key_id], clargs[2], clargs[3])
                models.storage.save()   

        

    def parse(line):
        """Helper method to parse user-typed input."""
        return tuple(line.split())


if __name__ == "__main__":
    HBNBCommand().cmdloop()

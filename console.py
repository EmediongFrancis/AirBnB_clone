#!/usr/bin/python3
"""
Building a command interpreter.
"""

from models.base_model import BaseModel
from models import storage
import cmd
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB console.
    """
    prompt = "(hbnb) "
    intro = '''
    |+------------------------------------------------------+|
    |                                                        |
    | Welcome to Collins & Francis' HBNB Console!            |
    | Enter 'help' to see a list of commands.                |
    |                                                        |
    |+------------------------------------------------------+|
   '''

    classes = {"BaseModel", "User"}

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

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
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(line)()
                new_instance.save()
                print(new_instance.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
            Prints the string representation of an instance
            based on the class name and id.
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """
            Deletes an instance based on the class name and id.
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """
            Prints string representations of all instances
            based or not based on the class name.
        """
        if not line:
            print([str(i) for i in storage.all().values()])
        else:
            try:
                print([str(i) for i in storage.all().values() if
                       type(i).__name__ == line])
            except:
                print("** class doesn't exist **")

    def do_update(self, line):
        """
            Updates an instance based on the class name and id
            by adding or updating attribute.
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                args = line.split()
                if len(args) == 1:
                    print("** instance id missing **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    if args[1] not in storage.all().keys():
                        print("** no instance found **")
                    else:
                        eval(args[0] + "." + args[1]).update(args[2], args[3])
                        storage.save()
            except:
                print("** class doesn't exist **")


def parse(line):
    """Helper method to parse user-typed input."""
    return tuple(line.split())


if __name__ == "__main__":
    HBNBCommand().cmdloop()

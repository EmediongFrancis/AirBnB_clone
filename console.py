#!/usr/bin/python3
"""
Building a command interpreter.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Starting the interpreter.
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit with Ctrl-D."""
        print()
        return True
    
    def do_quit(self, line):
        """Exit with `quit`."""
        print()
        return True

    def do_create(self, line):
        """
           Creates a new instance of BaseModel, saves it
           to disk, and prints the id.
        """
        if line:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return False
    


def parse(line):
    """Helper method to parse user-typed input."""
    return tuple(line.split())


if __name__ == "__main__":
    HBNBCommand().cmdloop()

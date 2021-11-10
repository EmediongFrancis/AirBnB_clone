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


def parse(line):
    """Helper method to parse user-typed input."""
    return tuple(line.split())


if __name__ == "__main__":
    HBNBCommand().cmdloop()

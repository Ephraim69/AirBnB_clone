#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command line program"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles Exiting the program by pressing Ctrl-D.
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

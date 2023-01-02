#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command line program"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True

    def do_quit(self, line):
        """Exits the program.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

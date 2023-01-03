#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel
import re
import json


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

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id"""
        if line == '' or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class name missing **")
        else:
            dict = storage.classes()
            inst = dict[line]()
            inst.save()
            print(inst.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234."""
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        if line == '' or line is None:
            print('** class name missing **')
            return
        cmd = line.split(' ')
        if cmd[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print('** instance id missing **')
        else:
            key = f'{cmd[0]}.{cmd[1]}'
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line == "":
            obj_list = [str(obj) for obj in storage.all().values()]
            print(obj_list)
        else:
            cmd = line.split(' ')
            if cmd[0] not in storage.classes():
                print('** class doesn\'t exist **')
                return
            obj_list = [str(obj) for obj in storage.all().values()
                        if type(obj).__name__ == cmd[0]]
            print(obj_list)

    def do_update(self, line):
        """ Updates an instance based on the class name
        and id by adding or updating attribute (save the
        change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"""
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
""" Alx AirBnB Console """
import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ General Class for HBNBCommand """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_quit(self, argument):
        """ Exit method for quit typing """
        exit()

    def do_EOF(self, argument):
        """ Exit method for EOF """
        print('')
        exit()

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

    def do_create(self, argument):
        """ Create a new instance """
        if len(argument) == 0:
            print('** class name missing **')

        new = None
        if argument:
            arg_list = argument.split()
            if len(arg_list) == 1:
                if argument in self.classes.keys():
                    new = self.classes[argument]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, argument):
        """ Method to print instance """
        if len(argument) == 0:
            print('** class name missing **')

        elif argument.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(argument.split()) > 1:
            key = argument.split()[0] + '.' + argument.split()[1]
            if key in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, argument):
        """ Method to delete instance with class and id """
        if len(argument) == 0:
            print("** class name missing **")

        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")

        if len(arg_list) == 1:
            print('** instance id missing **')

        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')


    def do_all(self, argument):
        """ Method to print all instances """
        if len(argument) == 0:
            print([str(a) for a in storage.all().values()])
        elif argument not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if argument in b])

    def do_update(self, argument):
        """ Method to update JSON file"""
        argument = argument.split()
        if len(argument) == 0:
            print('** class name missing **')

        elif argument[0] not in self.classes:
            print("** class doesn't exist **")

        elif len(argument) == 1:
            print('** instance id missing **')

        else:
            key = argument[0] + '.' + argument[1]
            if key in storage.all():
                if len(argument) > 2:
                    if len(argument) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            argument[2],
                            argument[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()

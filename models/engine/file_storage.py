#!/usr/bin/python3
"""FileStorage module for serializing and deserializing
JSON strigns and objects"""
import json
import os


class FileStorage():
    """FileStorage Class for saving objects to File using JSON"""
    __file_path = './objects.json'
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """sets an object to the __objects dict"""
        key = f'{type(obj)}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Save the __objects dict to a json file"""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """ deserializes the JSON file to
        __objects (only if the JSON file (__file_path) exists"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)

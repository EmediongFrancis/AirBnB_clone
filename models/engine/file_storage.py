#!/usr/bin/python3
'''File Storage'''
import json
from models.base_model import BaseModel


class FileStorage:
    """serializeing ang deserializing json"""

    __file_path = 'file.json'
    __objects = {}
    
    def all(self):
        """Return dictionry of __objects"""
        return self.__objects

    def new(self, obj):
        """adds new object to dictionary"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """save directories to json"""
        my_dict = {}

        for key, val in self.__objects.items():
            """if val is type dict"""
            my_dict[key] = val.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """convert existing json  dicts to instances"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass

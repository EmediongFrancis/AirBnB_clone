#!usr/bin/python3
"""
File storage: serializes instances to a JSON file and
deserializes JSON file to instance:
"""

import json
import models
import os


class Objects(dict):
    """class object"""

    def __getitem__(self, key):
        """get item"""
        try:
            return super(Objects, self).__getitem__(key)
        except Exception as e:
            raise Exception("** no instance found **")

    def pop(self, key):
        """pop item"""
        try:
            return super(Objects, self).pop(key)
        except Exception as e:
            raise Exception("** no instances **")


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON to instances
    """

    __file_path = 'file.json'
    __objects = Objects()

    def __init__(self):
        """init method"""
        super().__init__()

    def all(self):
        """return the class attribute objects"""
        return FileStorage.__objects

    def rest(self):
        """clear data on __object (cache)"""
        self._objects.clear()

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = '{}. {}'.format(type(obj).__name__, obj.id)
            self._objects[key] = obj

    def save(self):
        """ serializes __objects to JSON file (path: __file_path)"""
        file = FileStorage.__file_path

        with open(file, mode="w", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    FileStorage.__objects,
                    cls=models.base_model.BaseModelEncoder
                )
            )

    def reload(self):
        """deserializes the JSON file to __objects"""

        file = FileStorage.__file_path
        if not os.path.exists(file):
            return
        try:
            with open(file, mode='r+', encoding="utf-8") as f:
                file_string = f.read()
                data = json.loads(file_string)
                for object_key, model_data in data.item():
                    model_name, model_id = object_key.split('.')
                    model = models.classes[model_name](**model_name)
                    self.new(model)

        except Exception as e:
            print(e)

    def update(self, obj_name, obj_id, attr, value):
        """update object with id `obj_id`"""
        model = self.__objects["{}.{}".format(obj_name, obj_id)]
        setattr(model, attr, value)

    def find(self, obj_name, obj_id):
        """find object with id `obj_id`"""
        return self.__objects["{}.{}".format(obj_name, obj_id)]

    def delete(self, obj_name, obj_id):
        """delete object with id `obj_id`"""
        return self.__objects.pop("{}.{}".format(obj_name, obj_id))


# #!/usr/bin/python3

# '''File Storage'''

# import json
# import models
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review
# import os.path as path
# from models.base_model import BaseModel

# class FileStorage:
#     """serializing and deserializing instances
#     to and from json files"""

#     __file_path = 'file.json'
#     __objects = {}

#     def all(self):
#         """Returns dictionary: __objects"""
#         return self.__objects

#     def new(self, obj):
#         """adds new object to dictionary"""
#         if obj:
#             obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
#             self.__objects[obj_key] = obj

#     def save(self):
#         """save directories to json"""
#         my_dict = {}
#         with open(self.__file_path, mode="w", encoding='UTF-8') as f:
#             for key, value in self.__objects.items():
#                 my_dict[key] = value.to_dict()
#             json.dump(my_dict, f)

#     def reload(self):
#         """convert existing json  dicts to instances"""
#         try:
#             if path.isfile(self.__file_path):
#                 with open(self.__file_path, mode="r", encoding='UTF-8') as f:
#                    for key, value in json.load(f).items():
#                        value = eval(value['__class__'])(**value)
#                        self.__objects[key] = value
#         except FileNotFoundError:
#             pass

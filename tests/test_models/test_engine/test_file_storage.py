#!/usr/bin/python3

"""
    Unit tests for file storage.
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import io
from datetime import datetime
import json
import unittest
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import path, remove


class Test_all(unittest.TestCase):
    """
        Tests the `all` command.
    """

    def setUp(self):
        """
            Sets up the tests.
        """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """
            Tears down the tests.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_all_w_o_arg(self):
        """
            Tests the `all` command without arguments.
        """
        self.assertEqual(models.storage.all(), {})

    def test_all_w_arg(self):
        """
            Tests the `all` command with arguments.
        """
        bm = BaseModel()
        name = bm.__class__.__name__ + "." + bm.id
        dict_ = {name: bm}
        self.assertEqual(models.storage.all(), {})

    def test_user(self):
        """
            Tests the `all` command with User.
        """
        bm = User()
        name = bm.__class__.__name__ + "." + bm.id
        dict_ = {name: bm}
        self.assertEqual(models.storage.all(), dict)

    def test_state(self):
        """
            Tests the `all` command with State.
        """
        bm = State()
        name = bm.__class__.__name__ + "." + bm.id
        dict_ = {name: bm}
        self.assertEqual(models.storage.all(), dict)

    def test_city(self):
        """
            Tests the `all` command with City.
        """
        bm = City()
        name = bm.__class__.__name__ + "." + bm.id
        dict_ = {name: bm}
        self.assertEqual(models.storage.all(), dict)

    def test_amenity(self):
        """
            Tests the `all` command with Amenity.
        """
        bm = Amenity()
        name = bm.__class__.__name__ + "." + bm.id
        dict_ = {name: bm}
        self.assertEqual(models.storage.all(), dict)

    def test_place(self):
        """
            Tests the `all` command with Place.
        """
        bm = Place()
        name = bm.__class__.__name__ + "." + bm.id
        dict_ = {name: bm}
        self.assertEqual(models.storage.all(), dict)

    def test_review(self):
        """
            Tests the `all` command with Review.
        """
        bm = Review()
        name = bm.__class__.__name__ + "." + bm.id
        dict_ = {name: bm}
        self.assertEqual(models.storage.all(), dict)

    def test_all_classes(self):
        """
            Tests the `all` command with all classes.
        """
        bm = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()

        dicts = models.storage.all()
        self.assertEqual(bm, dicts["BaseModel.{}".format(bm.id)])
        self.assertEqual(u, dicts["User.{}".format(u.id)])
        self.assertEqual(s, dicts["State.{}".format(s.id)])
        self.assertEqual(c, dicts["City.{}".format(c.id)])
        self.assertEqual(a, dicts["Amenity.{}".format(a.id)])
        self.assertEqual(p, dicts["Place.{}".format(p.id)])
        self.assertEqual(r, dicts["Review.{}".format(r.id)])


class Test_new(unittest.TestCase):
    """
        Tests the `new` command.
    """

    def setUp(self):
        """
            Sets up the tests.
        """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """
            Tears down the tests.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_new_w_o_arg(self):
        """
            Tests the `new` command without arguments.
        """
        with self.assertRaises(TypeError):
            models.storage.new()

    def test_new_w_arg(self):
        """
            Tests the `new` command with arguments.
        """
        bm = BaseModel()
        with self.assertRaises(TypeError):
            models.storage.new(bm, bm)

    def test_new_base(self):
        """
            Tests the `new` command with BaseModel.
        """
        dict = {"id": "456"}
        bm = BaseModel(**dict)
        key = bm.__class__.__name__ + "." + "456"
        dicts = models.storage.all()
        self.assertEqual(dicts, {})
        models.storage.new(bm)
        dicts = models.storage.all()
        self.assertEqual(bm, dicts[key])

    def test_new_user(self):
        """
            Tests the `new` command with User.
        """
        dict = {"id": "456"}
        bm = User(**dict)
        key = bm.__class__.__name__ + "." + "456"
        dicts = models.storage.all()
        self.assertEqual(dicts, {})
        models.storage.new(bm)
        dicts = models.storage.all()
        self.assertEqual(bm, dicts[key])

    def test_new_state(self):
        """
            Tests the `new` command with State.
        """
        dict = {"id": "456"}
        bm = State(**dict)
        key = bm.__class__.__name__ + "." + "456"
        dicts = models.storage.all()
        self.assertEqual(dicts, {})
        models.storage.new(bm)
        dicts = models.storage.all()
        self.assertEqual(bm, dicts[key])

    def test_new_city(self):
        """
            Tests the `new` command with City.
        """
        dict = {"id": "456"}
        bm = City(**dict)
        key = bm.__class__.__name__ + "." + "456"
        dicts = models.storage.all()
        self.assertEqual(dicts, {})
        models.storage.new(bm)
        dicts = models.storage.all()
        self.assertEqual(bm, dicts[key])

    def test_new_amenity(self):
        """
            Tests the `new` command with Amenity.
        """
        dict = {"id": "456"}
        bm = Amenity(**dict)
        key = bm.__class__.__name__ + "." + "456"
        dicts = models.storage.all()
        self.assertEqual(dicts, {})
        models.storage.new(bm)
        dicts = models.storage.all()
        self.assertEqual(bm, dicts[key])

    def test_new_place(self):
        """
            Tests the `new` command with Place.
        """
        dict = {"id": "456"}
        bm = Place(**dict)
        key = bm.__class__.__name__ + "." + "456"
        dicts = models.storage.all()
        self.assertEqual(dicts, {})
        models.storage.new(bm)
        dicts = models.storage.all()
        self.assertEqual(bm, dicts[key])

    def test_new_review(self):
        """
            Tests the `new` command with Review.
        """
        dict = {"id": "456"}
        bm = Review(**dict)
        key = bm.__class__.__name__ + "." + "456"
        dicts = models.storage.all()
        self.assertEqual(dicts, {})
        models.storage.new(bm)
        dicts = models.storage.all()
        self.assertEqual(bm, dicts[key])


class Test_save(unittest.TestCase):
    """
        Tests the `save` command.
    """

    def setUp(self):
        """
            Sets up the tests.
        """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """
            Tears down the tests.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_save_base(self):
        """
            Tests the `save` command with BaseModel.
        """
        bm = BaseModel()
        key = bm.__class__.__name__ + "." + bm.id
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        with open(filename, encoding="utf-8") as f:
            object = json.load(f)
            self.assertEqual(bm.id, object[key]["id"])
            self.assertEqual(bm.__class__.__name__, object[key]["__class__"])

    def test_save_base_no_kwarg(self):
        """
            Tests the `save` command with BaseModel without arguments.
        """
        bm = BaseModel()
        bm1 = BaseModel()
        key = bm.__class__.__name__ + "." + bm.id
        key1 = bm1.__class__.__name__ + "." + bm1.id
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        with open(filename, encoding="utf-8") as f:
            object = json.load(f)
            self.assertEqual(bm.id, object[key]["id"])
            self.assertEqual(bm.__class__.__name__, object[key]["__class__"])
            self.assertEqual(bm1.id, object[key1]["id"])
            self.assertEqual(bm1.__class__.__name__, object[key1]["__class__"])

    def test_save_user(self):
        """
            Tests the `save` command with User.
        """
        dict = {"id": "456"}
        bm = User(**dict)
        key = bm.__class__.__name__ + "." + "456"
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.new(bm)
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        with open(filename, encoding="utf-8") as f:
            object = json.load(f)
            self.assertEqual(bm.id, object[key]["id"])
            self.assertEqual(bm.__class__.__name__, object[key]["__class__"])

    def test_save_state(self):
        """
            Tests the `save` command with State.
        """
        dict = {"id": "456"}
        bm = State(**dict)
        key = bm.__class__.__name__ + "." + "456"
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.new(bm)
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        with open(filename, encoding="utf-8") as f:
            object = json.load(f)
            self.assertEqual(bm.id, object[key]["id"])
            self.assertEqual(bm.__class__.__name__, object[key]["__class__"])

    def test_save_city(self):
        """
            Tests the `save` command with City.
        """
        dict = {"id": "456"}
        bm = City(**dict)
        key = bm.__class__.__name__ + "." + "456"
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.new(bm)
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        with open(filename, encoding="utf-8") as f:
            object = json.load(f)
            self.assertEqual(bm.id, object[key]["id"])
            self.assertEqual(bm.__class__.__name__, object[key]["__class__"])

    def test_save_place(self):
        """
            Tests the `save` command with Place.
        """
        dict = {"id": "456"}
        bm = Place(**dict)
        key = bm.__class__.__name__ + "." + "456"
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.new(bm)
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        with open(filename, encoding="utf-8") as f:
            object = json.load(f)
            self.assertEqual(bm.id, object[key]["id"])
            self.assertEqual(bm.__class__.__name__, object[key]["__class__"])

    def test_save_amenity(self):
        """
            Tests the `save` command with Amenity.
        """
        dict = {"id": "456"}
        bm = Amenity(**dict)
        key = bm.__class__.__name__ + "." + "456"
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.new(bm)
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        with open(filename, encoding="utf-8") as f:
            object = json.load(f)
            self.assertEqual(bm.id, object[key]["id"])
            self.assertEqual(bm.__class__.__name__, object[key]["__class__"])

    def test_save_review(self):
        """
            Tests the `save` command with Review.
        """
        dict = {"id": "456"}
        bm = Review(**dict)
        key = bm.__class__.__name__ + "." + "456"
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.new(bm)
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        with open(filename, encoding="utf-8") as f:
            object = json.load(f)
            self.assertEqual(bm.id, object[key]["id"])
            self.assertEqual(bm.__class__.__name__, object[key]["__class__"])

    def test_save_all(self):
        """
            Tests the `save` command with all classes.
        """
        dict = {"id": "456"}
        bm = BaseModel(**dict)
        u = User(**dict)
        s = State(**dict)
        c = City(**dict)
        p = Place(**dict)
        a = Amenity(**dict)
        r = Review(**dict)
        key = bm.__class__.__name__ + "." + "456"
        key1 = u.__class__.__name__ + "." + "456"
        key2 = s.__class__.__name__ + "." + "456"
        key3 = c.__class__.__name__ + "." + "456"
        key4 = p.__class__.__name__ + "." + "456"
        key5 = a.__class__.__name__ + "." + "456"
        key6 = r.__class__.__name__ + "." + "456"
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.new(bm)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(c)
        models.storage.new(p)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        with open(filename, encoding="utf-8") as f:
            object = json.load(f)
            self.assertEqual(bm.id, object[key]["id"])
            self.assertEqual(bm.__class__.__name__, object[key]["__class__"])
            self.assertEqual(u.id, object[key1]["id"])
            self.assertEqual(u.__class__.__name__, object[key1]["__class__"])
            self.assertEqual(s.id, object[key2]["id"])
            self.assertEqual(s.__class__.__name__, object[key2]["__class__"])
            self.assertEqual(c.id, object[key3]["id"])
            self.assertEqual(c.__class__.__name__, object[key3]["__class__"])
            self.assertEqual(p.id, object[key4]["id"])
            self.assertEqual(p.__class__.__name__, object[key4]["__class__"])
            self.assertEqual(a.id, object[key5]["id"])
            self.assertEqual(a.__class__.__name__, object[key5]["__class__"])
            self.assertEqual(r.id, object[key6]["id"])
            self.assertEqual(r.__class__.__name__, object[key6]["__class__"])

    def test_save_all_no_kwargs(self):
        """
            Tests the `save` command with all classes without kwargs.
        """
        bm = BaseModel()
        u = User()
        s = State()
        c = City()
        p = Place()
        a = Amenity()
        r = Review()
        key = bm.__class__.__name__ + "." + bm.id
        key1 = u.__class__.__name__ + "." + u.id
        key2 = s.__class__.__name__ + "." + s.id
        key3 = c.__class__.__name__ + "." + c.id
        key4 = p.__class__.__name__ + "." + p.id
        key5 = a.__class__.__name__ + "." + a.id
        key6 = r.__class__.__name__ + "." + r.id
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        with open(filename, encoding="utf-8") as f:
            object = json.load(f)
            self.assertEqual(bm.id, object[key]["id"])
            self.assertEqual(bm.__class__.__name__, object[key]["__class__"])
            self.assertEqual(u.id, object[key1]["id"])
            self.assertEqual(u.__class__.__name__, object[key1]["__class__"])
            self.assertEqual(s.id, object[key2]["id"])
            self.assertEqual(s.__class__.__name__, object[key2]["__class__"])
            self.assertEqual(c.id, object[key3]["id"])
            self.assertEqual(c.__class__.__name__, object[key3]["__class__"])
            self.assertEqual(p.id, object[key4]["id"])
            self.assertEqual(p.__class__.__name__, object[key4]["__class__"])
            self.assertEqual(a.id, object[key5]["id"])
            self.assertEqual(a.__class__.__name__, object[key5]["__class__"])
            self.assertEqual(r.id, object[key6]["id"])
            self.assertEqual(r.__class__.__name__, object[key6]["__class__"])


class Test_reload(unittest.TestCase):
    """
        Tests the `reload` command.
    """

    def setUp(self):
        """
            Sets up the tests.
        """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """
            Tears down the tests.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_reload_no_file(self):
        """
            Tests the `reload` command with no file.
        """
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.reload()

    def test_reload_base(self):
        """
            Tests the `reload` command with BaseModel.
        """
        bm = BaseModel()
        bm.name = "Bendito"
        key = bm.__class__.__name__ + "." + bm.id
        filename = "file.json"
        self.assertFalse(path.isfile(filename))
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        self.assertTrue(len(models.storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(models.storage.all(), {})
        models.storage.reload()
        dicts = models.storage.all()
        self.assertFalse(bm == dicts[key])
        self.assertEqual(bm.id, dicts[key].id)
        self.assertEqual(bm.__class__, dicts[key].__class__)
        self.assertEqual(bm.created_at, dicts[key].created_at)
        self.assertEqual(bm.updated_at, dicts[key].updated_at)
        self.assertEqual(bm.name, dicts[key].name)

    def test_reload_user(self):
        """
            Tests the `reload` command with User.
        """
        filename = "file.json"
        u = User()
        u.name = "Bendito"
        key = u.__class__.__name__ + "." + u.id
        self.assertFalse(path.isfile(filename))
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        self.assertTrue(len(models.storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(models.storage.all(), {})
        models.storage.reload()
        dicts = models.storage.all()
        self.assertFalse(u == dicts[key])
        self.assertEqual(u.id, dicts[key].id)
        self.assertEqual(u.__class__, dicts[key].__class__)
        self.assertEqual(u.created_at, dicts[key].created_at)
        self.assertEqual(u.updated_at, dicts[key].updated_at)
        self.assertEqual(u.name, dicts[key].name)

    def test_reload_state(self):
        """
            Tests the `reload` command with State.
        """
        filename = "file.json"
        s = State()
        s.name = "Bendito"
        key = s.__class__.__name__ + "." + s.id
        self.assertFalse(path.isfile(filename))
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        self.assertTrue(len(models.storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(models.storage.all(), {})
        models.storage.reload()
        dicts = models.storage.all()
        self.assertFalse(s == dicts[key])
        self.assertEqual(s.id, dicts[key].id)
        self.assertEqual(s.__class__, dicts[key].__class__)
        self.assertEqual(s.created_at, dicts[key].created_at)
        self.assertEqual(s.updated_at, dicts[key].updated_at)
        self.assertEqual(s.name, dicts[key].name)

    def test_reload_city(self):
        """
            Tests the `reload` command with City.
        """
        filename = "file.json"
        c = City()
        c.name = "Bendito"
        key = c.__class__.__name__ + "." + c.id
        self.assertFalse(path.isfile(filename))
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        self.assertTrue(len(models.storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(models.storage.all(), {})
        models.storage.reload()
        dicts = models.storage.all()
        self.assertFalse(c == dicts[key])
        self.assertEqual(c.id, dicts[key].id)
        self.assertEqual(c.__class__, dicts[key].__class__)
        self.assertEqual(c.created_at, dicts[key].created_at)
        self.assertEqual(c.updated_at, dicts[key].updated_at)
        self.assertEqual(c.name, dicts[key].name)

    def test_reload_place(self):
        """
            Tests the `reload` command with Place.
        """
        filename = "file.json"
        p = Place()
        p.name = "Bendito"
        key = p.__class__.__name__ + "." + p.id
        self.assertFalse(path.isfile(filename))
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        self.assertTrue(len(models.storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(models.storage.all(), {})
        models.storage.reload()
        dicts = models.storage.all()
        self.assertFalse(p == dicts[key])
        self.assertEqual(p.id, dicts[key].id)
        self.assertEqual(p.__class__, dicts[key].__class__)
        self.assertEqual(p.created_at, dicts[key].created_at)
        self.assertEqual(p.updated_at, dicts[key].updated_at)
        self.assertEqual(p.name, dicts[key].name)

    def test_reload_amenity(self):
        """
            Tests the `reload` command with Amenity.
        """
        filename = "file.json"
        a = Amenity()
        a.name = "Bendito"
        key = a.__class__.__name__ + "." + a.id
        self.assertFalse(path.isfile(filename))
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        self.assertTrue(len(models.storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(models.storage.all(), {})
        models.storage.reload()
        dicts = models.storage.all()
        self.assertFalse(a == dicts[key])
        self.assertEqual(a.id, dicts[key].id)
        self.assertEqual(a.__class__, dicts[key].__class__)
        self.assertEqual(a.created_at, dicts[key].created_at)
        self.assertEqual(a.updated_at, dicts[key].updated_at)
        self.assertEqual(a.name, dicts[key].name)

    def test_reload_review(self):
        """
            Tests the `reload` command with Review.
        """
        filename = "file.json"
        r = Review()
        r.text = "Bendito"
        key = r.__class__.__name__ + "." + r.id
        self.assertFalse(path.isfile(filename))
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        self.assertTrue(len(models.storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(models.storage.all(), {})
        models.storage.reload()
        dicts = models.storage.all()
        self.assertFalse(r == dicts[key])
        self.assertEqual(r.id, dicts[key].id)
        self.assertEqual(r.__class__, dicts[key].__class__)
        self.assertEqual(r.created_at, dicts[key].created_at)
        self.assertEqual(r.updated_at, dicts[key].updated_at)
        self.assertEqual(r.text, dicts[key].text)

    def test_reload_all(self):
        """
            Tests the `reload` command with all classes.
        """
        filename = "file.json"
        a = Amenity()
        bm = BaseModel()
        c = City()
        p = Place()
        r = Review()
        s = State()
        u = User()

        key = a.__class__.__name__ + "." + a.id
        key2 = bm.__class__.__name__ + "." + bm.id
        key3 = c.__class__.__name__ + "." + c.id
        key4 = p.__class__.__name__ + "." + p.id
        key5 = r.__class__.__name__ + "." + r.id
        key6 = s.__class__.__name__ + "." + s.id
        key7 = u.__class__.__name__ + "." + u.id

        self.assertFalse(path.isfile(filename))
        models.storage.save()
        self.assertTrue(path.isfile(filename))
        self.assertTrue(len(models.storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(models.storage.all(), {})
        models.storage.reload()
        dicts = models.storage.all()
        classes = [a, bm, c, p, r, s, u]
        class_names = ['a', 'bm', 'c', 'p', 'r', 's', 'u']
        for s, k in zip(classes, class_names):
            key = "key" + k
            self.assertFalse(s == dicts[eval(key)])
            self.assertEqual(s.id, dicts[eval(key)].id)
            self.assertEqual(s.__class__, dicts[eval(key)].__class__)

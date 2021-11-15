#!/usr/bin/python3

"""
    Unit tests for the User model.
"""

from models.user import User
from models.base_model import BaseModel
import unittest
from datetime import datetime
import io
from os import path, remove
from unittest.mock import patch
from time import sleep


class Test_user_instance(unittest.TestCase):
    """
        Test cases for the User class.
    """

    def setUp(self):
        """
            Initializes the User class.
        """
        pass

    def tearDown(self):
        """
            Cleans up the User class.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_user_instance(self):
        """
            Test that the User class is an instance of BaseModel.
        """
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_args(self):
        """
            Test that the User with args is an
            instance of BaseModel.
        """
        user = User(696, "Hi", ["Bye"])
        self.assertTrue(isinstance(user, BaseModel))

    def test_user_kwargs(self):
        """
            Test that the User with kwargs is an
            instance of BaseModel.
        """
        datas = {"name": "Bendito"}
        user = User(**datas)
        self.assertTrue(isinstance(user, BaseModel))


class Test_user_attributes(unittest.TestCase):
    """
        Test cases for the User class attributes.
    """

    def setUp(self):
        """
            Initializes the User class.
        """
        pass

    def tearDown(self):
        """
            Cleans up the User class.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_user_attributes(self):
        """
            Test that the User class has the
            correct attributes.
        """
        user = User()
        attribute = ["email", "password", "first_name", "last_name"]
        dat = user.__dict__
        for i in attribute:
            self.assertFalse(i in dat)
            self.assertTrue(hasattr(user, i))
            self.assertEqual(getattr(user, i, False), "")

    def test_set_attrs(self):
        """
            Test that the User class has the
            correct attributes.
        """
        user = User()
        attribute = ["email", "password", "first_name", "last_name"]
        values = ["emediong@gmail.com", "root", "Emediong", "Francis"]
        for a, j in zip(attribute, values):
            setattr(user, a, j)
        dat = user.__dict__
        for i, m in zip(attribute, values):
            self.assertEqual(getattr(user, i, False), m)
        for i in attribute:
            self.assertEqual(getattr(user.__class__, i, False), "")


class Test_init_user(unittest.TestCase):
    """
        Test cases for the User class init method.
    """

    def setUp(self):
        """
            Initializes the User class.
        """
        pass

    def tearDown(self):
        """
            Cleans up the User class.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_instance_creation_w_o_arg(self):
        """
            Test that the User class with no args
            is an instance of BaseModel.
        """
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_attr_types(self):
        """
            Test that the User class attributes
            are of the correct type.
        """
        user = User()
        self.assertEqual(type(user.id), str)
        self.assertEqual(type(user.created_at), datetime)
        self.assertEqual(type(user.updated_at), datetime)

    def test_id__different_instances(self):
        """
            Test that the User class id is
            different for different instances.
        """
        user1 = User()
        user2 = User()
        user3 = User()
        user4 = User()
        self.assertFalse(user1.id == user2.id)
        self.assertFalse(user1.id == user3.id)
        self.assertFalse(user1.id == user4.id)
        self.assertFalse(user2.id == user3.id)
        self.assertFalse(user2.id == user4.id)
        self.assertFalse(user3.id == user4.id)

    def test_args(self):
        """
            Test that the User class with args
            is an instance of BaseModel.
        """
        user = User(1)
        user2 = User(1, "Hi")
        user3 = User(1, "Hi", (1, 2))
        user4 = User(696, "Hi", (1, 2), [1, 2])

    def test_args_def(self):
        """
            Test that the User class with args
            is an instance of BaseModel.
        """
        user = User(1, "hi", (1, 2), [1, 2])
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_kwargs(self):
        """
            Test that the User class with kwargs
            is an instance of BaseModel.
        """
        dat = {"id": "43ff8bae-dbe6-4a99-bc27-6ffa7f26caef",
               "created_at": "2021-11-13T01:16:36.442329",
               "updated_at": "2021-11-13T01:16:36.442382",
               "class_": "User"}

        user = User(**dat)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "__class__"))
        self.assertTrue(user.__class__ not in user.__dict__)

        self.assertEqual(user.id, dat["id"])
        self.assertEqual(user.created_at.isoformat(), dat["created_at"])
        self.assertEqual(user.updated_at.isoformat(), dat["updated_at"])

    def test_no_def_kwargs(self):
        """
            Checks if id/datecreatedif !in kwargs.
        """
        dat = {"name": "Bendito"}
        user = User(**dat)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertEqual(user.name, "Bendito")

    def test_dates_to_datetime(self):
        """
            Checks proper datetime conversion.
        """
        dat = {"id": "43ff8bae-dbe6-4a99-bc27-6ffa7f26caef",
               "created_at": "2021-11-13T01:16:36.442329",
               "updated_at": "2021-11-13T01:16:36.442382",
               "class_": "User"}

        user = User(**dat)
        self.assertEqual(user.created_at.isoformat(), dat["created_at"])
        self.assertEqual(user.updated_at.isoformat(), dat["updated_at"])
        self.assertEqual(type(user.created_at), datetime)
        self.assertEqual(type(user.updated_at), datetime)

    def test_args_kwargs(self):
        """
            Test that the User class with args and kwargs
            is an instance of BaseModel.
        """
        dat = {"id": "43ff8bae-dbe6-4a99-bc27-6ffa7f26caef",
               "created_at": "2021-11-13T01:16:36.442329",
               "updated_at": "2021-11-13T01:16:36.442382",
               "class_": "User"}
        user = User(1, "Hi", ["World"], **dat)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "__class__"))
        self.assertTrue(user.__class__ not in user.__dict__)


class Test_str(unittest.TestCase):
    """
        Test cases for the User class str method.
    """

    def setUp(self):
        """
            Initializes the User class.
        """
        pass

    def tearDown(self):
        """
            Cleans up the User class.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_print(self):
        """
            Test that the User class str method
            returns the correct string.
        """
        user = User()
        string = "[{:s}] ({:s}) {:s}\n"
        string = string.format(user.__class__.__name__,
                               user.id,
                               str(user.__dict__))
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            print(user)
            self.assertEqual(fake_out.getvalue(), string)

    def test_str(self):
        """
            Test that the User class str method
            returns the correct string.
        """
        user = User()
        user.name = "Bendito"
        user.code = 6969
        string = "[{:s}] ({:s}) {:s}\n"
        string = string.format(user.__class__.__name__,
                               user.id,
                               str(user.__dict__))
        self.assertEqual(str(user), string)
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            print(user)
            self.assertEqual(fake_out.getvalue(), string)

    def test_print_kwargs(self):
        """
            Test that the User class str method
            returns the correct string.
        """
        dat = {"id": "43ff8bae-dbe6-4a99-bc27-6ffa7f26caef",
               "created_at": "2021-11-13T01:16:36.442329",
               "updated_at": "2021-11-13T01:16:36.442382",
               "class_": "User"}
        user = User(**dat)
        string = "[{:s}] ({:s}) {:s}\n"
        string = string.format(user.__class__.__name__,
                               user.id,
                               str(user.__dict__))
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            print(user)
            self.assertEqual(fake_out.getvalue(), string)


class Test_save(unittest.TestCase):
    """
        Test cases for the User class save method.
    """

    def setUp(self):
        """
            Initializes the User class.
        """
        pass

    def tearDown(self):
        """
            Cleans up the User class.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_save(self):
        """
            Test that the updated_at time is updated
            via save method.
        """
        user = User()
        time_cr = user.created_at
        time_up = user.updated_at
        sleep(0.05)
        user.save()
        self.assertFalse(time_up == user.updated_at)
        self.assertTrue(time_cr == user.created_at)


class Test_to_dict(unittest.TestCase):
    """
        Test cases for the User class to_dict method.
    """

    def setUp(self):
        """
            Initializes the User class.
        """
        pass

    def tearDown(self):
        """
            Cleans up the User class.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_to_dict(self):
        """
            Test that the User class to_dict method
            returns the correct dictionary.
        """
        user = User()
        user.name = "Bendito"
        user.code = 6969
        dat = {}
        dat["id"] = user.id
        dat["created_at"] = user.created_at.isoformat()
        dat["updated_at"] = user.updated_at.isoformat()
        dat["name"] = user.name
        dat["code"] = user.code
        dicts = user.to_dict()
        self.assertEqual(dat["id"], dicts["id"])
        self.assertEqual(dat["created_at"], dicts["created_at"])
        self.assertEqual(dat["updated_at"], dicts["updated_at"])
        self.assertEqual(dat["name"], dicts["name"])
        self.assertEqual(dat["code"], dicts["code"])

    def test_to_dict_class_dates(self):
        """
            Test that the User class to_dict method
            returns the correct dictionary.
        """
        user = User()
        dicts = user.to_dict()
        self.assertEqual(dicts["__class__"], "User")
        self.assertEqual(type(dicts["created_at"]), str)
        self.assertEqual(type(dicts["updated_at"]), str)

    def test_isoformat(self):
        """
            Test that the User class to_dict method
            returns the correct dictionary.
        """
        user = User()
        time_cr = datetime.now()
        time_up = datetime.now()
        user.created_at = time_cr
        user.updated_at = time_up
        dicts = user.to_dict()
        self.assertEqual(dicts["created_at"], time_cr.isoformat())
        self.assertEqual(dicts["updated_at"], time_up.isoformat())

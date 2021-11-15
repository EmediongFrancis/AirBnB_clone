#!/usr/bin/python3

"""
    Unit tests for the State class.
"""

from datetime import datetime
import unittest
from models import state
from models.base_model import BaseModel
from models.state import State
from os import path, remove
from unittest.mock import patch
from time import sleep
import io

class Test_state_instance(unittest.TestCase):
    """
        Instance checking of State class.
    """

    def setUp(self):
        """
            Setting up the test.
        """
        pass

    def tearDown(self):
        """
            Cleaning up the test.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_state_instance(self):
        """
            Test for State class instance.
        """
        state = State()
        self.assertTrue(isinstance(state, BaseModel))

    def test_instance_args(self):
        """
            Test for State class instance arguments.
        """
        state = State(6969, "Hi", ["People"])
        self.assertTrue(isinstance(state, BaseModel))

    def test_intance_kwargs(self):
        """
            Test for State class instance with kwargs.
        """
        dat = {"name": "John"}
        state = State(**dat)
        self.assertTrue(isinstance(state, BaseModel))


class Test_state_attributes(unittest.TestCase):
    """
        Attributes checking of State class.
    """

    def setUp(self):
        """
            Setting up the test.
        """
        pass

    def tearDown(self):
        """
            Cleaning up the test.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_correct_state_attributes(self):
        """
            Test for presence of State class attributes.
        """
        state = State()
        attribute = ["name"]
        dat = state.__dict__
        for key in attribute:
            self.assertFalse(key in dat)
            self.assertTrue(hasattr(state, key))
            self.assertEqual(getattr(state, key, False), "")

    def test_set_attributes(self):
        """
            Test for setting State class attributes.
        """
        state = State()
        attribute = ["name"]
        value = ["Bendito"]
        for key, val in zip(attribute, value):
            setattr(state, key, val)
            dat = state.__dict__
        for key, val in zip(attribute, value):
            self.assertEqual(getattr(state, key, False), val)
        for key in attribute:
            self.assertEqual(getattr(state.__class__, key, False), "")


class Test_state_init(unittest.TestCase):
    """
        Init checking of State class.
    """
    
    def setUp(self):
        """
          Setting up the test.
        """
        pass
    
        def tearDown(self):
            """
                Cleaning up the test.
            """
            try:
                remove("file.json")
            except:
                pass
    
        def test_state_init(self):
            """
                Test for State class init.
            """
            state = State()
            self.assertTrue(hasattr(state, "id"))
            self.assertTrue(hasattr(state, "created_at"))
            self.assertTrue(hasattr(state, "updated_at"))
    
        def test_state_init_args(self):
            """
                Test for State class init with args.
            """
            s1 = State(1)
            s2 = State(1, "hi")
            s3 = State(1, "hi", (1, 2))
            s4 = State(1, "hi", (1, 2), [1, 2])
    
        def test_state_init_kwargs(self):
            """
                Test for State class init with kwargs.
            """
            dat = {"id": "43ff8bae-dbe6-4a99-bc27-6ffa7f26caef",
               "created_at": "2021-11-13T01:16:36.442329",
               "updated_at": "2021-11-13T01:16:36.442382",
               "class_": "State"}
            state = State(**dat)
            self.assertTrue(hasattr(state, "id"))
            self.assertTrue(hasattr(state, "created_at"))
            self.assertTrue(hasattr(state, "updated_at"))
            self.assertTrue(hasattr(state, "__class__"))
            self.assertTrue(state.__class__ not in state.__dict__)
            self.assertEqual(state.id, dat["id"])
            self.assertEqual(state.created_at.isoformat(), dat["created_at"])
            self.assertEqual(state.updated_at.isoformat(), dat["updated_at"])

        def test_attr_types(self):
            """
                Tests for attribute types.
            """
            state = State()
            self.assertEqual(type(state.id), str)
            self.assertEqual(type(state.created_at), datetime)
            self.assertEqual(type(state.updated_at), datetime)

        def test_different_instance_id(self):
            """
                Test for different instance id.
            """
            state1 = State()
            state2 = State()
            self.assertNotEqual(state1.id, state2.id)

        def test_no_def_args(self):
            """
                Test for no default args.
            """
            dat = {"name": "Bendito"}
            state = State(**dat)
            self.assertTrue(hasattr(state, "id"))
            self.assertTrue(hasattr(state, "created_at"))
            self.assertTrue(hasattr(state, "updated_at"))
            self.assertEqual(state.name, "Bendito")

        def test_dates_to_str(self):
            """
                Test for dates to string.
            """
            dat = {"id": "43ff8bae-dbe6-4a99-bc27-6ffa7f26caef",
               "created_at": "2021-11-13T01:16:36.442329",
               "updated_at": "2021-11-13T01:16:36.442382",
               "class_": "State"}
            state = State(**dat)
            self.assertEqual(state.created_at.isoformat(), dat["created_at"])
            self.assertEqual(state.updated_at.isoformat(), dat["updated_at"])
            self.assertEqual(type(state.created_at), datetime)
            self.assertEqual(type(state.updated_at), datetime)


class Test_state_str(unittest.TestCase):
    """
        String representation of State class.
    """

    def setUp(self):
        """
            Setting up the test.
        """
        pass

    def tearDown(self):
        """
            Cleaning up the test.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_print(self):
        """
            Test for print.
        """
        state = State()
        string = "[{:s}] ({:s}) {:s}\n"
        string = string.format(state.__class__.__name__,
                                 state.id,
                                    str(state.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print(state)
            self.assertEqual(fake_out.getvalue().strip(), string)

    def test_print_two(self):
        """
            Test for print two.
        """
        state = State()
        state.name = "Bendito"
        state.code = 69
        string = "[{:s}] ({:s}) {:s}\n"
        string = string.format(state.__class__.__name__,
                                 state.id,
                                    str(state.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print(state)
            self.assertEqual(fake_out.getvalue(), string)

    def test_print_args(self):
        """
            Test for print two.
        """
        state = State(None, 1, ["B"])
        state.name = "Bendito"
        state.code = 69
        string = "[{:s}] ({:s}) {:s}\n"
        string = string.format(state.__class__.__name__,
                                 state.id,
                                    str(state.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print(state)
            self.assertEqual(fake_out.getvalue(), string)

    def test_print_kwargs(self):
        """
            Test for printing with kwargs.
        """
        dat = {"id": "43ff8bae-dbe6-4a99-bc27-6ffa7f26caef",
                "created_at": "2021-11-13T01:16:36.442329",
                "updated_at": "2021-11-13T01:16:36.442382",
                "class_": "State"}
        state = State(**dat)
        string = "[{:s}] ({:s}) {:s}\n"
        string = string.format(state.__class__.__name__,
                                 state.id,
                                    str(state.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print(state)
            self.assertEqual(fake_out.getvalue(), string)


class Test_save_state(unittest.TestCase):
    """
        Test for save_state.
    """

    def setUp(self):
        """
            Setting up the test.
        """
        pass

    def tearDown(self):
        """
            Cleaning up the test.
        """
        try:
            remove("file.json")
        except:
            pass
            
    def test_save_state(self):
        """
            Test for save_state.
        """
        state = State()
        time_cr = state.created_at
        time_up = state.updated_at
        sleep(0.05)
        state.save()
        self.assertTrue(state.created_at == time_cr)
        self.assertFalse(state.updated_at == time_up)

    def test_type_save(self):
        """
            Test for save_state.
        """
        state = State()
        state.save()
        self.assertTrue(type(state.created_at) == datetime)
        self.assertTrue(type(state.updated_at) == datetime)


class Test_to_dict_state(unittest.TestCase):
    """
        Test for to_dict_state.
    """

    def setUp(self):
        """
            Setting up the test.
        """
        pass

    def tearDown(self):
        """
            Cleaning up the test.
        """
        try:
            remove("file.json")
        except:
            pass

    def test_to_dict_state(self):
        """
            Test for to_dict_state.
        """
        state = State()
        state.name = "Bendito"
        state.code = 69
        dat = {}
        dat["id"] = state.id
        dat["created_at"] = state.created_at.isoformat()
        dat["updated_at"] = state.updated_at.isoformat()
        dat["name"] = state.name
        dat["code"] = state.code
        dicts = state.to_dict()
        self.assertEqual(dat, dicts)

    def test_to_dict_dates(self):
        """
            Test for to_dict_state.
        """
        state = State()
        dicts = state.to_dict()
        self.assertEqual(dicts["__class__"], "State")
        self.assertEqual(type(dicts["created_at"]), str)
        self.assertEqual(type(dicts["updated_at"]), str)

    def test_isoformat(self):
        """
            Checks conversion to iso.
        """
        state = State()
        time_cr = datetime.now()
        time_up = datetime.now()
        state.created_at = time_cr
        state.updated_at = time_up
        dicts = state.to_dict()
        self.assertEqual(dicts["created_at"], time_cr.isoformat())
        self.assertEqual(dicts["updated_at"], time_up.isoformat())
        
#!/usr/bin/python3
"""
    Unit tests for BaseModel class.
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
import io
from time import sleep
from unittest.mock import patch
from os import path, remove


class Test_init(unittest.TestCase):
    """
        Class for testing __init__
    """
    def setUp(self):
        """
            Set up for each test.
        """
        pass

    def tearDown(self):
        """
            Clean up after each test.
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """
            Test instance creation.
        """
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))

    def test_attr_types(self):
        """
            Test attribute types.
        """
        bm = BaseModel()
        self.assertEqual(bm.id, str)
        self.assertEqual(bm.created_at, datetime)
        self.assertEqual(bm.updated_at, datetime)

    def test_id_unique(self):
        """
            Test id uniqueness.
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        bm3 = BaseModel()
        bm4 = BaseModel()
        self.assertFalse(bm1.id == bm2.id)
        self.assertFalse(bm1.id == bm3.id)
        self.assertFalse(bm1.id == bm4.id)
        self.assertFalse(bm2.id == bm3.id)
        self.assertFalse(bm2.id == bm4.id)
        self.assertFalse(bm3.id == bm4.id)

    def test_clargs(self):
        """
            Test that args is working.
        """
        bm1 = BaseModel(1)
        bm2 = BaseModel(1, "Bendito")
        bm3 = BaseModel(1, "Bendito", (1, 2))
        bm4 = BaseModel(1, "Bendito", (1, 2), [1, 2])

    def test_def_attr(self):
        """
            Test default attributes.
        """
        bm1 = BaseModel(1, "Bendito", (1, 2), [1, 2])
        self.assertTrue(hasattr(bm1, "id"))
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))

    def test_instantiation_with_kwargs(self):
        """
            Test instantiation with kwargs.
        """
        key_id = {"id": "43ff8bae-dbe6-4a99-bc27-6ffa7f26caef",
                  "created_at": "2021-11-13T01:16:36.442329",
                  "updated_at": "2021-11-13T01:16:36.442382",
                  "class_": "BaseModel"}
        bm1 = BaseModel(**key_id)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertTrue(hasattr(bm1, "__class__"))
        self.assertTrue(bm1.__class__ not in bm1.__dict__)
        self.assertEqual(bm1.id, key_id["id"])
        self.assertEqual(bm1.created_at.isoformat(),
                         key_id["created_at"])
        self.assertEqual(bm1.updated_at.isoformat(),
                         key_id["updated_at"])

    def test_instantiation_without_kwargs_and_args(self):
        """
            Test instantiation without kwargs and args.
        """
        data_m = {"name": "Bendito"}
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "id"))
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertEqual(bm1.name, "Bendito")

    def test_date_conv_to_str(self):
        """
            Test date conversion to string.
        """
        key_id = {"id": "43ff8bae-dbe6-4a99-bc27-6ffa7f26caef",
                  "created_at": "2021-11-13T01:16:36.442329",
                  "updated_at": "2021-11-13T01:16:36.442382",
                  "class_": "BaseModel"}
        bm1 = BaseModel(**key_id)
        self.assertEqual(bm1.created_at.isoformat(),
                         key_id["created_at"])
        self.assertEqual(bm1.updated_at.isoformat(),
                         key_id["updated_at"])
        self.assertEqual(type(bm1.created_at), datetime)
        self.assertEqual(type(bm1.updated_at), datetime)

    def test_kwars_works_with_args(self):
        """
            Test kwargs works even in the
            presence of args.
        """
        key_id = {"id": "43ff8bae-dbe6-4a99-bc27-6ffa7f26caef",
                  "created_at": "2021-11-13T01:16:36.442329",
                  "updated_at": "2021-11-13T01:16:36.442382",
                  "class_": "BaseModel"}
        bm1 = BaseModel(1, "Bendito", ["Francis"], **key_id)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertTrue(hasattr(bm1, "__class__"))
        self.assertTrue(bm1.__class__ not in bm1.__dict__)
        self.assertEqual(bm1.id, key_id["id"])
        self.assertEqual(bm1.created_at.isoformat(),
                         key_id["created_at"])
        self.assertEqual(bm1.updated_at.isoformat(),
                         key_id["updated_at"])

    class Test_str__(unittest.TestCase):
        """
            Test __str__ method.
        """
        def setUp(self):
            """
                Set up.
            """
            pass

        def tearDown(self):
            """
                Tear down.
            """
            try:
                remove("file.json")
            except:
                pass

        def test_print_uno(self):
            """
                Test __str__ method.
            """
            bm = BaseModel()
            string = "[{:s}] ({:s}) {:s}\n"
            string = string.format(bm.__class__.__name__,
                                   bm.id,
                                   str(bm.__dict__))
            with patch("sys.stdout", new=io.StringIO()) as f:
                print(bm)
                str_test = f.getvalue()
                self.assertEqual(str_test, string)

        def test_print_dos(self):
            """
                Test __str__ method.
            """
            bm = BaseModel()
            bm.name = "Bendito"
            bm.code = 6969
            string = "[{:s}] ({:s}) {:s}\n"
            string = string.format(bm.__class__.__name__,
                                   bm.id,
                                   str(bm.__dict__))
            with patch("sys.stdout", new=io.StringIO()) as f:
                print(bm)
                str_test = f.getvalue()
                self.assertEqual(str_test, string)

        def test_print_clargs(self):
            """
                Test __str__ method with clargs.
            """
            bm = BaseModel(None, 1, ["Bendito"])
            bm.name = "Frances"
            bm.code = 6969
            string = "[{:s}] ({:s}) {:s}\n"
            string = string.format(bm.__class__.__name__,
                                   bm.id,
                                   str(bm.__dict__))
            with patch("sys.stdout", new=io.StringIO()) as f:
                print(bm)
                str_test = f.getvalue()
                self.assertEqual(str_test, string)

        def test_print_kwargs(self):
            """
                Test __str__ method with kwargs.
            """
            key_id = {"id": "43ff8bae-dbe6-4a99-bc27-6ffa7f26caef",
                      "created_at": "2021-11-13T01:16:36.442329",
                      "updated_at": "2021-11-13T01:16:36.442382",
                      "class_": "BaseModel"}
            bm = BaseModel(**key_id)
            string = "[{:s}] ({:s}) {:s}\n"
            string = string.format(bm.__class__.__name__,
                                   bm.id,
                                   str(bm.__dict__))
            with patch("sys.stdout", new=io.StringIO()) as f:
                print(bm)
                str_test = f.getvalue()
                self.assertEqual(str_test, string)

    class Test_save(unittest.TestCase):
        """
            Test save method.
        """
        def setUp(self):
            """
                Set up.
            """
            pass

        def tearDown(self):
            """
                Tear down.
            """
            try:
                remove("file.json")
            except:
                pass

        def test_save(self):
            """
                Test save method.
            """
            bm = BaseModel()
            time_cr = bm.created_at
            time_up = bm.updated_at
            sleep(0.5)
            bm.save()
            self.assertFalse(time_up == bm.updated_at)
            self.assertTrue(time_cr == bm.created_at)

        def test_save_type(self):
            """
                Test that save method type is of datetime.
            """
            bm = BaseModel()
            bm.save()
            self.assertEqual(type(bm.created_at), datetime)
            self.assertEqual(type(bm.updated_at), datetime)

    class Test_to_dict(unittest.TestCase):
        """
            Test to_dict method.
        """
        def setUp(self):
            """
                Set up.
            """
            pass

        def tearDown(self):
            """
                Tear down.
            """
            try:
                remove("file.json")
            except:
                pass

        def test_to_dict(self):
            """
                Test to_dict method.
            """
            bm = BaseModel()
            bm.name = "Bendito"
            bm.code = 6969
            dada = {}
            dada["id"] = bm.id
            dada["created_at"] = bm.created_at.isoformat()
            dada["updated_at"] = bm.updated_at.isoformat()
            dada["name"] = bm.name
            dada["code"] = bm.code
            dada_dict = bm.to_dict()
            self.assertEqual(dada["id"], dada_dict["id"])
            self.assertEqual(dada["created_at"], dada_dict["created_at"])
            self.assertEqual(dada["updated_at"], dada_dict["updated_at"])
            self.assertEqual(dada["name"], dada_dict["name"])
            self.assertEqual(dada["code"], dada_dict["code"])

        def test_class_date_conv(self):
            """
                Test that to_dict method converts datetime to string.
            """
            bm = BaseModel()
            dict = bm.to_dict()
            self.assertEqual(dict["__class__"], "BaseModel")
            self.assertEqual(type(dict["created_at"]), str)
            self.assertEqual(type(dict["updated_at"]), str)

        def test_date_isoformat(self):
            """
                Test that to_dict method converts datetime to string.
            """
            bm = BaseModel()
            time_cr = datetime.now()
            time_up = datetime.now()
            bm.created_at = time_cr
            bm.updated_at = time_up
            dict = bm.to_dict()
            self.assertEqual(dict["created_at"], time_cr.isoformat())
            self.assertEqual(dict["updated_at"], time_up.isoformat())

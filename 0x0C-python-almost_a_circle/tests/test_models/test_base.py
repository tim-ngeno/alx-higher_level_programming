#!/usr/bin/python3
"""Unit tests for module `base`"""
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Defines the test cases for module 'base'
    """

    def test_base_no_argument(self):
        """
        Test for base class without argument, verify id instance
        is initialized to 1
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_increment(self):
        """Test to ensure unique id assignment for new instance"""
        b2 = Base()
        self.assertTrue(b2.id > 1)

    def test_base_one_argument(self):
        """Test for Base class initialized with id argument"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_json_serialization(self):
        """Convert a list of dictionaries to JSON string"""
        a = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        b = Base.to_json_string(a)
        self.assertEqual(
            b, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        )

    def test_to_json_string_empty(self):
        """Test for empty list passed to json serialize method"""
        a = []
        self.assertEqual(Base.to_json_string(a), '[]')

    def test_to_json_string_none(self):
        """Test for None passed as argument to convert"""
        a = None
        self.assertEqual(Base.to_json_string(a), '[]')

    def test_json_deserialization(self):
        """Tests if resulting list matches json format"""
        json_str = '[{"x": 2, "width": 10, "id": 1, "height": 7}]'
        de_json = Base.from_json_string(json_str)
        self.assertEqual(
            de_json, [{"x": 2, "width": 10, "id": 1, "height": 7}]
        )

    def test_from_json_empty(self):
        """Test for conversion of empty string"""
        json_str = ""
        self.assertEqual(Base.from_json_string(json_str), [])

    def test_from_json_none(self):
        """Test for conversion of None"""
        json_str = None
        self.assertEqual(Base.from_json_string(json_str), [])

    def test_empty_child_instance(self):
        """Test for instance creation with no arguments"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_save_to_file(self):
        """Test that file exists and contains the correct content"""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(6, 7, 8, 9)
        Rectangle.save_to_file([r1, r2])
        pwd = os.getcwd()
        filepath = os.path.join(pwd, "Rectangle.json")
        self.assertTrue(os.path.exists(filepath))

        # check the content of the file
        with open(filepath, "r") as file:
            content = json.load(file)

        # Check for expected format (list)
        self.assertIsInstance(content, list)
        self.assertEqual(len(content), 2)

    def test_save_to_file_empty(self):
        """Test save to file with empty list"""
        empty = []
        Base.save_to_file(empty)
        filename = "{}.json".format(Base.__name__)
        self.assertTrue(os.path.exists(filename))

    def test_load_from_file(self):
        """Test loading from a file"""
        sample = '[{"id":1,"width":2,"height":6},{"id:2","width":5,"height":10}]'

        with open("Rectangle.json", "w") as file:
            file.write(sample)

        # load from json file
        objs = Base.load_from_file()

        self.assertIsInstance(objs, list)

    def test_load_from_file_none(self):
        """Test load from file with non-existent file"""
        objs = Base.load_from_file()
        self.assertEqual(objs, [])

    def test_load_from_file_empty(self):
        """Test load from file with empty JSON"""
        json_sample = ""
        objs = Base.load_from_file()
        self.assertEqual(objs, [])

    def test_load_from_file_invalid_json(self):
        """Test load file with invalid JSON data"""
        data = '()'
        objs = Base.load_from_file()
        self.assertEqual(objs, [])

    def test_create(self):
        """Test instance creation from dictionary"""
        attrs = {"id": 1, "width": 8, "height": 5, "x": 1, "y": 1}
        obj = Rectangle.create(**attrs)
        self.assertIsInstance(obj, Base)
        to_dict = obj.to_dictionary()
        self.assertDictEqual(attrs, to_dict)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unittest for module square"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the module `Square`"""

    def test_initialize(self):
        """Test correct initialization with correct attributes"""
        s = Square(2)
        self.assertEqual(s.size, 2)

    def test_initialize_noninteger(self):
        """Test to initialize with noninteger"""
        with self.assertRaises(TypeError):
            s = Square("5")

    def test_initialize_negative(self):
        """Test initialize with negative size"""
        with self.assertRaises(ValueError):
            s = Square(-9)

    def test_initialize_float(self):
        """Test initialize with float"""
        with self.assertRaises(TypeError):
            s = Square(5.6)

    def test_initialize_zero(self):
        """Test initialize with size 0"""
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_initialize_string_x(self):
        """Test initialize with string x"""
        with self.assertRaises(TypeError):
            s = Square(1, "5")

    def test_initialize_string_y(self):
        """Test initialize with string y"""
        with self.assertRaises(TypeError):
            s = Square(1, 2, "4")

    def test_initialize_negative_x(self):
        """Test initialize with negative x"""
        with self.assertRaises(ValueError):
            s = Square(1, -2)

    def test_initialize_negative_y(self):
        """Test initialize with negative y"""
        with self.assertRaises(ValueError):
            s = Square(1, 2, -4)

    def test_initialize_values(self):
        """Test for default values of x and y"""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_initialize_x_and_y(self):
        """Test case correct initialization with x and y"""
        s = Square(3, 4, 5)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_initialize_no_attrs(self):
        """Test instance creation with no attributes"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_getter(self):
        """Test the getter method"""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_setter_valid(self):
        """Test for modifying size value"""
        s = Square(5)
        s.size = 9
        self.assertEqual(s.size, 9)

    def test_setter_invalid(self):
        """Test setter method with invalid data"""
        s = Square(4)
        with self.assertRaises(ValueError):
            s.size = -9

    def test_setter_string(self):
        """Test setter method with wrong type data"""
        s = Square(9)
        with self.assertRaises(TypeError):
            s.size = "4"

    def test_setter_empty_string(self):
        """Test setter method with empty string"""
        s = Square(7)
        with self.assertRaises(TypeError):
            s.size = ""

    def test_setter_float(self):
        """Test setter method with float value"""
        s = Square(8)
        with self.assertRaises(TypeError):
            s.size = 5.67

    def test_setter_none(self):
        """Test for setter method with none"""
        s = Square(8)
        with self.assertRaises(TypeError):
            s.size = None

    def getter_x_default(self):
        """Test getter method for x vector"""
        s = Square(5)
        self.assertEqual(s.x, 0)

    def getter_x_value(self):
        """Test getter method for x with defined value"""
        s = Square(9, 8, 7)
        self.assertEqual(s.x, 8)

    def test_setter_x(self):
        """Test setter method for x vector"""
        s = Square(4)
        s.x = 5
        self.assertEqual(s.x, 5)

    def test_getter_y_default(self):
        """Test for getter method of y vector"""
        s = Square(6)
        self.assertEqual(s.y, 0)

    def test_getter_y_defined(self):
        """Test getter method for y vector with defined value"""
        s = Square(9, 8, 9)
        self.assertEqual(s.y, 9)

    def test_area(self):
        """Test for area method()"""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_area_present(self):
        """Test area method present"""
        with self.assertRaises(TypeError):
            Square.area()

    def test_update_id(self):
        """Test the update method on id"""
        s = Square(5)
        s.update(6)
        self.assertEqual(s.id, 6)

    def test_update_size(self):
        """Test update method for size"""
        s = Square(1, 9)
        s.update(1, 5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)

    def test_update_x_and_y(self):
        """Test update method x and y"""
        s = Square(6)
        s.update(6, 3, 4, 5)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_update_with_kwargs(self):
        """Test update method with kwargs"""
        s = Square(8)
        s.update(size=20, x=9, y=8)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 9)
        self.assertEqual(s.y, 8)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s = Square(2, 3, 4, 6)

        self.assertEqual(s.to_dictionary(), {
                         'id': 6, 'size': 2, 'x': 3, 'y': 4})

    def test_str_method(self):
        """Test __str__ method"""
        self.assertEqual(Square(3, 4, 5, 6).__str__(),
                         '[Square] (6) 4/5 - 3')

    def test_create(self):
        """Test creation of new Square"""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_size(self):
        """Test creation of new square with size"""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_create_with_x(self):
        """Test creation of new square with x vector"""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_create_with_x_y(self):
        """Test creation of new square with x,y vector"""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        """Test saving to file"""
        self.assertEqual(Square.save_to_file(None), None)

    def test_save_to_file_empty_list(self):
        """Test saving to file an empty list"""
        self.assertEqual(Square.save_to_file([]), None)

    def test_save_to_file_square(self):
        """Test saving square object to file"""
        self.assertEqual(Square.save_to_file([Square(1)]), None)

    def test_load_from_file(self):
        """Test loading from a file"""
        s = Square(4)
        s2 = Square(6)
        Square.save_to_file([s, s2])
        self.assertIsInstance(Square.load_from_file(), list)


if __name__ == "__main__":
    unittest.main()

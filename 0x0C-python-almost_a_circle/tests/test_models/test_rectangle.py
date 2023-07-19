#!/usr/bin/python3
"""Test cases for module Rectangle
"""
import sys
import unittest
from io import StringIO
from models.rectangle import Rectangle
MAX_INT = 10000


class TestRectangle(unittest.TestCase):
    """Test class for the Rectangle module"""

    def test_initialize(self):
        """Test that instances of the class are
        properly initialized
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

    def test_initialize_with_id(self):
        """Test initialization with id"""
        r = Rectangle(1, 2, 3, 4, 6)
        self.assertEqual(r.id, 6)

    def test_initialize_zero(self):
        """Test initialize with 0 for dimensions"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 0)

    def test_initialize_zero_width(self):
        """Test initialize with zero width"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_initialize_zero_height(self):
        """Test initialize with zero height"""
        with self.assertRaises(ValueError):
            r = Rectangle(2, 0)

    def test_initialize_negative(self):
        """Test initialization with negative values"""
        with self.assertRaises(ValueError):
            r = Rectangle(-3, -6)

    def test_initialize_negative_width(self):
        """Test initialize instance with negative width"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 3)

    def test_initialize_negative_height(self):
        """Test initialize with negative height"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_initialize_negative_y(self):
        """Test initialize negative y vector"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_initialize_noninteger_width(self):
        """Test initialize noninteger width"""
        with self.assertRaises(TypeError):
            r = Rectangle("4", 6)

    def test_initialize_noninteger_height(self):
        """Test initialize with non integer height"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, "4")

    def test_initialize_float(self):
        """Test initialize with floats"""
        with self.assertRaises(TypeError):
            r = Rectangle(2.4, 6, 8)

    def test_initialize_none(self):
        """Test initialize with none"""
        with self.assertRaises(TypeError):
            r = Rectangle(None, 5)

    def test_initialize_minimum_values(self):
        """Test initialize with minimum values"""
        r = Rectangle(1, 1, 0, 0)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_initialize_maximum_values(self):
        """Test initialize with maximum values"""
        r = Rectangle(MAX_INT, MAX_INT, MAX_INT, MAX_INT)
        self.assertEqual(r.width, MAX_INT)

    def test_width_getter(self):
        """Test property setter for width"""
        r = Rectangle(10, 12)
        self.assertEqual(r.width, 10)

    def test_width_setter(self):
        """Test width setter method"""
        r = Rectangle(12, 4)
        r.width = 7
        self.assertEqual(r.width, 7)

    def test_width_setter_noninteger(self):
        """Test width setter with non-integer"""
        r = Rectangle(12, 3)
        with self.assertRaises(TypeError):
            r.width = "string"

    def test_width_setter_invalid(self):
        """Test width setter with invalid value"""
        r = Rectangle(2, 4)
        with self.assertRaises(ValueError):
            r.width = -3

    def test_width_setter_empty(self):
        """Test width setter with empty value"""
        r = Rectangle(3, 5)
        with self.assertRaises(TypeError):
            r.width = ""

    def test_width_setter_none(self):
        """Test width setter with none type"""
        r = Rectangle(3, 5)
        with self.assertRaises(TypeError):
            r.width = None

    def test_width_setter_float(self):
        """Test width setter with float values"""
        r = Rectangle(12, 6)
        with self.assertRaises(TypeError):
            r.width = 6.88

    def test_height_getter(self):
        """Test getter method for height"""
        r = Rectangle(2, 6)
        self.assertEqual(r.height, 6)

    def test_height_setter(self):
        """Test height setter method"""
        r = Rectangle(2, 4)
        r.height = 9
        self.assertEqual(r.height, 9)

    def test_height_setter_noninteger(self):
        """Test height setter for non integer values"""
        r = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            r.height = "6"

    def test_height_setter_empty(self):
        """Test for height setter method with empty string"""
        r = Rectangle(12, 3)
        with self.assertRaises(TypeError):
            r.height = ""

    def test_height_setter_invalid(self):
        """Test setter for height with invalid data"""
        r = Rectangle(9, 8)
        with self.assertRaises(ValueError):
            r.height = -9

    def test_height_setter_float(self):
        """Test height setter with float values"""
        r = Rectangle(2, 6)
        with self.assertRaises(TypeError):
            r.height = 4.5

    def test_x_getter(self):
        """Test the getter method for x vector"""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.x, 3)

    def test_x_getter_default(self):
        """Test the getter method for x default values"""
        r = Rectangle(3, 5)
        self.assertEqual(r.x, 0)

    def test_x_setter_invalid(self):
        """Test for invalid x vector value"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -5, 0)

    def test_x_setter_none(self):
        """Test for none value for x  vector"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, None, 6)

    def test_x_setter_string(self):
        """Test x setter with string value"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "y", 8)

    def test_y_getter(self):
        """Test the getter method for y vector"""
        r = Rectangle(12, 4, 2, 3)
        self.assertEqual(r.y, 3)

    def test_y_getter_default(self):
        """Test default value for y getter method"""
        r = Rectangle(4, 5)
        self.assertEqual(r.y, 0)

    def test_y_setter_string(self):
        """Test for wrong type y vector value"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 5, "6")

    def test_y_setter_none(self):
        """Test for none value in y setter"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 4, None)

    def test_y_setter_invalid(self):
        """Test for invalid y vector value"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3 - 8)

    def test_y_setter_float(self):
        """Test for float value y vector"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 5.6)

    def test_area_present(self):
        """Test for area() method present"""
        with self.assertRaises(TypeError):
            Rectangle.area()

    def test_area(self):
        """Test the area method"""
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)

    def test_area_invalid(self):
        """Test for area with invalid width"""
        with self.assertRaises(TypeError):
            r = Rectangle("5", 4).area()

    def test_display_present(self):
        """Test display method present"""
        with self.assertRaises(TypeError):
            Rectangle.display()

    def test_display(self):
        """Test the display method"""
        r = Rectangle(2, 3)
        output = "##\n##\n##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), output)

    def test_display_with_x_y(self):
        """Test display with x and y values"""
        r = Rectangle(2, 3, 1, 1)
        output = "\n ##\n ##\n ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), output)

    def test_display_without_y(self):
        """Test display without y"""
        r = Rectangle(2, 2, 1)
        output = " ##\n ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), output)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r = Rectangle(2, 3, 1, 1, 10)
        self.assertEqual(
            r.to_dictionary(),
            {'id': 10, 'width': 2, 'height': 3, 'x': 1, 'y': 1}
        )

    def test_str(self):
        """Test the string representation of an instance"""
        self.assertEqual(Rectangle(2, 3, 4, 5, 7).__str__(),
                         '[Rectangle] (7) 4/5 - 2/3')

    def test_update_width(self):
        """Test case for update method"""
        b = Rectangle(3, 5, 6, 7)
        b.update(width=4)
        self.assertEqual(b.width, 4)
        self.assertEqual(b.height, 5)
        self.assertEqual(b.x, 6)
        self.assertEqual(b.y, 7)

    def test_update_height(self):
        """Test case for update height"""
        b = Rectangle(3, 5, 6, 7)
        b.update(height=9)
        self.assertEqual(b.width, 3)
        self.assertEqual(b.height, 9)
        self.assertEqual(b.x, 6)
        self.assertEqual(b.y, 7)

    def test_update_x(self):
        """Update x vector test"""
        b = Rectangle(3, 5, 6, 7)
        b.update(x=4)
        self.assertEqual(b.width, 3)
        self.assertEqual(b.height, 5)
        self.assertEqual(b.x, 4)
        self.assertEqual(b.y, 7)

    def test_update_y(self):
        """Test: update y vector"""
        b = Rectangle(3, 5, 6, 7)
        b.update(y=4)
        self.assertEqual(b.width, 3)
        self.assertEqual(b.height, 5)
        self.assertEqual(b.x, 6)
        self.assertEqual(b.y, 4)

    def test_update_width_height(self):
        """Test for updating width and height"""
        r = Rectangle(2, 3, 8)
        r.update(width=4, height=5)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)

    def test_update_args(self):
        """Test update with variable args"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(7, 8, 9, 10, 5)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 5)

    def test_update_args_varying_length(self):
        """Test variable args"""
        r = Rectangle(1, 2, 3)
        r.update(5, 6, 7)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)

    def test_update_only_id(self):
        """Test update only id with args"""
        r = Rectangle(3, 4, 5)
        r.update(5)
        self.assertEqual(r.id, 5)

    def test_update_only_width(self):
        """Test update only width"""
        r = Rectangle(2, 3, 4)
        r.update(2, 8, 4)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 8)

    def test_save_to_file_none(self):
        """Test saving None type to file"""
        with self.assertRaises(TypeError):
            self.assertEqual(Rectangle.save_to_file(None), None)

    def test_save_to_file_empty_list(self):
        """Test save empty list to file"""
        self.assertEqual(Rectangle.save_to_file([]), None)


if __name__ == "__main__":
    unittest.main()

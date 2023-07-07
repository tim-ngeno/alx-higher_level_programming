#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines the test cases for the max_integer module"""

    def test_ordered_list(self):
        """Test on ordered list of integers"""
        t = [1, 2, 3, 4]
        self.assertEqual(max_integer(t), 4)

    def test_unordered_list(self):
        """Test on unordered list of integers"""
        t = [1, 4, 3, 2]
        self.assertEqual(max_integer(t), 4)

    def test_first_is_max(self):
        """Test when the first item is highest"""
        t = [4, 3, 2, 1]
        self.assertEqual(max_integer(t), 4)

    def test_one_item(self):
        """Test if list has only one item"""
        t = [7]
        self.assertEqual(max_integer(t), 7)

    def test_negative(self):
        """Test for list of negative numbers"""
        t = [-2, -6, -56]
        self.assertEqual(max_integer(t), -2)

    def test_isinteger(self):
        """Test if all members of input list are type int"""
        a_list = [1, 2, 3, 4]
        self.assertIsInstance((all(a_list)), int)

    def test_empty_list(self):
        """Test case on an empty list"""
        t = []
        self.assertEqual(max_integer(t), None)

    def test_floats(self):
        """Test floating point numbers"""
        t = [1.23, 4.56, 7.89, 15.6]
        self.assertEqual(max_integer(t), 15.6)

    def test_floats_and_ints(self):
        """Test floats and integers"""
        t = [1, 3.5, 56, 78.9]
        self.assertEqual(max_integer(t), 78.9)

    def test_strings_list(self):
        """Test for list of strings"""
        strings = ["a", "b", "c"]
        self.assertEqual(max_integer(strings), "c")

    def test_string(self):
        """Test for a string type"""
        t = "String"
        self.assertEqual(max_integer(t), "t")

    def test_empty_string(self):
        """Test for an empty string"""
        self.assertEqual(max_integer(""), None)

    def test_strings_and_numbers(self):
        """Test for list of strings and numbers"""
        t = ["a", 3]
        with self.assertRaises(TypeError):
            max_integer(t)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Tests for the Square Class"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Class for the Square Class"""

    def test_create_instance_with_valid_arguments(self):
        """tests for valid arguments"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_create_instance_with_invalid_arguments(self):
        """tests for invalid arguments"""
        with self.assertRaises(ValueError):
            s1 = Square(0)

    # Add more test cases for other methods as needed


if __name__ == '__main__':
    unittest.main()

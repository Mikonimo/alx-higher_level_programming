#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for Rectangle"""
    def test_create_instance_with_valid_arguments(self):
        """Tests valid arguments"""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)

    def test_create_instance_with_invalid_arguments(self):
        """Tests for invalid arguments"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 5)
            r2 = Rectangle(5, 0)

    # Add more test cases for other methods as needed


if __name__ == '__main__':
    unittest.main()

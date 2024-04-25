#!/usr/bin/python3
"""Tests for the Base class and its methods"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for base class"""
    def test_create_instance_with_id(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

    def test_create_instance_without_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)


if __name__ == '__main__':
    unittest.main()

__author__ = 'santa'

from src.point import *
import unittest
import math


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.a = Point(10.5, 20.5)

    def test_validate_float(self):
        self.assertEqual(Point._validate(100.5), 100.5)
        self.assertEqual(type(Point._validate(100.5)), float)

        with self.assertRaises(ValueError):
            Point._validate('incorrect input: not float type')

    def test_init(self):
        self.assertEqual(self.a._x, 10.5)
        self.assertEqual(self.a._y, 20.5)

        with self.assertRaises(ValueError):
            b = Point('10.0a', 15.0)

        with self.assertRaises(ValueError):
            b = Point(10.0, '15.0a')

    def test_property_and_setters(self):
        self.assertEqual(self.a.x, 10.5)
        self.assertEqual(self.a.y, 20.5)

        self.a.x = 30.0
        self.a.y = 40.0

        self.assertEqual(self.a.x, 30.0)
        self.assertEqual(self.a.y, 40.0)

    def test_distance(self):
        b = Point(50.0, 60.0)

        self.assertEqual(
            self.a.distance(b),
            math.sqrt((self.a.x - b.x) ** 2 + (self.a.y - b.y) ** 2)
        )

        c = Point(-90.0, 50.0)
        self.assertEqual(
            c.distance(b),
            math.sqrt((c.x - b.x) ** 2 + (c.y - b.y) ** 2)
        )

    def test_str_repr(self):
        self.assertEqual('(10.5, 20.5)', str(self.a))
        self.assertEqual('Point (10.5, 20.5)', repr(self.a))

    def test_comparison_oper(self):
        b = Point(10.5, 20.5)
        c = Point(15.0, 20.0)

        self.assertTrue(self.a == b)
        self.assertFalse(self.a == c)
        self.assertTrue(self.a != c)
        self.assertFalse(self.a != b)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
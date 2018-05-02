__author__ = 'santa'

from src.car import *
from src.point import *
import unittest


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car_default = Car()
        self.car_taz = Car(50, 0.9, Point(10.0, 10.0), 'Taz')

    def test_init(self):
        self.assertEqual(self.car_default._model, 'Mercedes')
        self.assertEqual(self.car_default._fuel_consumption, 0.6)
        self.assertEqual(self.car_default._fuel_capacity, 60.0)
        self.assertEqual(self.car_default._fuel_amount, 0.0)
        self.assertEqual(str(self.car_default._location), '(0.0, 0.0)')

        self.assertEqual(self.car_taz._model, 'Taz')
        self.assertEqual(self.car_taz._fuel_consumption, 0.9)
        self.assertEqual(self.car_taz._fuel_capacity, 50.0)
        self.assertEqual(self.car_taz._fuel_amount, 0.0)
        self.assertEqual(str(self.car_taz._location), '(10.0, 10.0)')

        with self.assertRaises(ValueError):
            porsche = Car('incorrect data', 10.0, Point(0.0, 0.0), 'Porsche')
        with self.assertRaises(ValueError):
            porsche = Car(100.0, 'incorrect data', Point(0.0, 0.0), 'Porsche')

        with self.assertRaises(TypeError):
            porsche = Car(100.0, 10.0, 0.0, 'Porsche')
        with self.assertRaises(TypeError):
            porsche = Car(100.0, 10.0, Point(0.0, 0.0), 1)

        porsche = Car(-100.0, -10, Point(10.0,10.0), 'Porsche')
        self.assertEqual(porsche._fuel_consumption, 10.0, 'Negative fuel consumption!')
        self.assertEqual(porsche._fuel_capacity, 100.0, 'Negative fuel capacity!')

    def test_getters(self):
        self.assertEqual(self.car_default.model, 'Mercedes')
        self.assertEqual(self.car_default.fuel_capacity, 60.0)
        self.assertEqual(self.car_default.fuel_amount, 0.0)
        self.assertEqual(self.car_default.fuel_consumption, 0.6)
        self.assertEqual(str(self.car_default.location), '(0.0, 0.0)')

    def test_refill(self):
        self.car_default.refill(60.0)
        self.assertEqual(self.car_default.fuel_amount, 60.0)

        with self.assertRaises(Warning):
            self.car_default.refill(40.0)

        with self.assertRaises(ValueError):
            self.car_default.refill(-5.0)

    def test_drive(self):
        b = Point(2.0, 2.0)
        self.car_default.refill(60.0)
        self.car_default.drive(b)
        distance = b.distance(Point(0.0, 0.0))

        self.assertEqual(
            self.car_default.fuel_amount,
            60.0 - (self.car_default.fuel_consumption * distance)
        )
        self.assertEqual(str(self.car_default.location), str(b))

        c = Point(200.0, 200.0)

        with self.assertRaises(Warning):
            self.car_default.drive(c)

    def test_str_repr(self):
        self.assertEqual(
            str(self.car_default),
            ('Model:			Mercedes\n'
            'Consumption:	0.6\n'
            'Location:		(0.0, 0.0)\n'
            'Fuel capacity:	60.0\n'
            'Fuel amount:	0.0000\n')
        )

        self.assertEqual(
            repr(self.car_default),
            'Car: Mercedes (consumption 0.6), fuel 0.0 (60.0), located at (0.0, 0.0)'
        )

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
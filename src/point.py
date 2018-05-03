"""Define Point class"""

__author__ = 'santa'
__all__ = (
    'Point',
)

from math import hypot


class Point:
    """
    Class provide creating and working with two-dimensional geometric point.

    :Usage:
    :>>> point = Point(2.0, 5.0)
    :>>> print(point)
    (2.0, 5.0)
    :>>> print(point.x)
    2.0
    :>>> print(point.y)
    5.0
    :>>> point.x = 12.0
    :>>> point.y = 15.0
    :>>> print(point.x)
    12.0
    :>>> print(point.y)
    15.0
    :>>> other_point = Point(20.0, 30.0)
    :>>> print(point.distance(other_point))
    17.0
    :>>> print(point == other_point)
    False
    :>>> print(point != other_point)
    True
    """

    @staticmethod
    def _validate(value):
        """
        Validate if value can be convert to float.

        :param value: Value to validate
        :type value: Any numerical type that can be converted to float
        :raise ValueError: If value can't be converted to float
        :return: value converted to float
        :rtype: float
        """

        try:
            return float(value)
        except ValueError as e:
            e.args = (e.args[0],'Value entered can not be convert to float')
            raise

    def __init__(self, x=0, y=0):
        """
        The initializer.

        :param x: x-coordinate of point, 0 by default
        :type x: Any string or numerical type that can be converted to float
        :param y: y-coordinate of point, 0 by default
        :type y: Any string or numerical type that can be converted to float
        :raise ValueError: If x or y can't be converted to float
        """

        self._x = Point._validate(x)
        self._y = Point._validate(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = Point._validate(value)

    @y.setter
    def y(self, value):
        self._y = Point._validate(value)

    def distance(self, other):
        """
        Calculate distance to other point.

        :param other: point to which distance from original point should be calculated
        :type other: Point
        :return: distance between original and other points
        :rtype: float
        """
        return hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return str('({0}, {1})'.format(self.x, self.y))

    def __repr__(self):
        return str('Point ({0}, {1})'.format(self.x, self.y))

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def __ne__(self, other):
        return self._x != other._x or self._y != other._y

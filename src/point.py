__author__ = 'santa'

__all__ = (
    'Point',
)

from math import hypot


class Point:
    @staticmethod
    def _validate(value):
        # return float(value)
        try:
            return float(value)
        except ValueError as e:
            e.args = (e.args[0],'Value entered can not be convert to float')
            raise

    def __init__(self, x, y):
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
        return hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return str('({0}, {1})'.format(self.x, self.y))

    def __repr__(self):
        return str('Point ({0}, {1})'.format(self.x, self.y))

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def __ne__(self, other):
        return self._x != other._x or self._y != other._y

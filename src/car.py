__author__ = 'santa'

__all__ = (
    'Car',
)

from src.point import Point
from math import fabs


class Car:
    @staticmethod
    def _validate_float(value):
        try:
            return float(value)
        except ValueError as e:
            e.args = (e.args[0], 'Value entered can not be convert to float')
            raise

    @staticmethod
    def _validate_string(value):
        if isinstance(value, str):
            return value
        else:
            raise TypeError(f'Incorrect field type: {type(value)} instead of {str}')

    @staticmethod
    def _validate_point(value):
        if isinstance(value, Point):
            return value
        else:
            raise TypeError(f'Incorrect field type: {type(value)} instead of {type(Point)}')

    def __init__(self, capacity=60, consumption=0.6, location=Point(0, 0), model='Mercedes'):
        self._fuel_capacity = fabs(self._validate_float(capacity))
        self._fuel_consumption = fabs(self._validate_float(consumption))
        self._location = self._validate_point(location)
        self._model = self._validate_string(model)
        self._fuel_amount = float(0.0)

    @property
    def fuel_amount(self):
        return self._fuel_amount

    @property
    def fuel_capacity(self):
        return self._fuel_capacity

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @property
    def location(self):
        return self._location

    @property
    def model(self):
        return self._model

    def refill(self, fuel):
        fuel = self._validate_float(fuel)
        if fuel < 0:
            raise ValueError('Negative quantity of fuel!')


        if self._fuel_capacity - self._fuel_amount < fuel:
            raise Warning('Too much fuel! Refill was not started!')
        else:
            self._fuel_amount += fuel

    def _drive(self, destination):
        destination = self._validate_point(destination)

        distance = self.location.distance(destination)
        fuel_needed = self.fuel_consumption * distance

        if self._fuel_amount < fuel_needed:
            raise Warning('Not enough fuel! Drive was not started!')
        else:
            self._fuel_amount -= fuel_needed
            self._location = destination

    def drive(self, *args):
        if isinstance(args[0], Point):
            self._drive(args[0])
        else:
            self._drive(Point(args[0], args[1]))


    def __str__(self):
        presentation =  (
            f'Model:\t\t\t{self.model}\n'
            f'Consumption:\t{self.fuel_consumption}\n'
            f'Location:\t\t{self.location}\n'
            f'Fuel capacity:\t{self.fuel_capacity}\n'
            f'Fuel amount:\t{self.fuel_amount:.4f}\n'
        )
        return presentation

    def __repr__(self):
        presentation = (f'Car: {self.model} (consumption {self.fuel_consumption}), '
                        f'fuel {self.fuel_amount} ({self.fuel_capacity}), '
                        f'located at {self.location}')

        return presentation

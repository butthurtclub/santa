"""Define Car class"""

__author__ = 'santa'
__all__ = (
    'Car',
)

from src.point import Point
from math import fabs


class Car:
    """
    Create car and provide refill and drive capabilities

    Usage:
    :>>> point = Point(1.0, 1.0)
    :>>> car = Car(100.0, 0.9, point, 'BMW')
    :>>> car.refill(80)
    :>>> print(car.model)
    BMW
    :>>> print(car.location)
    (1.0, 1.0)
    :>>> print(car.fuel_consumption)
    0.9
    :>>> print(car.fuel_capacity)
    100.0
    :>>> print(car.fuel_amount)
    80.0
    :>>> car.drive(Point(5.0, 5.0))
    :>>> car.drive(10.0, 10.0)
    :>>> print(car)
    Model:			BMW
    Consumption:	0.9
    Location:		(10.0, 10.0)
    Fuel capacity:	100.0
    Fuel amount:	68.5449
    """

    @staticmethod
    def _validate_float(value):
        """
        Validate if value can be convert to float.

        :param value: Value to validate
        :type value: Any string or numerical type that can be converted to float
        :raise ValueError: If value can't be converted to float
        :return: value converted to float
        :rtype: float
        """

        try:
            return float(value)
        except ValueError as e:
            e.args = (e.args[0], 'Value entered can not be convert to float')
            raise

    @staticmethod
    def _validate_string(value):
        """
        Validate if value is string.

        :param value: Value to validate
        :type value: Str
        :raise TypeError: If value is not string
        :return: value if string
        :rtype: str
        """

        if isinstance(value, str):
            return value
        else:
            raise TypeError(f'Incorrect field type: {type(value)} instead of {str}')

    @staticmethod
    def _validate_point(value):
        """
        Validate if value is of Point type.

        :param value: Object to validate
        :type value: Point
        :raise TypeError: If value is not of Point type
        :return: value if Point type
        :rtype: Point
        """

        if isinstance(value, Point):
            return value
        else:
            raise TypeError(f'Incorrect field type: {type(value)} instead of {type(Point)}')

    def __init__(self, capacity=60, consumption=0.6, location=Point(0, 0), model='Mercedes'):
        """
        The initializer.

        :param capacity: Capacity of fuel tank of car. By default: 60.
        :type capacity: Any string or numerical type that can be converted to float
        :param consumption: Consumption of fuel by car: liter/km. By default: 0.6.
        :type consumption: Any string or numerical type that can be converted to float
        :param location: Initial location of car
        :type location: Point
        :param model: Name of car
        :type model: str
        :raise ValueError: If capacity or fuel consumption can't be converted to float
        :raise TypeError: If location is not of Point type
        :raise TypeError: If model is not of str type

        :fuel amount: Initial fuel amount is float 0.0
        """

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
        """
        Refill car with fuel after validation of input fuel.

        :param fuel: Quantity of fuel to be refilled
        :type fuel: float
        :raise ValueError: If fuel received is negative
        :raise Warning: If fuel received is more than capacity available
        :return: None
        :rtype: None
        """

        fuel = self._validate_float(fuel)
        if fuel < 0:
            raise ValueError('Negative quantity of fuel!')


        if self._fuel_capacity - self._fuel_amount < fuel:
            raise Warning('Too much fuel! Refill was not started!')
        else:
            self._fuel_amount += fuel

    def _drive(self, destination):
        """
        Drive car to destination point.

        :param destination: Point to which car should be driven by straight line
        :type destination: Point
        :raise TypeError: If destination is not of Point type
        :raise Warning: If car do not have enough fuel to drive to destination
        :return: None
        :rtype: None
        """

        destination = self._validate_point(destination)

        distance = self.location.distance(destination)
        fuel_needed = self.fuel_consumption * distance

        if self._fuel_amount < fuel_needed:
            raise Warning('Not enough fuel! Drive was not started!')
        else:
            self._fuel_amount -= fuel_needed
            self._location = destination

    def drive(self, *args):
        """
        Drive car to destination point after validating/converting *args to Point

        :param args[0]: Point to which car should be driven by straight line or x-coordinate of point needed
        :type args[0]: Point or float
        :param args[1]: y-coordinate of point needed. Next args are ignored.
        :type args[1]: float
        :raise ValueError: If args[0] or args[0] can't be converted to float
        :raise Warning: If car do not have enough fuel to drive to destination
        :return: None
        :rtype: None
        """

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

"""Define Unit class and UnitIsDead exception"""

__author__ = 'santa'
__all__ = (
    'Unit',
    'UnitIsDead'
)

from math import fabs


class UnitIsDead(Exception):
    pass


class Unit:
    """
    Define Unit with state params and attack, take damage, add hit points capabilities

    Usage:
    :>>> unit = Unit('Name', hit_points=200, damage=10)
    :>>> print(unit.name)
    Name
    :>>> print(unit.hit_points)
    200.0
    :>>> print(unit.hit_points_limit)
    200.0
    :>>> print(unit.damage)
    10.0
    :>>> enemy = Unit('Enemy')
    :>>> print(enemy)
    Name (damage):		Enemy(40.0)
    Hit points (limit):	200.0(200.0)
    :>>> unit.attack(enemy)
    :>>> print(unit.hit_points)
    180.0
    :>>> print(enemy.hit_points)
    190.0
    :>>> unit.add_hit_points(20)
    :>>> print(unit.hit_points)
    200.0
    """

    @staticmethod
    def _validate_int(value):
        """
        Validate if value can be convert to int.

        :param value: Value to validate
        :type value: Any string or numerical type that can be converted to int
        :raise ValueError: If value can't be converted to int
        :return: value converted to int
        :rtype: int
        """

        try:
            return int(value)
        except ValueError as e:
            e.args = (e.args[0], ('Value can not be convert to int'))
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
    def _validate_unit_type(unit):
        """
        Validate if unit is of Unit type.

        :param unit: Object to validate
        :type unit: Unit
        :raise TypeError: If unit is not of Unit type
        :return: unit if Unit type
        :rtype: Unit
        """

        if isinstance(unit, Unit):
            return unit
        else:
            raise TypeError(f'Incorrect field type: {type(unit)} instead of {type(Unit)}')

    def __init__(self, name, hit_points=200, damage=40):
        """
        The initializer.

        :param name: Name of unit
        :type name: str
        :param hit_points: Current and maximum hit points of unit. Abs from input is taken. By default: 200.
        :type hit_points: Any string or numerical type that can be converted to int.
        :param damage: Damage unit make to other unit during attack. Abs from input is taken. By default: 40.
        :type damage: Any string or numerical type that can be converted to int.
        :raise ValueError: If hit_points or damage can't be converted to int
        :raise TypeError: If name is not of str type
        """

        self._name = self._validate_string(name)
        self._hit_points = fabs(self._validate_int(hit_points))
        self._hit_points_limit = self.hit_points
        self._damage = fabs(self._validate_int(damage))

    def _ensure_is_alive(self):
        """
        Check if unit is alive.

        :raise UnitIsDead: If hit_points_amount is zero.
        """

        if self._hit_points == 0:
            raise UnitIsDead

    @property
    def name(self):
        return self._name

    @property
    def hit_points(self):
        return self._hit_points

    @property
    def hit_points_limit(self):
        return self._hit_points_limit

    @property
    def damage(self):
        return self._damage



    def add_hit_points(self, hp):
        """
        Increase hit points after validation of input hp.

        :param hp: Quantity of hit points to be added. Abs is taken.
        :type hp: int
        :raise ValueError: If hp can't be converted to int.
        :raise UnitIsDead: If unit's hit points is zero.
        :return: None
        :rtype: None
        """

        new_hit_points = self._hit_points + fabs(self._validate_int(hp))

        self._ensure_is_alive()
        if new_hit_points > self._hit_points_limit:
            self._hit_points = self._hit_points_limit
        else:
            self._hit_points = new_hit_points

    def _take_damage(self, dmg):
        """
        Decrease hit points after validation of input dmg.

        :param dmg: Quantity of hit points to be decreased. Abs is taken.
        :type dmg: int
        :raise ValueError: If dmg can't be converted to int.
        :raise UnitIsDead: If unit's hit points is zero.
        :return: None
        :rtype: None
        """

        dmg = fabs(self._validate_int(dmg))

        self._ensure_is_alive()
        if dmg > self._hit_points:
            self._hit_points = 0
        else:
            self._hit_points -= dmg

    def attack(self, enemy):
        """
        Decrease enemy's hit points for unit's damage and call counterattack method.

        :param enemy: Unit is attacked
        :type enemy: Unit
        :raise TypeError: If enemy is not of Unit type.
        :raise UnitIsDead: If unit's or enemy's hit points is zero.
        :return: None
        :rtype: None
        """

        enemy = self._validate_unit_type(enemy)

        self._ensure_is_alive()
        enemy._ensure_is_alive()

        enemy._take_damage(self._damage)
        enemy._ensure_is_alive()
        enemy._counter_attack(self)

    def _counter_attack(self, enemy):
        """
        Call attack method with damage divided by 2.

        :param enemy: Unit is counterattacked
        :type enemy: Unit
        :raise TypeError: If enemy is not of Unit type.
        :raise UnitIsDead: If enemy's hit points is zero.
        :return: None
        :rtype: None
        """

        enemy._take_damage(self._damage / 2)

    def __str__(self):
        presentation = (
            f'Name (damage):\t\t{self.name}({self.damage})\n'
            f'Hit points (limit):\t{self.hit_points}({self.hit_points_limit})'
        )
        return presentation

    def __repr__(self):
        presentation = (
            f'Unit: {self.name}(dmg {self.damage}), '
            f'hp {self.hit_points}({self.hit_points_limit})'
        )
        return presentation

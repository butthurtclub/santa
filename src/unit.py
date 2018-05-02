__author__ = 'santa'

__all__ = (
    'Unit',
    'UnitIsDead'
)

from math import fabs


class UnitIsDead(Exception):
    pass


class Unit:
    @staticmethod
    def _validate_int(value):
        try:
            return int(value)
        except ValueError as e:
            e.args = (e.args[0], ('Value can not be convert to int'))
            raise

    @staticmethod
    def _validate_string(value):
        if isinstance(value, str):
            return value
        else:
            raise TypeError(f'Incorrect field type: {type(value)} instead of {str}')

    @staticmethod
    def _validate_unit_type(unit):
        if isinstance(unit, Unit):
            return unit
        else:
            raise TypeError(f'Incorrect field type: {type(unit)} instead of {type(Unit)}')

    def __init__(self, name, hit_points=200, damage=40):
        self._name = self._validate_string(name)
        self._hit_points = fabs(self._validate_int(hit_points))
        self._hit_points_limit = self.hit_points
        self._damage = fabs(self._validate_int(damage))

    def _ensure_is_alive(self):
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
        new_hit_points = self._hit_points + fabs(self._validate_int(hp))

        self._ensure_is_alive()
        if new_hit_points > self._hit_points_limit:
            self._hit_points = self._hit_points_limit
        else:
            self._hit_points = new_hit_points

    def take_damage(self, dmg):
        dmg = fabs(self._validate_int(dmg))

        self._ensure_is_alive()
        if dmg > self._hit_points:
            self._hit_points = 0
        else:
            self._hit_points -= dmg

    def attack(self, enemy):
        enemy = self._validate_unit_type(enemy)

        self._ensure_is_alive()
        enemy._ensure_is_alive()

        enemy.take_damage(self._damage)
        enemy._ensure_is_alive()
        enemy._counter_attack(self)

    def _counter_attack(self, enemy):
        enemy.take_damage(self._damage / 2)

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

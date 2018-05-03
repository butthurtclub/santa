__author__ = 'santa'

from src.unit import *
import unittest


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.soldier = Unit('Soldier', 100, 20)
        self.sergeant = Unit('Sergeant')

    def test_init(self):
        self.assertEqual(self.soldier._name, 'Soldier')
        self.assertEqual(self.soldier._hit_points, 100)
        self.assertEqual(self.soldier._hit_points_limit, 100)
        self.assertEqual(self.soldier._damage, 20)

        self.assertEqual(self.sergeant._name, 'Sergeant')
        self.assertEqual(self.sergeant._hit_points, 200)
        self.assertEqual(self.sergeant._hit_points_limit, 200)
        self.assertEqual(self.sergeant._damage, 40)

        with self.assertRaises(TypeError):
            lieutenant = Unit()
        with self.assertRaises(TypeError):
            lieutenant = Unit(1, 200, 40)

        with self.assertRaises(ValueError):
            lieutenant = Unit('Lieutenant', 'incorrect data', 40)

        with self.assertRaises(ValueError):
            lieutenant = Unit('Lieutenant', 100, 'incorrect data')

        lieutenant = Unit('Lieutenant', -200, -40)
        self.assertEqual(lieutenant._name, 'Lieutenant')
        self.assertEqual(lieutenant._hit_points, 200)
        self.assertEqual(lieutenant._hit_points_limit, 200)
        self.assertEqual(lieutenant._damage, 40)

    def test_ensure_is_alive(self):
        self.soldier._ensure_is_alive()
        self.soldier._take_damage(100)

        with self.assertRaises(UnitIsDead):
            self.soldier._ensure_is_alive()

    def test_getters(self):
        self.assertEqual(self.soldier.name, 'Soldier')
        self.assertEqual(self.soldier.hit_points, 100)
        self.assertEqual(self.soldier.hit_points_limit, 100)
        self.assertEqual(self.soldier.damage, 20)

    def test_add_hp(self):
        self.soldier.add_hit_points(20)
        self.assertEqual(self.soldier.hit_points, 100)

        self.soldier._hit_points -= 50
        self.soldier.add_hit_points(40)
        self.assertEqual(self.soldier.hit_points, 90)

        self.soldier.add_hit_points(-40)
        self.assertEqual(self.soldier.hit_points, 100)

        self.soldier._hit_points -= 100
        with self.assertRaises(UnitIsDead):
            self.soldier.add_hit_points(40)

    def test_take_damage(self):
        self.soldier._take_damage(50)
        self.assertEqual(self.soldier.hit_points, 50)

        self.soldier._take_damage(-60)
        self.assertEqual(self.soldier.hit_points, 0)

        with self.assertRaises(UnitIsDead):
            self.soldier._take_damage(60)

    def test_attack(self):
        self.sergeant.attack(self.soldier)
        self.assertEqual(self.sergeant._hit_points, 190)
        self.assertEqual(self.soldier._hit_points, 60)

        self.sergeant.attack(self.soldier)
        self.assertEqual(self.sergeant._hit_points, 180)
        self.assertEqual(self.soldier._hit_points, 20)

        with self.assertRaises(UnitIsDead):
            self.sergeant.attack(self.soldier)
        self.assertEqual(self.sergeant._hit_points, 180)
        self.assertEqual(self.soldier._hit_points, 0)

        with self.assertRaises(UnitIsDead):
            self.sergeant.attack(self.soldier)

        self.assertEqual(self.sergeant._hit_points, 180)
        self.assertEqual(self.soldier._hit_points, 0)

    def test_str_repr(self):
        self.assertEqual(
            str(self.soldier),
            (f'Name (damage):		{self.soldier.name}({self.soldier.damage})\n'
             f'Hit points (limit):	{self.soldier.hit_points}({self.soldier.hit_points_limit})')
        )

        self.assertEqual(
            repr(self.soldier),
            f'Unit: Soldier(dmg {self.soldier.damage}), hp {self.soldier.hit_points}({self.soldier.hit_points_limit})'
        )

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
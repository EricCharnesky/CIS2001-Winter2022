from unittest import TestCase
from Ship import Ship, Repair, Battleship, Corvette, Alignment


class TestShip(TestCase):

    def test_ship_init(self):

        # arrange
        expected_name = "ship"
        expected_type = "Ship"
        expected_alignment = Alignment.US
        expected_x = 1
        expected_y = 2
        expected_max_health = 10
        expected_current_health = 10
        expected_attack_power = 10
        expected_attack_range = 10

        # act
        ship = Ship(expected_name, expected_x, expected_y, expected_alignment,
                    expected_max_health, expected_attack_range, expected_attack_power)
        actual_name = ship.get_name()
        actual_type = ship.get_type()
        actual_x = ship.get_x()
        actual_y = ship.get_y()
        actual_alignment = ship.get_alignment()
        actual_max_health = ship.get_max_health()
        actual_current_health = ship.get_current_health()
        actual_attack_power = ship.get_attack_power()
        actual_attack_range = ship.get_attack_range()

        # assert
        self.assertEqual(expected_name, actual_name )
        self.assertEqual(expected_type, actual_type)
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)
        self.assertEqual(expected_alignment, actual_alignment)
        self.assertEqual(expected_max_health, actual_max_health)
        self.assertEqual(expected_current_health, actual_current_health)
        self.assertEqual(expected_attack_power, actual_attack_power)
        self.assertEqual(expected_attack_range, actual_attack_range)

    def test_ship_attack_within_range(self):
        # arrange
        ship = Ship("", 0, 0, Alignment.US, 10, 10, 10)
        target = Ship("", 0, 0, Alignment.THEM, 10, 10, 10)
        expected_current_health = 0

        # act
        ship.attack(target)
        actual_current_health = target.get_current_health()

        # assert
        self.assertEqual(expected_current_health, actual_current_health)

    def test_ship_attack_not_within_range(self):
        # arrange
        ship = Ship("", 0, 0, Alignment.US, 10, 10, 10)
        target = Ship("", 10, 10, Alignment.THEM, 10, 10, 10)
        expected_current_health = 10

        # act
        ship.attack(target)
        actual_current_health = target.get_current_health()

        # assert
        self.assertEqual(expected_current_health, actual_current_health)

    def test_ship_attack_same_team(self):
        # arrange
        ship = Ship("", 0, 0, Alignment.US, 10, 10, 10)
        target = Ship("", 0, 0, Alignment.US, 10, 10, 10)
        expected_current_health = 10

        # act
        ship.attack(target)
        actual_current_health = target.get_current_health()

        # assert
        self.assertEqual(expected_current_health, actual_current_health)

    def test_ship_status(self):
        # arrange
        ship = Ship("test", 0, 0, Alignment.US, 10, 10, 10)
        expected_status = """test
type: Ship
health: 10
location: 0, 0"""

        # act
        actual_status = ship.status()

        # assert
        self.assertEqual(expected_status, actual_status)

    def test_ship_move(self):
        # arrange
        ship = Ship("test", 0, 0, Alignment.US, 10, 10, 10, 1, 1)
        ship.assess_damage(2)
        expected_current_health = 9
        expected_x = 1
        expected_y = 1

        # act
        ship.move()
        actual_current_health = ship.get_current_health()
        actual_x = ship.get_x()
        actual_y = ship.get_y()

        # assert
        self.assertEqual(expected_y, actual_y)
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_current_health, actual_current_health)

    def test_ship_assess_damage_does_not_go_below_0(self):
        # arrange
        ship = Ship("test", 0, 0, Alignment.US, 10, 10, 10)
        expected_current_health = 0

        # act
        ship.assess_damage(20)
        actual_current_health = ship.get_current_health()

        # assert
        self.assertEqual(expected_current_health, actual_current_health)

    def test_ship_assess_damage_does_not_go_above_max(self):
        # arrange
        ship = Ship("test", 0, 0, Alignment.US, 10, 10, 10)
        expected_current_health = 10

        # act
        ship.assess_damage(-1)
        actual_current_health = ship.get_current_health()

        # assert
        self.assertEqual(expected_current_health, actual_current_health)

    def test_ship_change_alignment_us_to_them(self):
        # arrange
        ship = Ship("test", 0, 0, Alignment.US, 10, 10, 10)
        expected_alignment = Alignment.THEM

        # act
        ship.change_alignment()
        actual_alignment = ship.get_alignment()

        # assert
        self.assertEqual(expected_alignment, actual_alignment)

    def test_ship_change_alignment_them_to_us(self):
        # arrange
        ship = Ship("test", 0, 0, Alignment.THEM, 10, 10, 10)
        expected_alignment = Alignment.US

        # act
        ship.change_alignment()
        actual_alignment = ship.get_alignment()

        # assert
        self.assertEqual(expected_alignment, actual_alignment)

    def test_battleship_attack(self):
        # arrange
        ship = Battleship("", 0, 0, Alignment.US)
        target = Ship("", 0, 0, Alignment.THEM, 50, 10, 10)
        expected_current_health = 30
        expected_torpedoes = 9

        # act
        ship.attack(target)
        actual_current_health = target.get_current_health()
        actual_torpedoes = ship.get_torpedoes()

        # assert
        self.assertEqual(expected_current_health, actual_current_health)
        self.assertEqual(expected_torpedoes, actual_torpedoes)

    def test_battleship_attack_out_of_torpedoes(self):
        # arrange
        ship = Battleship("", 0, 0, Alignment.US)
        target = Ship("", 0, 0, Alignment.THEM, 300, 10, 10)
        expected_current_health = 90
        expected_torpedoes = 0

        # act
        for attack in range(11):
            ship.attack(target)
        actual_current_health = target.get_current_health()
        actual_torpedoes = ship.get_torpedoes()

        # assert
        self.assertEqual(expected_current_health, actual_current_health)
        self.assertEqual(expected_torpedoes, actual_torpedoes)

    def test_battleship_status(self):
        # arrange
        ship = Battleship("test", 0, 0, Alignment.US)
        expected_status = """test
type: Battleship
health: 100
location: 0, 0
torpedoes: 10"""

        # act
        actual_status = ship.status()

        # assert
        self.assertEqual(expected_status, actual_status)


    def test_corvette_attack(self):
        # arrange
        ship = Corvette("", 0, 0, Alignment.US)
        target = Ship("", 0, 0, Alignment.THEM, 50, 10, 10)
        expected_alignment = Alignment.US

        # act
        ship.attack(target)
        actual_alignment = target.get_alignment()

        # assert
        self.assertEqual(expected_alignment, actual_alignment)

    def test_repair(self):
        # arrange
        ship = Repair("", 0, 0, Alignment.US)
        target = Ship("", 0, 0, Alignment.US, 50, 10, 10)
        expected_current_health = 50
        target.assess_damage(10)

        # act
        ship.attack(target)
        actual_current_health = target.get_current_health()

        # assert
        self.assertEqual(expected_current_health, actual_current_health)
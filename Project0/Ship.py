import math
from enum import Enum


class Alignment(Enum):
    US = 1,
    THEM = 2
    CHAOTIC = 3


class Ship:

    def __init__(self, name, x, y, alignment, max_health, attack_range, attack_power, x_move=0, y_move=0):
        self._name = name
        self._x_position = x
        self._y_position = y
        self._alignment = alignment
        self._max_health = max_health
        self._current_health = max_health
        self._attack_range = attack_range
        self._attack_power = attack_power
        self._x_move = x_move
        self._y_move = y_move

    def _should_shoot_at(self, target):
        return self._alignment == Alignment.CHAOTIC or self._alignment != target.get_alignment()

    def _is_within_range(self, target):
        return self._attack_range >= math.sqrt(
            (self._x_position - target.get_x()) ** 2 +
            (self._y_position - target.get_y()) ** 2)

    def attack(self, target):
        if self._should_shoot_at(target) and self._is_within_range(target):
            target.assess_damage(self._attack_power)

    def status(self):
        return "{}\ntype: {}\nhealth: {}\nlocation: {}, {}".format(
            self._name, self.get_type(), self.get_current_health(), self.get_x(), self.get_y() )

    def move(self):
        self.assess_damage(-1) # easier for us than to repeat the logic
        self._x_position += self._x_move
        self._y_position += self._y_move

    def get_attack_power(self):
        return self._attack_power

    def get_attack_range(self):
        return self._attack_range

    def get_name(self):
        return self._name

    def get_type(self):
        return "Ship"

    def assess_damage(self, damage):
        self._current_health -= damage
        if self._current_health < 0:
            self._current_health = 0
        elif self._current_health > self._max_health:
            self._current_health = self._max_health

    def change_alignment(self):
        if self._alignment == Alignment.US:
            self._alignment = Alignment.THEM
        elif self._alignment == Alignment.THEM:
            self._alignment = Alignment.US

    def get_x(self):
        return self._x_position

    def get_y(self):
        return self._y_position

    def get_alignment(self):
        return self._alignment

    def get_current_health(self):
        return self._current_health

    def get_max_health(self):
        return self._max_health


class Battleship(Ship):

    def __init__(self, name, x, y, alignment):
        super().__init__(name, x, y, alignment, 100, 10, 10, -1, -1)
        self._torpedoes = 10

    def attack(self, target):
        if self._should_shoot_at(target) and self._is_within_range(target):
            target.assess_damage(self._attack_power)
            if self._torpedoes > 0:
                target.assess_damage(10)
                self._torpedoes -= 1

    def get_torpedoes(self):
        return self._torpedoes

    def get_type(self):
        return "Battleship"

    def status(self):
        return "{}\ntorpedoes: {}".format(super().status(), self._torpedoes)


class Cruiser(Ship):

    def __init__(self, name, x, y, alignment):
        super().__init__(name, x, y, alignment,
                         max_health=50, attack_range=50, attack_power=5,
                         x_move=1, y_move=2)


class Corvette(Ship):
    def __init__(self, name, x, y, alignment):
        super().__init__(name, x, y, alignment,
                         max_health=20, attack_range=25, attack_power=0,
                         x_move=5, y_move=5)

    def attack(self, target):
        if self._should_shoot_at(target) and self._is_within_range(target):
            target.change_alignment()


class Repair(Cruiser):
    def __init__(self, name, x, y, alignment):
        super().__init__(name, x, y, alignment)
        self._attack_range = 25
        self._max_health = 20
        self._current_health = 20

    def attack(self, target):
        if self._is_within_range(target) and self._alignment == target.get_alignment():
            target.assess_damage(-target.get_max_health())

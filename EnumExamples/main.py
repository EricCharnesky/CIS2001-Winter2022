from enum import Enum
import random


class Light(Enum):

    RED = 1
    YELLOW = 2
    GREEN = 3


print("let's play red light green light")

random_value = random.randint(1, 3)


if random_value == 1 :
    current_light = Light.RED
elif random_value == 2:
    current_light = Light.YELLOW
elif random_value == 3:
    current_light = Light.GREEN

if current_light == Light.GREEN:
    print("GO!")

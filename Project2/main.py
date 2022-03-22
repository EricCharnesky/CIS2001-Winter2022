import random


class Car:

    MAX_TIME_WAITING = 10

    def __init__(self):
        pass

    def get_fry_order(self):
        return 0

    def get_burger_order(self):
        return 0

    def is_order_complete(self, time):
        return True


class Food:

    def __init__(self, name, time_expiring, profit):
        self.name = name
        self.time_expiring = time_expiring
        self.profit = profit


class FourFriendsBurgersAndFryShop:

    MAX_BURGERS_ON_GRILL = 6
    MINUTES_NEEDED_TO_COOK_BURGER = 3

    def __init__(self):
        self.burger_queue = []
        self.fry_stack = []
        self.grill = []
        self.frier = []
        self.profit = 0

    def get_number_of_burgers_in_queue(self):
        return len(self.burger_queue)

    def check_grill_for_done_burgers(self, time):
        for item in self.grill[:]: # can't remove items as you loop through a list
            if item == time:
                self.burger_queue.append(Food("burger", time+10, 1))
                self.grill.remove(item)

    def add_burger_to_grill(self, time):
        if len(self.grill) < self.MAX_BURGERS_ON_GRILL:
            self.grill.append(time+self.MINUTES_NEEDED_TO_COOK_BURGER)

    def serve_burger(self, time):

        while len(self.burger_queue) != 0 and self.grill[0].time_expiring < time:

            # track profit loss
            self.profit -= self.grill.pop(0).profit

        if len(self.burger_queue) == 0:
            return False

        self.profit += self.grill.pop(0)
        return True


drive_thru = []

for minute in range(120):
    if random.randint(1, 3) == 1:
        drive_thru.append(Car())


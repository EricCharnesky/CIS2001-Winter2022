import random

from StackAndQueue import Stack, Queue


class Car:
    MAX_TIME_WAITING = 10

    def __init__(self, time_arrived_in_queue):
        self._time_arrived_in_queue = time_arrived_in_queue
        self._number_of_burgers_ordered = random.randint(0, 8)
        self._number_of_fries_ordered = random.randint(1, 8)
        self._number_of_burgers_received = 0
        self._number_of_fries_received = 0
        self._time_order_is_complete = 0
        self._time_order_was_placed = -1

    def place_order(self, time):
        self._time_order_was_placed = time

    def has_placed_order(self):
        return self._time_order_was_placed != -1

    def get_time_arrived_in_queue(self):
        return self._time_arrived_in_queue

    def serve_fry(self, fry_count=1):
        self._number_of_fries_received += fry_count

    def serve_burger(self, burger_count=1):
        self._number_of_burgers_received += burger_count

    def get_fries_needed_for_order(self):
        return self._number_of_fries_ordered - self._number_of_fries_received

    def get_burgers_needed_for_order(self):
        return self._number_of_burgers_ordered - self._number_of_burgers_received

    def is_order_complete(self, time):
        if self._number_of_burgers_ordered == self._number_of_burgers_received and \
                self._number_of_fries_ordered == self._number_of_fries_received:
            self._time_order_is_complete = time
            return True
        return False

    def get_total_wait_time(self):
        return self._time_order_is_complete - self._time_arrived_in_queue


class Food:

    BURGER_PROFIT = 1
    FRY_PROFIT = .5

    def __init__(self, name, time_expiring, profit):
        self.name = name
        self.time_expiring = time_expiring
        self.profit = profit


class FourFriendsBurgersAndFryShop:
    MAX_BURGERS_ON_GRILL = 6
    MINUTES_NEEDED_TO_COOK_BURGER = 3
    MAX_FRIES_IN_FRIER = 4
    MINUTES_NEED_TO_FRY_FRIES = 2

    NUMBER_OF_MINUTES_UNTIL_BURGERS_EXPIRE = 10
    NUMBER_OF_MINUTES_UNTIL_FRIES_EXPIRE = 20

    GOAL_BURGERS_READY = 6
    GOAL_FRIES_READY = 4

    def __init__(self):
        self.burger_queue = Queue()
        self.fry_stack = Stack()
        self.grill = []
        self.frier = []
        self.profit = 0

    def get_number_of_burgers_in_queue(self):
        return len(self.burger_queue)

    def get_number_of_fries_in_fry_stack(self):
        return len(self.fry_stack)

    def check_frier_for_done_fries(self, time):
        for item in self.frier[:]:  # can't remove items as you loop through a list
            if item == time:
                self.fry_stack.push(Food("fry", time + self.NUMBER_OF_MINUTES_UNTIL_FRIES_EXPIRE, Food.FRY_PROFIT))
                self.frier.remove(item)

    def check_grill_for_done_burgers(self, time):
        for item in self.grill[:]:  # can't remove items as you loop through a list
            if item == time:
                self.burger_queue.enqueue(Food("burger", time + self.NUMBER_OF_MINUTES_UNTIL_BURGERS_EXPIRE, Food.BURGER_PROFIT))
                self.grill.remove(item)

    def get_number_of_fries_in_frier(self):
        return len(self.frier)

    def get_number_of_burgers_cooking(self):
        return len(self.grill)

    def add_fry_to_frier(self, time):
        if len(self.frier) < self.MAX_FRIES_IN_FRIER:
            #print('started cooking fry at', minute)
            self.frier.append(time + self.MINUTES_NEED_TO_FRY_FRIES)

    def add_burger_to_grill(self, time):
        if len(self.grill) < self.MAX_BURGERS_ON_GRILL:
            #print('started cooking burger at', minute)
            self.grill.append(time + self.MINUTES_NEEDED_TO_COOK_BURGER)

    def serve_burger(self, time):

        while len(self.burger_queue) != 0 and self.burger_queue.front().time_expiring < time:
            # track profit loss
            self.profit -= self.burger_queue.dequeue().profit

        if len(self.burger_queue) == 0:
            return False

        self.profit += self.burger_queue.dequeue().profit
        return True

    def serve_fry(self, time):

        while len(self.fry_stack) != 0 and self.fry_stack.peek().time_expiring < time:
            # track profit loss
            self.profit -= self.fry_stack.pop().profit

        if len(self.fry_stack) == 0:
            return False

        self.profit += self.fry_stack.pop().profit
        return True

    def check_for_minimum_ready(self, minute):
        for fry in range(self.GOAL_FRIES_READY - self.get_number_of_fries_in_frier() - self.get_number_of_fries_in_fry_stack()):
            self.add_fry_to_frier(minute)

        for burger in range(self.GOAL_BURGERS_READY - self.get_number_of_burgers_cooking() - self.get_number_of_burgers_in_queue()):
            self.add_burger_to_grill(minute)


shop = FourFriendsBurgersAndFryShop()
drive_thru = Queue()

for minute in range(120):
    # randomly adding car
    if random.randint(1, 3) == 1:
        print('car arrived at', minute)
        drive_thru.enqueue(Car(minute))

    # checking for items that are done cooking
    shop.check_frier_for_done_fries(minute)
    shop.check_grill_for_done_burgers(minute)

    # serving front car
    if len(drive_thru) != 0:
        car = drive_thru.front()

        if not car.has_placed_order():
            if car.get_time_arrived_in_queue() + car.MAX_TIME_WAITING < minute:
                print('car drives off')
                drive_thru.dequeue()
            else:
                car.place_order(minute)
                #print('car places order')

        if car.has_placed_order():
            # serve ready food
            fries_ordered = car.get_fries_needed_for_order()
            burgers_ordered = car.get_burgers_needed_for_order()

            for fry in range(fries_ordered):
                if shop.serve_fry(minute):
                    car.serve_fry()

            for burger in range(burgers_ordered):
                if shop.serve_burger(minute):
                    car.serve_burger()

            if car.is_order_complete(minute):
                drive_thru.dequeue()
                print('car is served and drives off at', minute)

            # get remaining order to cook
            fries_ordered = car.get_fries_needed_for_order()
            burgers_ordered = car.get_burgers_needed_for_order()

            # cook more for order, unless it is already cooking
            for fry in range(fries_ordered-shop.get_number_of_fries_in_frier()):
                shop.add_fry_to_frier(minute)

            for burger in range(burgers_ordered-shop.get_number_of_burgers_cooking()):
                shop.add_burger_to_grill(minute)

    shop.check_for_minimum_ready(minute)

print('Profit: $', shop.profit)



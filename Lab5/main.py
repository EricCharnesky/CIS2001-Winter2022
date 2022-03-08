
#https://github.com/EricCharnesky/CIS2001-Winter2022/blob/main/Week5-StacksAndQueues/main.py#L4-L28
class Stack:

    # O(1)
    def __init__(self):
        self._data = []

    # O(1)
    def push(self, item):
        self._data.append(item)

    # O(1)
    def pop(self):
        return self._data.pop()

    # O(1)
    def peek(self):
        return self._data[len(self._data)-1]

    # O(1)
    def is_empty(self):
        return len(self._data) == 0

    # O(1)
    def __len__(self):
        return len(self._data)


# https://github.com/EricCharnesky/CIS2001-Winter2022/blob/main/Week5-StacksAndQueues/main.py#L98-L187
class CircularQueue:


    _MINIMUM_SIZE = 10

    def __init__(self):
        self._data = [None] * CircularQueue._MINIMUM_SIZE
        self._front_index = 0
        self._back_index = 0

    # O(1)
    def enqueue(self, item):

        self._data[self._back_index] = item
        self._back_index += 1
        if self._back_index == len(self._data):
            self._back_index = 0

        if self._back_index == self._front_index:
            self._resize()

    # O(1)
    def dequeue(self):
        if self.is_empty():
            raise IndexError
        item = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index += 1
        if self._front_index == len(self._data):
            self._front_index = 0

            # 10 becomes the minimum size
        if CircularQueue._MINIMUM_SIZE < len(self) * 4 < len(self._data):
            self._resize_smaller()
        return item

    # O(1)
    def front(self):
        if self.is_empty():
            raise IndexError
        return self._data[self._front_index]

    # O(1)
    def is_empty(self):
        return len(self) == 0

    # O(1)
    def __len__(self):
        if self._back_index < self._front_index:
            return len(self._data) - self._front_index + self._back_index
        return self._back_index - self._front_index

    # O(n)
    def _resize(self):
        new_data = [None] * len(self._data) * 2
        new_index = 0
        for index in range(self._front_index, len(self._data)):
            new_data[new_index] = self._data[index]
            new_index += 1
        for index in range(0, self._front_index):
            new_data[new_index] = self._data[index]
            new_index += 1
        self._data = new_data
        self._front_index = 0
        self._back_index = new_index

# O(n)
    def _resize_smaller(self):
        new_data = [None] * ( len(self._data) // 2 )

        for index in range(len(self)):
            new_data[index] = self._data[( self._front_index + index ) % len(self._data)]

        number_of_items = len(self)
        self._data = new_data
        self._front_index = 0
        self._back_index = number_of_items


class TransportMethod:

    def __init__(self, number_of_items_until_full):
        self._number_of_items_until_full = number_of_items_until_full
        self._current_item_count = 0
        self._time_until_fully_loaded = 0

    def load_item(self, time_worked_arrived):
        self._current_item_count += 1

        if self._current_item_count == self._number_of_items_until_full:
            self._time_until_fully_loaded = time_worked_arrived

    def get_time_until_fully_loaded(self):
        return self._time_until_fully_loaded


class Dock:

    MAX_TRAIN_STACK_SIZE = 5
    TRAIN_ONE_WAY_TIME = 1
    PLANE_ONE_WAY_TIME = 5

    def __init__(self, items_per_train, items_per_plane, train_items, plane_items):
        self._trains = [None] # index 0 is none, trains are at 1 - N trains
        for value in items_per_train.split():
            self._trains.append(TransportMethod(int(value)))

        self._planes = [None]
        for value in items_per_plane.split():
            self._planes.append(TransportMethod(int(value)))

        self._train_items = CircularQueue()

        current_stack = Stack()
        for item in train_items.split():
            item = int(item)
            current_stack.push(item)
            if len(current_stack) == self.MAX_TRAIN_STACK_SIZE:
                self._train_items.enqueue(current_stack)
                current_stack = Stack()

        # adding the last possible partial stack if we didn't have a multiple of 5 items
        self._train_items.enqueue(current_stack)

        self._plane_items = CircularQueue()

        for item in plane_items.split():
            item = int(item)
            self._plane_items.enqueue(item)

        self.load_trains()
        self.load_planes()

    def load_trains(self):
        current_time = 0
        while not self._train_items.is_empty():
            current_stack = self._train_items.dequeue()
            while not current_stack.is_empty():
                current_item = current_stack.pop()
                arrival_time = current_time + current_item * self.TRAIN_ONE_WAY_TIME
                self._trains[current_item].load_item(arrival_time)
                current_time += current_item * 2 * self.TRAIN_ONE_WAY_TIME

    def load_planes(self):
        current_time = 0
        while not self._plane_items.is_empty():
            current_item = self._plane_items.dequeue()
            arrival_time = current_time + current_item * self.PLANE_ONE_WAY_TIME
            self._planes[current_item].load_item(arrival_time)
            current_time += current_item * 2 * self.PLANE_ONE_WAY_TIME

    def get_train_fully_loaded_times(self):
        # print
        #for index in range(1, len(self._trains)):
        #    print(self._trains[index].get_time_until_fully_loaded(), end=" ")
        return " ".join(str(train.get_time_until_fully_loaded()) for train in self._trains[1:])

    def get_plane_fully_loaded_times(self):
        return " ".join(str(plane.get_time_until_fully_loaded()) for plane in self._planes[1:])


first_line_to_ignore = input()
items_per_train = input()
items_per_plane = input()
train_items = input()
plane_items = input()

dock = Dock(items_per_train, items_per_plane, train_items, plane_items)
print(dock.get_train_fully_loaded_times())
print(dock.get_plane_fully_loaded_times())

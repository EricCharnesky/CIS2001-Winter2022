import sys


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


# stack = Stack()
#
# for number in range(10):
#     stack.push(number)
#
# while not stack.is_empty():
#     print(stack.pop())

class SlowQueue:

    def __init__(self):
        self._data = []

    # O(1)
    def enqueue(self, item):
        self._data.append(item)

    # O(n) - SAD
    def dequeue(self):
        return self._data.pop(0)

    # O(1)
    def front(self):
        return self._data[0]

    # O(1)
    def is_empty(self):
        return len(self._data) == 0

    # O(1)
    def __len__(self):
        return len(self._data)

class FasterQueueButMoreMemory:

    def __init__(self):
        self._data = []
        self._front_index = 0

    # O(1)
    def enqueue(self, item):
        self._data.append(item)

    # O(1)
    def dequeue(self):
        if self.is_empty():
            raise IndexError
        item = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index += 1
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
        return len(self._data) - self._front_index


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
        # new_index = 0
        # if self._back_index > self._front_index:
        #     for index in range(self._front_index, self._back_index):
        #         new_data[new_index] = self._data[index]
        #         new_index += 1
        # else:
        #     for index in range(self._front_index, len(self._data)):
        #         new_data[new_index] = self._data[index]
        #         new_index += 1
        #     for index in range(0, self._back_index):
        #         new_data[new_index] = self._data[index]
        #         new_index += 1


        for index in range(len(self)):
            new_data[index] = self._data[( self._front_index + index ) % len(self._data)]

        number_of_items = len(self)
        self._data = new_data
        self._front_index = 0
        self._back_index = number_of_items


class Deque:


    _MINIMUM_SIZE = 10

    def __init__(self):
        self._data = [None] * CircularQueue._MINIMUM_SIZE
        self._front_index = 0
        self._back_index = 0

    # O(1)
    def add_back(self, item):

        self._data[self._back_index] = item
        self._back_index += 1
        if self._back_index == len(self._data):
            self._back_index = 0

        if self._back_index == self._front_index:
            self._resize()

    def add_front(self, item):
        self._front_index -= 1

        self._data[self._front_index] = item

        if self._front_index == -1:
            self._front_index = len(self._data) - 1

        if self._back_index == self._front_index:
            self._resize()

    # O(1)
    def remove_front(self):
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
    def remove_back(self):
        if self.is_empty():
            raise IndexError
        self._back_index -= 1
        item = self._data[self._back_index]
        self._data[self._back_index] = None

        if self._back_index == -1:
            self._back_index = len(self._data) - 1

            # 10 becomes the minimum size
        if CircularQueue._MINIMUM_SIZE < len(self) * 4 < len(self._data):
            self._resize_smaller()
        return item

    # O(1)
    def front(self):
        if self.is_empty():
            raise IndexError
        return self._data[self._front_index]

    def back(self):
        if self.is_empty():
            raise IndexError
        return self._data[self._back_index - 1] # python lists rock -1 is the last item

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


queue = Deque()

for number in range(1, 7):
    queue.add_back(number)

for number in range(4):
    print(queue.remove_front())

for number in range(7, 12):
    queue.add_back(number)

while not queue.is_empty():
    print(queue.remove_back())


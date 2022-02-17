class LinkedListStack:

    def __init__(self):
        self._first = None
        self._number_of_items = 0

    # O(1) always - never is resizing like an array based list
    def push(self, data):
        if self._first is None:
            self._first = LinkedListStack.Node(data)
        else:
            self._first = LinkedListStack.Node(data, self._first)
        self._number_of_items += 1

    # O(1)
    def peek(self):
        if self._first is None:
            raise IndexError
        return self._first.data

    # O(1)
    def pop(self):
        if self._first is None:
            raise IndexError
        data = self._first.data
        self._first = self._first.next
        self._number_of_items -= 1
        return data

    def is_empty(self):
        return self._number_of_items == 0

    def __len__(self):
        return self._number_of_items

    class Node:

        def __init__(self, data, next=None):
            self.data = data
            self.next = next


class LinkedListQueue:

    def __init__(self):
        self._front = None
        self._back = None
        self._number_of_items = 0

    # O(1) always - never is resizing like an array based list
    def enqueue(self, data):
        if self._front is None:
            self._front = LinkedListQueue.Node(data)
            self._back = self._front
        else:
            self._back.next = LinkedListQueue.Node(data)
            self._back = self._back.next
        self._number_of_items += 1

    # O(1)
    def front(self):
        if self._front is None:
            raise IndexError
        return self._front.data

    # O(1)
    def dequeue(self):
        if self._front is None:
            raise IndexError
        data = self._front.data
        self._front = self._front.next
        self._number_of_items -= 1
        # if we removed the last item,
        # keep back from pointing at it and preventing it from
        # being garbage collected and freeing the memory
        if self._front is None:
            self._back = None
        return data

    def is_empty(self):
        return self._number_of_items == 0

    def __len__(self):
        return self._number_of_items

    class Node:

        def __init__(self, data, next=None):
            self.data = data
            self.next = next


class LinkedListDeque:

    def __init__(self):
        self._front = None
        self._back = None
        self._number_of_items = 0

    # O(1) always - never is resizing like an array based list
    def add_back(self, data):
        if self._front is None:
            self._front = LinkedListDeque.Node(data)
            self._back = self._front
        else:
            self._back.next = LinkedListDeque.Node(data)
            self._back = self._back.next
        self._number_of_items += 1

    # O(1)
    def add_front(self, data):
        if self._front is None:
            self._front = LinkedListDeque.Node(data)
            self._back = self._front
        else:
            self._front = LinkedListDeque.Node(data, self._front)
        self._number_of_items += 1

    # O(1)
    def front(self):
        if self._front is None:
            raise IndexError
        return self._front.data

    def back(self):
        if self._back is None:
            raise IndexError
        return self._back.data

    # O(1)
    def remove_front(self):
        if self._front is None:
            raise IndexError
        data = self._front.data
        self._front = self._front.next
        self._number_of_items -= 1
        # if we removed the last item,
        # keep back from pointing at it and preventing it from
        # being garbage collected and freeing the memory
        if self._front is None:
            self._back = None
        return data

    # O(n) always
    def remove_back(self):
        if self._back is None:
            raise IndexError
        if self._front == self._back:
            return self.remove_front()
        current_node = self._front
        while current_node.next != self._back:
            current_node = current_node.next
        data = current_node.next.data
        current_node.next = None # clears the link to the old back node for garbage collection
        self._back = current_node
        self._number_of_items -= 1

        return data

    def is_empty(self):
        return self._number_of_items == 0

    def __len__(self):
        return self._number_of_items

    class Node:

        def __init__(self, data, next=None):
            self.data = data
            self.next = next


class DoublyLinkedListDeque:

    def __init__(self):
        self._front = None
        self._back = None
        self._number_of_items = 0

    # O(1) always - never is resizing like an array based list
    def add_back(self, data):
        if self._front is None:
            self._front = DoublyLinkedListDeque.Node(data)
            self._back = self._front
        else:
            self._back.next = DoublyLinkedListDeque.Node(data, previous=self._back)
            self._back = self._back.next
        self._number_of_items += 1

    # O(1)
    def add_front(self, data):
        if self._front is None:
            self._front = DoublyLinkedListDeque.Node(data)
            self._back = self._front
        else:
            self._front = DoublyLinkedListDeque.Node(data, self._front)
        self._number_of_items += 1

    # O(1)
    def front(self):
        if self._front is None:
            raise IndexError
        return self._front.data

    def back(self):
        if self._back is None:
            raise IndexError
        return self._back.data

    # O(1)
    def remove_front(self):
        if self._front is None:
            raise IndexError
        data = self._front.data
        self._front = self._front.next
        self._number_of_items -= 1
        # if we removed the last item,
        # keep back from pointing at it and preventing it from
        # being garbage collected and freeing the memory
        if self._front is None:
            self._back = None
        return data

    # O(1) always
    def remove_back(self):
        if self._back is None:
            raise IndexError
        if self._front == self._back:
            return self.remove_front()
        current_node = self._back.previous
        data = self._back.data
        current_node.next = None # clears the link to the old back node for garbage collection
        self._back = current_node
        self._number_of_items -= 1

        return data

    def is_empty(self):
        return self._number_of_items == 0

    def __len__(self):
        return self._number_of_items

    class Node:

        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous


class CircularDoublyLinkedListDeque:

    def __init__(self):
        self._start = CircularDoublyLinkedListDeque.Node(None)
        self._start.previous = self._start
        self._start.next = self._start
        self._number_of_items = 0

    def _add_node(self, data, next, previous):
        new_node = CircularDoublyLinkedListDeque.Node(data, next, previous)
        new_node.next.previous = new_node
        new_node.previous.next = new_node
        self._number_of_items += 1

    # O(1) always - never is resizing like an array based list
    def add_back(self, data):
        self._add_node(data, self._start, self._start.previous)

    # O(1)
    def add_front(self, data):
        self._add_node(data, self._start.next, self._start)

    # O(1)
    def front(self):
        if self.is_empty():
            raise IndexError
        return self._start.next.data

    def back(self):
        if self.is_empty():
            raise IndexError
        return self._start.previous.data

    def _remove_node(self, node):
        if self.is_empty():
            raise IndexError
        current_node = node
        data = current_node.data
        current_node.next.previous = current_node.previous
        current_node.previous.next = current_node.next
        self._number_of_items -= 1

        return data

    # O(1)
    def remove_front(self):
        return self._remove_node(self._start.next)

    # O(1) always
    def remove_back(self):
        return self._remove_node(self._start.previous)

    def is_empty(self):
        return self._number_of_items == 0

    def __len__(self):
        return self._number_of_items

    class Node:

        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous

class CircularDoublyLinkedList:

    def __init__(self):
        self._start = CircularDoublyLinkedList.Node(None)
        self._start.previous = self._start
        self._start.next = self._start
        self._number_of_items = 0

    def _add_node(self, data, next, previous):
        new_node = CircularDoublyLinkedList.Node(data, next, previous)
        new_node.next.previous = new_node
        new_node.previous.next = new_node
        self._number_of_items += 1

    # O(1) always - never is resizing like an array based list
    def append(self, data):
        self._add_node(data, self._start, self._start.previous)

    # O(n-index) ~ O(n)
    def __getitem__(self, index):
        self.validate_index(index)

        current_index = 0
        current_node = self._start.next

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        return current_node.data

    # O(n-index) ~ O(n)
    def __setitem__(self, index, value):
        self.validate_index(index)

        current_index = 0
        current_node = self._start.next

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        old_data = current_node.data
        current_node.data = value
        return old_data

    # O(n-index) ~ O(n)
    def insert(self, index, data):
        self.validate_index(index)

        current_index = 0
        current_node = self._start.next

        # fun optimization - look at skip lists later
        # see if index is closer to 0 or closer to len(self)
        # if it is closer to 0, start at start.next and go forwards
        # if it is closer to len(self), start at start.previous and go backwards

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        self._add_node(data, current_node, current_node.previous)

    def validate_index(self, index):
        if index < 0 or index >= len(self):
            raise IndexError

    #O(n-index) ~ O(n)
    def pop(self, index=None):
        if index is None:
            return self._remove_node(self._start.previous)

        self.validate_index(index)

        current_index = 0
        current_node = self._start.next

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        return self._remove_node(current_node)

    def _remove_node(self, node):
        if self.is_empty():
            raise IndexError

        node.next.previous = node.previous
        node.previous.next = node.next
        self._number_of_items -= 1

        return node.data

    def is_empty(self):
        return self._number_of_items == 0

    def __len__(self):
        return self._number_of_items

    class Node:

        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous


linked_list = LinkedListStack()
for number in range(10):
    linked_list.push(number)

while not linked_list.is_empty():
    print(linked_list.pop())


linked_list_queue = LinkedListQueue()
for number in range(10):
    linked_list_queue.enqueue(number)

while not linked_list_queue.is_empty():
    print(linked_list_queue.dequeue())


linked_list_deque = CircularDoublyLinkedListDeque()

for number in range(5, -1, -1):
    linked_list_deque.add_front(number)

for number in range(6, 10):
    linked_list_deque.add_back(number)

while not linked_list_deque.is_empty():
    print(linked_list_deque.remove_front())
    print(linked_list_deque.remove_back())


linked_list = CircularDoublyLinkedList()

for number in range(10):
    linked_list.append(number)

for index in range(len(linked_list)):
    linked_list[index] = index * 2 # call __setitem__

for index in range(len(linked_list)):
    print(linked_list[index]) # call __getitem__
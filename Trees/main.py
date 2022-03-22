import random


class Tree:

    class Position:

        def element(self):
            raise NotImplementedError

        def __eq__(self, other):
            raise NotImplementedError

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError

    def parent(self, position):
        raise NotImplementedError

    def number_of_children(self, position):
        raise NotImplementedError

    def children(self, position):
        raise NotImplementedError

    def positions(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def is_root(self, position):
        return self.root() == position

    def is_leaf(self, position):
        return self.number_of_children(position) == 0

    def is_empty(self):
        return len(self) == 0

    #average O(n)
    def depth(self, position):
        if self.is_root(position):
            return 0
        return 1 + self.depth(self.parent(position))

    # works, but....
    # O(n^2)
    def _height_max_depth(self):
        return max( self.depth(position) for position in self.positions() if self.is_leaf(position) )

    # O(n) because each position is only looked at once
    def _height_better(self, position):
        if (self.is_leaf(position)):
            return 0
        return 1 + max( self._height_better(child) for child in self.children(position))

    def height(self, position=None):
        if position is None:
            position = self.root()
        return self._height_better(position)


class BinaryTree(Tree):

    def left(self, position):
        raise NotImplementedError

    def right(self, position):
        raise NotImplementedError

    def sibling(self, position):
        parent = self.parent(position)
        if parent is None:
            return None
        if position == self.left(parent):
            return self.right(parent)
        return self.left(parent)

    def children(self, position):
        if self.left(position) is not None:
            yield self.left(position)
        if self.right(position) is not None:
            yield self.right(position)


class LinkedBinaryTree(BinaryTree):

    class Node:

        def __init__(self, data, parent=None, left=None, right=None):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right

    class Position:

        def __init__(self, container, node):
            self.container = container
            self.node = node

        def data(self):
            return self.node.data

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node

    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError()
        if position.container is not self:
            raise ValueError()
        if position.node.parent is position.node:  # convention for deprecated node
            raise ValueError()
        return position.node # ERROR WAS HERE - missed a return

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, position):
        node = self._validate(position)
        return self._make_position(node.parent)

    def left(self, position):
        node = self._validate(position)
        return self._make_position(node.left)

    def right(self, position):
        node = self._validate(position)
        return self._make_position(node.right)

    def num_children(self, position):
        children = 0
        if self.left(position) is not None:
            children += 1
        if self.right(position) is not None:
            children += 1
        return children

    def add_root(self, data):
        if self._root is not None:
            raise ValueError()
        self._size = 1
        self._root = self.Node(data)
        return self._make_position(self._root)

    def add_left(self, position, data):
        node = self._validate(position)
        if node.left is not None:
            raise ValueError()
        self._size += 1
        node.left = self.Node(data, node)
        return self._make_position(node.left)

    def add_right(self, position, data):
        node = self._validate(position)
        if node.right is not None:
            raise ValueError()
        self._size += 1
        node.right = self.Node(data, node)
        return self._make_position(node.right)

    def replace(self, position, data):
        node = self._validate(position)
        old_data = node.data
        node.data = data
        return old_data

    def delete(self, position):
        node = self._validate(position)
        if self.num_children(position) == 2:
            raise ValueError()
        child = node.left if node.left else node.right
        if child is not None:
            child.parent = node.parent
        if node is self.root:
            self._root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child

        self._size -= 1
        node.parent = node  # convention for deprecated node
        return node.data


class ArrayBasedTree(BinaryTree):

    class Position:

        def __init__(self, container, index):
            self.container = container
            self.index = index

        def data(self):
            return self.container._data[self.index]

        def __eq__(self, other):
            return type(other) is type(self) and other.index is self.index

    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError()
        if position.container is not self:
            raise ValueError()
        if position.index == -1:  # convention for deprecated node
            raise ValueError()
        return position.index # ERROR WAS HERE - missed a return

    def _make_position(self, index):
        return self.Position(self, index) if index != -1 and index < self._size else None

    def __init__(self):
        self._data = []
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(0)

    def parent(self, position):
        index = self._validate(position)
        return self._make_position((index + 1) // 2 - 1)

    def left(self, position):
        index = self._validate(position)
        return self._make_position(index*2 + 1)

    def right(self, position):
        index = self._validate(position)
        return self._make_position(index * 2 + 2)

    def num_children(self, position):
        children = 0
        if self.left(position) != -1:
            children += 1
        if self.right(position) != -1:
            children += 1
        return children

    def add_root(self, data):
        if len(self._data) != 0:
            raise ValueError()
        self._size = 1
        self._data.append(data)
        return self._make_position(0)

    def add_left(self, position, data):
        if self.left(position) is not None:
            raise ValueError()
        self._ensure_capacity()
        self._size += 1
        left_index = self._validate(self.left(position))
        self._data[left_index] = data
        return self._make_position(left_index)

    def add_right(self, position, data):
        if self.right(position) is not None:
            raise ValueError()
        self._ensure_capacity()
        self._size += 1
        right_index = self._validate(self.right(position))
        self._data[right_index] = data
        return self._make_position(right_index)

    def replace(self, position, data):
        index = self._validate(position)
        old_data = self._data[index]
        self._data[index] = data
        return old_data

    def _ensure_capacity(self):
        if len(self._data) < self._size * 2 + 1:
            new_data = [None] * (self._size * 2 + 1)
            for index in range(len(self._data)):
                new_data[index] = (self._data[index])
            self._data = new_data


class MinPriorityQueue:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    # O(log(n))
    def enqueue(self, data):
        self._data.append(data)
        self._upheap(len(self._data) - 1)

    # O(1)
    def front(self):
        return self._data[0]

    # O(log(n))
    def dequeue(self):
        data = self._data[0]
        value = self._data.pop()
        if len(self._data) > 0:
            self._data[0] = value
            self._downheap(0)
        return data

    def _downheap(self, index):

        if index < len(self._data):
            right_index = self._right(index)
            left_index = self._left(index)
            smallest_child_index = None

            if left_index < len(self._data):
                smallest_child_index = left_index

            if right_index < len(self._data):
                if self._data[right_index] < self._data[smallest_child_index]:
                    smallest_child_index = right_index

            if smallest_child_index is not None and self._data[index] > self._data[smallest_child_index]:
                temp = self._data[index]
                self._data[index] = self._data[smallest_child_index]
                self._data[smallest_child_index] = temp
                self._downheap(smallest_child_index)

    def _upheap(self, index):
        if index != 0:
            parent_index = self._parent(index)
            if self._data[index] < self._data[parent_index]:
                temp = self._data[index]
                self._data[index] = self._data[parent_index]
                self._data[parent_index] = temp
                self._upheap(parent_index)



    def _parent(self, index):
        return ( index + 1 ) // 2 - 1

    def _left(self, index):
        return index * 2 + 1

    def _right(self, index):
        return index * 2 + 2



priority_queue = MinPriorityQueue()
for number in range(10):
    priority_queue.enqueue(random.randint(1, 100))

while not priority_queue.is_empty():
    print(priority_queue.dequeue())

#
# tree = ArrayBasedTree()
# your_name = input("What's your name?")
# root = tree.add_root(your_name)
# father = input("What's your father's name?")
# father_position = tree.add_left(root, father)
# mother = input("What's your mother's name?")
# mother_position = tree.add_right(root, mother)
#
# father = input("What's your father's father's name?")
# tree.add_left(father_position, father)
# mother = input("What's your father's mother's name?")
# tree.add_right(father_position, mother)
#
# father = input("What's your mother's father's name?")
# tree.add_left(mother_position, father)
# mother = input("What's your mother's mother's name?")
# tree.add_right(mother_position, mother)


def pre_order_traversal(tree, position=None):
    if position is None:
        position = tree.root()
    print(position.data())
    for child in tree.children(position):
        pre_order_traversal(tree, child)


def in_order_traversal(tree, position=None):
    if position is None:
        position = tree.root()
    if tree.left(position) is not None:
        in_order_traversal(tree, tree.left(position))
    print(position.data())
    if tree.right(position) is not None:
        in_order_traversal(tree, tree.right(position))


# depth first
def post_order_traversal(tree, position=None):
    if position is None:
        position = tree.root()

    for child in tree.children(position):
        post_order_traversal(tree, child)
    print(position.data())


def breadth_first(tree, position=None, queue=None):
    if queue is None:
        queue = []
    if position is None:
        position = tree.root()
    print(position.data())
    for child in tree.children(position):
        queue.append(child)
    if len(queue) != 0:
        breadth_first(tree, queue.pop(0), queue)


print('pre-order - self, left, right')
pre_order_traversal(tree)

print('in-order - left, self, right')
in_order_traversal(tree)

print('post-order - left, right, self')
post_order_traversal(tree)

print('breadth-first - each level at a time')
breadth_first(tree)
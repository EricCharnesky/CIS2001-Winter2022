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

tree = LinkedBinaryTree()
your_name = input("What's your name?")
root = tree.add_root(your_name)
father = input("What's your father's name?")
father_position = tree.add_left(root, father)
mother = input("What's your mother's name?")
mother_position = tree.add_right(root, mother)

father = input("What's your father's father's name?")
tree.add_left(father_position, father)
mother = input("What's your father's mother's name?")
tree.add_right(father_position, mother)

father = input("What's your mother's father's name?")
tree.add_left(mother_position, father)
mother = input("What's your mother's mother's name?")
tree.add_right(mother_position, mother)


def pre_order_traversal(tree, position):
    print(position.data())
    for child in tree.children(position):
        pre_order_traversal(tree, child)



pre_order_traversal(tree, tree.root())
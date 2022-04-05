
# https://github.com/EricCharnesky/CIS2001-Winter2022/blob/main/Trees/main.py
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


class BinarySearchTree(BinaryTree):

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

    # average ( if we can be somewhat balanced ) O( log(n) )
    def add(self, data):
        if self._root is None:
            self._root = self.Node(data)
            self._size += 1
        else:
            self._add(data, self.root())

    def _add(self, data, position):
        node = self._validate(position)

        # less than to the left
        if data < node.data:
            if node.left is None:
                node.left = self.Node(data, node)
                self._size += 1
            else:
                self._add(data, self._make_position(node.left))
        elif data > node.data:
            if node.right is None:
                node.right = self.Node(data, node)
                self._size += 1
            else:
                self._add(data, self._make_position(node.right))
        else:
            raise ValueError("data already in tree")

    # worst case - chain - O(n)
    # best case - O(1)
    # average ( if we can be somewhat balanced ) O( log(n) )
    def contains(self, data):
        if self._root is None:
            raise ValueError("empty")
        return self._contains(data, self.root())

    # average ( if we can be somewhat balanced ) O( log(n) )
    def remove(self, data):
        position = self._get_position(data, self.root())
        if position is None:
            raise ValueError("data not in tree")

        self._size -= 1

        if self.num_children(position) == 0:
            node = self._validate(position)
            if node == node.parent.left:
                node.parent.left = None
            elif node == node.parent.right:
                node.parent.right = None
            node.parent = node # invalidate

        elif self.num_children(position) == 1:
            node = self._validate(position)

            child = node.left
            if child is None:
                child = node.right

            if node == node.parent.left:
                node.parent.left = child
            elif node == node.parent.right:
                node.parent.right = child

            node.parent = node  # invalidate

        # two children
        else:
            next_descendant = self.right(position)
            while self.left(next_descendant) is not None:
                next_descendant = self.left(next_descendant)

            node_to_remove = self._validate(position)

            next_descendant_node = self._validate(next_descendant)

            node_to_remove.data = next_descendant_node.data

            if next_descendant_node.parent.right == next_descendant_node:
                next_descendant_node.parent.right = next_descendant_node.right

            else:
                next_descendant_node.parent.left = next_descendant_node.right

            if next_descendant_node.right is not None:
                next_descendant_node.right.parent = next_descendant_node.parent

    def _get_position(self, data, current_position):
        node = self._validate(current_position)
        if node is None:
            return None
        if data == node.data:
            return current_position
        if data < node.data:
            return self._get_position(data, self.left(current_position))
        return self._get_position(data, self.right(current_position))

    def _contains(self, data, position):
        node = self._validate(position)
        if node is None:
            return False
        if data == node.data:
            return True
        if data < node.data:
            return self._contains(data, self._make_position(node.left))
        # if data > node.data
        return self._contains(data, self._make_position(node.right))

    def _in_order_traversal(self, position):
        if self.left(position) is not None:
            for value in self._in_order_traversal(self.left(position)):
                yield value
        yield position.data()
        if self.right(position) is not None:
            for value in self._in_order_traversal(self.right(position)):
                yield value

    def __iter__(self):
        for value in self._in_order_traversal(self.root()):
            yield value

tree = BinarySearchTree()
tree.add(7)
tree.add(4)
tree.add(11)
tree.add(2)
tree.add(10)
tree.add(9)
tree.add(12)

for value in tree:
    print(value)

tree.remove(11)
tree.remove(7)

for value in tree:
    print(value)

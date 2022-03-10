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



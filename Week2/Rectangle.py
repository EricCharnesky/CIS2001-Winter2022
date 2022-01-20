from Polygon import Polygon


class Rectangle(Polygon):

    def __init__(self, length = 0, width = 0):
        super().__init__(4) # we always know the number of sides
        self.set_length(length)
        self.set_width(width)

    def set_side_length(self, side_index, length):
        if side_index > 3:
            return False
        # if side_index % 2 == 1:
        if side_index % 2: # for ints, anything other than 0 is true
            super().set_side_length(1, length)
            super().set_side_length(3, length)
        else:
            super().set_side_length(0, length)
            super().set_side_length(2, length)

    def set_length(self, length): # helpful methods to make it easier
        # might not be mathmatically correct
        self.set_side_length(0, length)

    def set_width(self, width): # helpful methods to make it easier
        self.set_side_length(1, width)

    def get_area(self):
        # doesn't matter self or super version, they are the same
        return self.get_side_length(0) * super().get_side_length(1)


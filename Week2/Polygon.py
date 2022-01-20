class Polygon:

    def __init__(self, number_of_sides):
        self._number_of_sides = number_of_sides # maybe do some defensive checks?
        self._side_lengths = [0] * number_of_sides
        #self._side_lengths = []
        #for side in range(number_of_sides):
        #     self._side_lengths.append(0)

    def get_number_of_sides(self):
        return self._number_of_sides

    def set_side_length(self, side_index, length):
        self._side_lengths[side_index] = length # defensive checks

    def get_side_length(self, side_index):
        return self._side_lengths[side_index]

    def get_perimeter(self):
        return sum(self._side_lengths)

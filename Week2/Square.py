from Rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, length = 0):
        super().__init__(length, length)

    def set_side_length(self, side_index, length):
        super().set_side_length(0, length)
        super().set_side_length(1, length)

    def set_length(self, length): # a nicer looking helper method
        self.set_side_length(0, length)
from unittest import TestCase
from main import MazeSolver

class TestMazeSolver(TestCase):
    def test_shortest_path(self):
        # arrange
        maze = [
            ['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' '],
            ['W', 'W', ' ', 'W', ' ', ' ', 'W', 'W', 'W', ' '],
            [' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' '],
            [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' '],
            [' ', 'W', ' ', 'W', 'W', 'W', 'W', ' ', 'W', ' '],
            [' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' '],
            [' ', 'W', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' '],
            [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E']
        ]
        expected_shorted_path = r'''['S', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'W', ' ']
['W', 'W', ' ', 'W', ' ', 'x', 'W', 'W', 'W', ' ']
[' ', ' ', ' ', 'W', ' ', 'x', 'W', ' ', ' ', ' ']
[' ', 'W', ' ', 'W', ' ', 'x', 'W', ' ', 'W', ' ']
[' ', 'W', ' ', ' ', ' ', 'x', 'x', 'x', 'W', ' ']
[' ', 'W', ' ', 'W', 'W', 'W', 'W', 'x', 'W', ' ']
[' ', ' ', ' ', 'W', ' ', ' ', 'W', 'x', 'W', ' ']
[' ', 'W', ' ', 'W', ' ', ' ', 'W', 'x', 'W', ' ']
[' ', 'W', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'E']
17 steps
'''

        #act
        solver = MazeSolver(maze)
        actual_shortest_path = solver.shortest_path()

        #assert
        self.assertEqual(expected_shorted_path, actual_shortest_path)
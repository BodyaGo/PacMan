import unittest
import pygame

import sys
sys.path.append('C:/Projects/PacManGroup')


from pacman import draw_board


# Define a mock screen
class MockScreen:
    def __init__(self):
        self.drawn_shapes = []

    def draw_circle(self, color, center, radius):
        self.drawn_shapes.append(('circle', color, center, radius))

    def draw_line(self, color, start_pos, end_pos, width):
        self.drawn_shapes.append(('line', color, start_pos, end_pos, width))

    def draw_arc(self, color, rect, start_angle, stop_angle, width):
        self.drawn_shapes.append(('arc', color, rect, start_angle, stop_angle, width))

# Define a test case
class TestDrawBoard(unittest.TestCase):
    def setUp(self):
        # Set up a mock screen
        self.screen = MockScreen()

    def test_draw_circle(self):
        # Call draw_board with a level containing a circle
        level = [[0, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 0]]
        draw_board(self.screen, level)
        # Assert that one circle is drawn
        self.assertEqual(len(self.screen.drawn_shapes), 1)
        # Assert the properties of the drawn circle
        shape = self.screen.drawn_shapes[0]
        self.assertEqual(shape[0], 'circle')  # Shape type
        self.assertEqual(shape[1], 'white')   # Color
        # Add more assertions as needed for center and radius

    def test_draw_line(self):
        # Call draw_board with a level containing a line
        level = [[0, 0, 0, 0],
                 [0, 3, 0, 0],
                 [0, 0, 0, 0]]
        draw_board(self.screen, level)
        # Assert that one line is drawn
        self.assertEqual(len(self.screen.drawn_shapes), 1)
        # Assert the properties of the drawn line
        shape = self.screen.drawn_shapes[0]
        self.assertEqual(shape[0], 'line')  # Shape type
        self.assertEqual(shape[1], 'color') # Color
        # Add more assertions as needed for start_pos, end_pos, and width

    # Add more test cases for other shapes (arc, etc.) and edge cases


pygame.init()

# Run the tests
if __name__ == '__main__':
    unittest.main()

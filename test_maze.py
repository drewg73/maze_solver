import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        m1 = Maze(0, 0, 10, 12, 10, 10)
        self.assertEqual(len(m1._cells), 12)
        self.assertEqual(len(m1._cells[0]), 10)

    def test_maze_min_values(self):
        m1 = Maze(0, 0, 1, 1, 10, 10)
        self.assertEqual(len(m1._cells), 1)
        self.assertEqual(len(m1._cells[0]), 1)
    
    def test_maze_zero_dimensions(self):
        with self.assertRaises(ValueError):
            m1 = Maze(0, 0, 0, 2, 10, 10) 
    
    def test_maze_negative_dimensions(self):
        with self.assertRaises(ValueError):
            m1 = Maze(0, 0, -5, 10, 10, 10)
    
    def test_maze_non_interger_values(self):
        with self.assertRaises(TypeError):
            Maze(0, 0, 5.5, 10, 10, 10)

    def test_entrance_and_exit(self):
        m1 = Maze(0, 0, 10, 12, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(
            m1._cells[m1._num_cols - 1][m1._num_rows - 1].has_bottom_wall, False
        )
    
    def test_visited_reset(self):
        m1 = Maze(0, 0, 10, 12, 10, 10)
        for row in m1._cells:
            for cell in row:
                self.assertEqual(cell.visited, False)
    
if __name__ == "__main__":
    unittest.main()

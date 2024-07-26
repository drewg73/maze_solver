import time
import random
from cell import Cell

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        if num_rows <= 0:
          raise ValueError("Invalid row value")
        else: 
          self._num_rows = num_rows
        if num_cols <= 0:
          raise ValueError("Invalid row value")
        else:  
          self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is None:
           self._seed = random.seed(0) 
        else:
           self._seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            cols = []
            for j in range(self._num_rows):
                cols.append(Cell(self._win))
            self._cells.append(cols)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, x2, y1, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
      if self._num_cols == 0 or self._num_rows == 0:
        return 
      self._cells[0][0].has_top_wall = False
      self._draw_cell(0, 0)
      self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
      self._draw_cell(self._num_cols -1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
       self._cells[i][j].visited = True
       while True:
        to_visit = []
        if i - 1 > 0:
           if self._cells[i - 1][j].visited is False:
              to_visit.append([i - 1, j])
        if i + 1 < len(self._cells):
           if self._cells[i + 1][j].visited is False:
              to_visit.append([i + 1, j])
        if j - 1 > 0:
           if self._cells[i][j - 1].visited is False:
              to_visit.append([i, j - 1]) 
        if j + 1 < len(self._cells[0]):
           if self._cells[i][j + 1].visited is False:
              to_visit.append([i, j + 1])
        if len(to_visit) == 0:
           self._draw_cell(i, j)
           return 
        next = random.choice(to_visit)
        if i < next[0]:
           self._cells[i][j].has_right_wall = False
           self._cells[next[0]][next[1]].has_left_wall = False
        if i > next[0]:
           self._cells[i][j].has_left_wall = False
           self._cells[next[0]][next[1]].has_right_wall = False
        if j < next[1]:
           self._cells[i][j].has_bottom_wall = False
           self._cells[next[0]][next[1]].has_top_wall = False
        if j > next[1]:
           self._cells[i][j].has_top_wall = False
           self._cells[next[0]][next[1]].has_bottom_wall = False
        self._break_walls_r(next[0], next[1])

    def _reset_cells_visited(self):
       for row in self._cells:
          for cell in row:
             cell.visited = False

    def solve(self):
       if self._solve_r(0, 0):
          print("Maze Solved")
          return True
       else:
          print("Couldn't Solve Maze")
          return False

    def _solve_r(self, i, j):
       self._animate()
       self._cells[i][j].visited = True
       if self._cells[i][j] == self._cells[self._num_cols - 1][self._num_rows -1]:
          return True
       if i - 1 >= 0:
          # look left 
          if not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
             self._cells[i][j].draw_move(self._cells[i - 1][j])
             if self._solve_r(i - 1, j):
                return True
             else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
       if i + 1 < self._num_cols:
          # look right 
          if not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
             self._cells[i][j].draw_move(self._cells[i + 1][j])
             if self._solve_r(i + 1, j):
                return True
             else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
       if j - 1 >= 0:
         # look up 
         if not self._cells[i][j-1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j-1):
               return True
            else:
               self._cells[i][j].draw_move(self._cells[i][j-1], True)
       if j + 1 < self._num_rows:
          # look down 
          if not self._cells[i][j+1].visited and not self._cells[i][j].has_bottom_wall:
             self._cells[i][j].draw_move(self._cells[i][j+1])
             if self._solve_r(i, j+1):
                return True
             else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
       return False

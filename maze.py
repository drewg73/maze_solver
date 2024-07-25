from cell import Maze

class Maze():
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
    self._cells = []
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win

  def _create_cells(self):
    for i in range(1, self.num_rows + 1):
      row = []
      for j in range(1, self._num_cols + 1):
        cell = Cell(self._win)
        row.append(cell)
        self._draw_cell(cell, i, j)
      self._cells.append(row)

  def _draw_cell(self, cell, i, j):
    x1 = i * self._x1
    x2 = x1 + self._cell_size_x
    y1 = j * self._y1
    y2 = y1 + self._cell_size_y
    cell.draw(x1, x2, y1, y2)

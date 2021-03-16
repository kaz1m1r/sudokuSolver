from Grid import Sudokugrid


class Sudokusolver:

    def __init__(self, sudoku: Sudokugrid):
        self.sudoku: Sudokugrid = sudoku

    def insertNumber(self, y: int, x: int, number: int) -> None:
        """
        Insert a number at the specified x- and y coordinate of the sudoku grid
        :param y: y coordinate
        :param x: x coordinate
        :param number: number that's ought to be inserted to the grid
        :return: None
        """
        self.sudoku.grid[y][x] = number

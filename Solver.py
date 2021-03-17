from typing import List

from Grid import Sudokugrid

import numpy as np


class Sudokusolver:

    def __init__(self, sudoku: Sudokugrid):
        """
        AI class that can be used to solve a sudoku
        :param sudoku: Sudokugrid
        """
        self.sudoku: Sudokugrid = sudoku

    def fillSudokuGrid(self):
        """
        Fill the grid
        :return: None
        """

        # if the board is correctly filled then stop the function call
        if self.checkIfSquaresCorrectlyFilled():
            self.sudoku.printGrid()
            return

        else:
            for y in range(0, 9):
                for x in range(0, 9):
                    if self.sudoku.grid[y][x] == 0:
                        for number in range(1, 10):

                            # check if the current number can be placed. If so, insert the number
                            if self.canNumberBePlaced(y, x, number):
                                self.insertNumber(y, x, number)
                                self.fillSudokuGrid()

                            else:
                                continue
                    else:
                        continue

    def canNumberBePlaced(self, y: int, x: int, number: int) -> bool:
        """
        Check if a number can be placed on the specified coordinate
        :param y: y coordinate of the number
        :param x: x coordinate of the number
        :param number: number that's ought to be placed on the specified coordinates
        :return: bool
        """

        # check if number can be placed in row and column
        if number not in self.sudoku.grid[y] and number not in self.sudoku.grid[:, x]:
            return True
        return False

    def checkIfSquaresCorrectlyFilled(self) -> bool:
        """
        Check if all of the squares in the grid are filled correctly. This
        means that every square should contain the numbers 1-9
        :return: bool
        """

        """ EXAMPLE OF A CELL:
        -----------
        | 1  4  5 | <- topRow
        | 9  3  6 | <- middleRow
        | 2  7  8 | <- bottomRow
        -----------
        """

        for a in range(0, 9, 3):
            for b in range(0, 9, 3):

                # making the top-, middle- and bottomRow of one of the 9 squares
                topRow: np.array = [self.sudoku.grid[0 + a, b: 3 + b]]
                middleRow: np.array = [self.sudoku.grid[1 + a, b: 3 + b]]
                bottomRow: np.array = [self.sudoku.grid[2 + a, b: 3 + b]]

                # adding the top-, middle- and bottomRow to one array named 'cell'
                cell: np.array = np.append(topRow, [middleRow, bottomRow])

                # returning False if the cell doesn't contain the numbers 1-9
                for i in range(1, 10):
                    if np.count_nonzero(cell == i) != 1:
                        return False

        # returning True if all the cells in the sudoku grid are filled and
        # contain the numbers 1-9
        return True

    def checkIfColumnCorrectlyFilled(self, x: int) -> bool:
        """
        Check if a column contains the numbers 1-9
        :param x: x coordinate of the column that's checked
        :return: bool
        """

        # saving the column to a variable
        column: np.array = self.sudoku.grid[:, x]

        # iterating over column to check if it contains numbers 1-9
        for number in range(1, 10):
            if column.count(number) != 1:
                return False
        return True

    def checkIfRowCorrectlyFilled(self, y: int) -> bool:
        """
        Check if a row contains the numbers 1-9
        :param y: y coordinate of the row that's checked
        :return: Bool
        """

        # saving the specified row to a variable
        row: np.array = self.sudoku.grid[y]

        # iterating over the row to check if it contains numbers 1-9
        for number in range(1, 10):
            if row.count(number) != 1:
                return False
        return True

    def checkForEmptyColumns(self, x: int) -> bool:
        """
        Only check if a column has cells that are not filled
        :param x: x coordinate of the column
        :return: bool
        """
        if 0 in self.sudoku.grid[:, x]:
            return True
        return False

    def checkForEmptyRows(self, y: int) -> bool:
        """
        Only check if a row has cells that are not filled
        :param y: y coordinate of the row
        :return: bool
        """
        if 0 in self.sudoku.grid[y]:
            return True
        return False

    def insertNumber(self, y: int, x: int, number: int) -> None:
        """
        Insert a number at the specified x- and y coordinate of the sudoku grid
        :param y: y coordinate
        :param x: x coordinate
        :param number: number that's ought to be inserted to the grid
        :return: None
        """
        self.sudoku.grid[y][x] = number

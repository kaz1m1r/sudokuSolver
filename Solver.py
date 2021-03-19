from Grid import Sudokugrid
from termcolor import colored


class Sudokusolver:

    def __init__(self, sudoku: Sudokugrid):
        """
        AI class that can be used to solve a sudoku
        :param sudoku: Sudokugrid
        """
        self.sudoku: Sudokugrid = sudoku

    def solveSudoku(self) -> None:
        """
        Fill the grid
        :return: None
        """

        # checks if the grid is filled
        if self.checkSudokuFilled():
            message = "\n" \
                      "   SOLVED SUDOKU!   \n" \
                      "--------------------\n"
            print(colored(message, 'red'))
            self.sudoku.printGrid()
            return

        # traversing rows
        for y in range(0, 9):

            # traversing columns
            for x in range(0, 9):

                # check if position at the current x-coordinate and y-coordinate is empty
                if self.sudoku.grid[y][x] == 0:

                    # traversing the numbers that could be placed in empty cell
                    for number in range(1, 10):

                        # check if the current number can be placed
                        if self.checkRowCol(y, x, number) and self.checkSquare(y, x, number):

                            self.insertNumber(y, x, number)  # insert the number
                            self.solveSudoku()  # recursive call
                            self.insertNumber(y, x, 0)  # place 0 again at the current position

                        else:
                            continue
                    return

    def checkSudokuFilled(self) -> bool:
        """
        Check if there are empty spaces in the grid
        :return:
        """

        # traverse all cells in sudoku grid
        if 0 in self.sudoku.grid:
            return False
        return True

    def checkRowCol(self, y: int, x: int, number: int) -> bool:
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

    def checkSquare(self, y: int, x: int, number: int) -> bool:
        """
        Check if the square that the number will be placed in already contains the number
        :param y: y coordinate of where you want to place the number
        :param x: x coordinate of where you want to place the number
        :param number: number that you want to place at the coordinate
        :return: bool
        """

        """ 
        EXAMPLE OF A SQUARE:
        -----------
        | 1  4  5 |   <- top row
        | 9  3  6 |   <- middle row
        | 2  7  8 |   <- bottom row
        -----------
        """

        # defining top left x coordinate of square and defining top left y coordinate of square
        y_cord: int = (y // 3) * 3
        x_cord: int = (x // 3) * 3

        # traversing over rows
        for y in range(y_cord, y_cord + 3):

            # traversing over columns
            for x in range(x_cord, x_cord + 3):

                # check if the specified number is at the specified coordinate
                if self.sudoku.grid[y][x] == number:

                    # return False if the number at the specified position equals the number
                    return False

        # return True if the number can be placed in the square
        return True

    def insertNumber(self, y: int, x: int, number: int) -> None:
        """
        Insert a number at the specified x- and y coordinate of the sudoku grid
        :param y: y coordinate
        :param x: x coordinate
        :param number: number that's ought to be inserted to the grid
        :return: None
        """

        # insert the specified number at the given x- and y-coordinate
        self.sudoku.grid[y][x] = number

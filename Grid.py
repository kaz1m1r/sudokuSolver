from typing import Tuple, List

import numpy as np

position = Tuple[int, int, int]


class Sudokugrid:

    def __init__(self):
        self.height: int = 9
        self.grid: np.array = np.zeros(self.height ** 2).reshape(self.height, self.height)
        self.fillGrid()

    def printGrid(self) -> None:
        """
        Print the current grid
        :return: None
        """
        print(self.grid)

    def fillGrid(self) -> None:
        """
        Fill the grid with a random sudoku from 'https://www.sudoku.com/expert/
        :return: None
        """

        def insertNumber(y: int, x: int, number: int) -> None:
            """
            Insert a number at the specified position using it's x and y coordinate
            :param y: y coordinate
            :param x: x coordinate
            :param number: number that's ought to be inserted
            :return:
            """
            self.grid[y][x] = number

        # saving the initial positions of the sudoku in a list
        initial_positions: List[position] = [
            (0, 5, 7),
            (0, 7, 1),
            (1, 2, 4),
            (1, 4, 1),
            (2, 3, 6),
            (2, 6, 2),
            (2, 8, 4),
            (3, 0, 9),
            (3, 5, 7),
            (4, 0, 8),
            (4, 5, 9),
            (4, 7, 2),
            (4, 8, 6),
            (5, 0, 4),
            (5, 6, 8),
            (6, 0, 6),
            (6, 1, 5),
            (6, 5, 2),
            (6, 8, 9),
            (7, 4, 9),
            (7, 5, 8),
            (8, 2, 1),
            (8, 7, 3)
        ]

        # placing the numbers from the initial positions on the grid
        for pos in initial_positions:
            insertNumber(pos[0], pos[1], pos[2])

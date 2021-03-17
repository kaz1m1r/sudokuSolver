from Grid import Sudokugrid
from Solver import Sudokusolver


if __name__ == "__main__":
    grid = Sudokugrid()
    solver = Sudokusolver(grid)
    solver.solveSudoku()


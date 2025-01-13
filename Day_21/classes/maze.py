from itertools import product

from utils.grid import Grid
from utils.loc import Loc 

class Maze(Grid):
    def __init__(self, grid:list[list[str]]) -> None:
        super().__init__(grid)
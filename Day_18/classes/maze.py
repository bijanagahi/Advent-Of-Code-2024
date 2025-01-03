from itertools import product

from utils.grid import Grid
from utils.loc import Loc 

class Maze(Grid):
    def __init__(self, grid:list[list[str]]) -> None:
        super().__init__(grid)
    
    def set_loc(self, loc:Loc, new_value:str) -> None:
        if not self.loc_in_grid(loc):
            raise ValueError(f'Location {loc} is not in grid')
        self.grid[loc.x][loc.y] = new_value

from itertools import product

from utils.grid import Grid
from utils.loc import Loc 

class Maze(Grid):
    def __init__(self, grid:list[list[str]]) -> None:
        super().__init__(grid)
        self.start:Loc = self.find_cell('S')
        self.end:Loc = self.find_cell('E')
        self.walls:list[Loc] = self.get_walls()
    
    def solve_part_1(self) -> int:
        base_time = len(self.find_shortest_path(self.start, self.end, ['#']))-1
        total:int = 0
        mapper:dict[int,int] = {}

        # figure we just start removing walls?
        for wall in self.walls:
            self.set_loc(wall,'.')
            new_time = len(self.find_shortest_path(self.start, self.end, ['#']))-1
            diff:int = base_time - new_time
            # print(f"Removed wall at {wall}, new time is {new_time}, diff is {base_time - new_time}")
            if diff in mapper:
                mapper[diff] +=1
            else:
                mapper[diff] = 1
            if new_time > 0 and base_time - new_time >= 100:
                total+=1
            # don't forget to reset!
            self.set_loc(wall,'#')
        # print(mapper)
        return total

    
    def set_loc(self, loc:Loc, new_value:str) -> None:
        if not self.loc_in_grid(loc):
            raise ValueError(f'Location {loc} is not in grid')
        self.grid[loc.x][loc.y] = new_value

    def find_cell(self, target:str) -> Loc:
        for i,j in product(range(len(self.grid)),range(len(self.grid))):
            if self.grid[i][j] == target:
                return Loc(i,j)
        raise IndexError(f"Could not find symbol ('{target}')")
    
    def get_walls(self) -> list[Loc]:
        walls:list[Loc] = []
        for i,j in product(range(len(self.grid)),range(len(self.grid))):
            if self.grid[i][j] == '#':
                walls.append(Loc(i,j))
        return walls
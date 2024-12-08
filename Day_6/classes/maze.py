from itertools import product
from .helper import Loc, Direction, Player

Grid = list[list[str]]
# Loc = tuple[int, int]

class Maze:
    def __init__(self, grid:Grid) -> None:
        self.grid:Grid = grid
        self.visited:set[tuple[int, int, Direction|None]] = set()
        self.player_starting_loc:Loc = self._getPlayerLoc()
        self.player:Player = Player(self.player_starting_loc, Direction.UP) # player location
    
    '''
    To solve the maze, we loop while walking the player forward,
    checking if they've hit an obstacle or walked off the grid.
    Meanwhile, we keep track of which locations they've visited. 
    '''
    def solve_part_1(self) -> int:
        while (self.loc_in_grid(self.player.loc)):
            # We're on a spot, let's save it
            self.visited.add((self.player.loc.x,self.player.loc.y, None))
            self.grid[self.player.loc.x][self.player.loc.y] = 'X' # DEBUG REMOVE LATER

            # Project a step ahead to see if we'll hit an obstacle
            if self.peek_grid_value(self.player.loc) == '#':
                self.player.turn() # turn 90 degrees if obstacle
            
            # Let's take a step!
            self.player.walk()
        return len(self.visited)
    
    '''
    Solving part 2 is going to be harder, and I can't be fucked.
    So we're just going to do this in N^2 time and check all possible options for loops.
    We detect a loop by seeing if we've entered a location in the same direction as before. Easy!
    '''
    def solve_part_2(self) -> int:
        totals:int = 0
        for i,j in product(range(len(self.grid)),range(len(self.grid))):
            if self.grid[i][j] in ('#','^'): # don't touch the starting location or already existing obstacles
                continue
            # print(f"Setting {(i,j)}:{self.grid[i][j]} to #")
            self.grid[i][j] = '#' # change this spot to be a obstacle.
            totals += 1 if self._solve_single_mutation() else 0
            self.grid[i][j] = '.' # reset the grid back.
        return totals
        
    
    def _solve_single_mutation(self) -> bool:
        self.visited = set() # reset the set
        self.player = Player(self.player_starting_loc, Direction.UP) # reset the player
        loop_counter = 0 # check for infinite loops
        while (self.loc_in_grid(self.player.loc)):

            # We're on a spot, let's see if we've be *exactly* here before.
            if (self.player.loc.x, self.player.loc.y, self.player.dir) in self.visited:
                # We're in a loop!
                return True
            
            # We haven't seen this before so let's save it.
            self.visited.add((self.player.loc.x, self.player.loc.y, self.player.dir))

            # Project a step ahead to see if we'll hit an obstacle
            if self.peek_grid_value(self.player.loc) == '#':
                self.player.turn() # turn 90 degrees if obstacle
            
            # Let's take a step!
            self.player.walk()
            loop_counter +=1
            if(loop_counter > len(self.grid)**2):
                raise Exception(f"Infinite Loop with grid at {self}")

        return False # never hit a loop, walked off the stage.

    '''
    Checks if the given location is still within the grid
    '''
    def loc_in_grid(self, loc:Loc) -> bool:
        max_size:int = len(self.grid)
        if loc.x >= max_size or loc.x < 0:
            return False
        if loc.y >= max_size or loc.y < 0:
            return False
        return True

    '''
    Checks ahead one step to see the 'next' value in the grid
    '''
    def peek_grid_value(self,loc:Loc) -> str:
        projected:Loc = Loc.add(self.player.loc, self.player.dir.value)
        if self.loc_in_grid(projected):
            return self.grid[projected.x][projected.y]
        return '' # return empty string to indicate we've left the grid

    '''
    Returns the value in the grid at this location
    '''
    def get_grid_value(self,loc:Loc) -> str:
        return self.grid[loc.x][loc.y]

    def _getPlayerLoc(self) -> Loc:
        for i,j in product(range(len(self.grid)),range(len(self.grid))):
            if self.grid[i][j] == '^':
                return Loc(i,j)
        raise IndexError("Could not find player symbol ('^')")
    
    def __str__(self) -> str:
        return '\n'+'\n'.join([''.join(_) for _ in self.grid])
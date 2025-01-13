from itertools import product
from .loc import Loc
from .direction import Direction

class Grid:
    def __init__(self, grid:list[list[str]]) -> None:
        self.grid:list[list[str]] = grid # raw values used to init

    def loc_in_grid(self, loc:Loc) -> bool:
        '''
        Checks if the given location is still within the grid
        '''
        max_size:int = len(self.grid)
        if loc.x >= max_size or loc.x < 0:
            return False
        if loc.y >= max_size or loc.y < 0:
            return False
        return True

    def peek_grid_value(self,loc:Loc, dir:Direction) -> str:
        '''
        Checks ahead one step to see the 'next' value in the grid
        '''
        projected:Loc = Loc.add(loc, dir.value)
        if self.loc_in_grid(projected):
            return self.grid[projected.x][projected.y]
        return '' # return empty string to indicate we've left the grid (override wraparounds)

    ###################
    ## UTILITY FUNCS ##
    ###################

    def find_shortest_path(self, start:Loc, end:Loc, walls:list[str]) -> list[Loc]:
        '''
        Returns the shortest path from the starting loc to ending loc as a list of locs
        
        This is just a BFS that stores the path as well.
        '''
        q:list[list[Loc]] = [] # queue of nodes to visit
        seen:set[tuple[int,int]] = set()
        q.append([start]) # add the starting node
        seen.add(start.as_tuple()) # mark starting node as seen
        
        while q:
            path:list[Loc] = q.pop(0)
            cur_loc:Loc = path[-1] # last visited node in path
            
            if cur_loc == end:
                return path
            
            for neighbor in [Loc.add(cur_loc,d.value) for d in Direction]:
                if (self.loc_in_grid(neighbor) and 
                    self.get_grid_value(neighbor) not in walls and
                    neighbor.as_tuple() not in seen):

                    seen.add(neighbor.as_tuple())
                    new_path:list[Loc] = list(path)
                    new_path.append(neighbor)
                    q.append(new_path)
        
        return [] # couldn't find a path between the nodes
    
    def find_cell(self, target:str) -> Loc:
        '''
        Returns the Loc of the *first* cell that matches the target value
        '''
        for x,y in product(range(len(self.grid)),range(len(self.grid[0]))):
            if self.grid[x][y] == target:
                return Loc(x,y)
        raise IndexError(f"Could not find symbol ('{target}')")
            

    def get_grid_value(self,loc:Loc) -> str:
        '''
        Returns the value in the grid at this location
        '''
        return self.grid[loc.x][loc.y]
    
    def __str__(self) -> str:
        return '\n'+'\n'.join([''.join(_) for _ in self.grid])
from itertools import product
from .helper import Loc, Direction, Region, Node

class Grid:
    def __init__(self, grid:list[list[str]]) -> None:
        self.grid:list[list[str]] = grid # raw values used to init the garden
        self.garden:dict[tuple[int, int],Node] = {} 
        self._init_garden() # holds the actual data
        self.seen:set[tuple[int, int]] = set()
        self.regions:list[Region] = []

    '''
    Our Algorithm here is to grab the first node in our list,
    add it to a new region. Then using DFS we iterate through all the neighbor nodes
    '''
    def solve_part_1(self)->int:
        self.process_regions()

        total_cost:int = 0

        # Now we have all the regions, let's calculate their areas and perimeters
        for region in self.regions:
            area:int = len(region.nodes)
            perimeter:int = 0
            for node in region.nodes:
                perimeter += node.open_sides
            print(f"{region}. has area of {area} and perimeter of {perimeter}")
            total_cost += (area*perimeter)
        
        return total_cost
    
    def solve_part_2(self) -> int:
        '''
        This one starts the same as part 1, identify all the regions.
        From there, we'll need to get clever. Let's grab a region, and find a Node
        within it that is on the corner. Then we 'walk' around the region, counting 
        how often we change sides.
        '''
        self.process_regions()

        total_cost:int = 0
        return total_cost
        # for region in self.regions:
            # count corner nodes


        
    
    def process_regions(self)->None:
        q:list[Node] = list(self.garden.values())
        while q:
            node:Node = q.pop()
            if node.loc.as_tuple() in self.seen:
                continue # move on
            self.seen.add(node.loc.as_tuple())

            # We haven't seen this node, so let's build out a new region
            region:Region = Region(node.value)
            region.add(node)
            neighbor_q:list[Node] = node.neighbors.copy()
            while neighbor_q:
                neighbor:Node = neighbor_q.pop()
                if neighbor.loc.as_tuple() in self.seen:
                    continue # we've already seen this node
                self.seen.add(neighbor.loc.as_tuple())

                # Add this node to the region and add it's neighbors to the queue
                region.add(neighbor)
                neighbor_q.extend(neighbor.neighbors)
            
            # Now that this region is complete, add it to the grid's list
            self.regions.append(region)

    
    
    
    
    def _init_garden(self) -> None:
        # First, go through the whole grid, and convert all points to Node objects
        for i,j in product(range(len(self.grid)),range(len(self.grid))):
            loc:Loc = Loc(i,j)
            node:Node = Node(loc,self.grid[i][j])
            self.garden[loc.as_tuple()] = node

        # Now, do it again, but add neighbor nodes
        for i,j in product(range(len(self.grid)),range(len(self.grid))):
            loc:Loc = Loc(i,j)
            node:Node = self.garden[loc.as_tuple()]
            for neighbor_loc in [Loc.add(loc,d.value) for d in Direction]:
                if self.loc_in_grid(neighbor_loc):
                    node.add_neighbor(self.garden[neighbor_loc.as_tuple()])
                    

        

    
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
    # def peek_grid_value(self,loc:Loc) -> str:
    #     projected:Loc = Loc.add(self.player.loc, self.player.dir.value)
    #     if self.loc_in_grid(projected):
    #         return self.grid[projected.x][projected.y]
    #     return '' # return empty string to indicate we've left the grid (override wraparounds)

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
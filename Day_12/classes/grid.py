from itertools import product
from .helper import Loc, Direction, Region, Node, Walker

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
            print(f"\tIt has a corner of {region.get_corner_loc()}")
            total_cost += (area*perimeter)
        
        return total_cost
    
    def solve_part_2(self) -> int:
        '''
        This one starts the same as part 1, identify all the regions.
        From there, we'll need to get clever. Let's grab a region, and find a Node
        within it that is on the corner. Then we 'walk' around the region, counting 
        how often we change sides.

        Start at top left corner. Start a walker there
        '''
        total_cost:int = 0
        self.process_regions()
        for region in self.regions:
            area:int = len(region.nodes)
            sides:int = self.walk_region(region)
            print(f"{region}. has area of {area} and {sides} sides")
            print(f"\tIt has a corner of {region.get_corner_loc()}")
            total_cost += (area*sides)
            
        return total_cost

    def walk_region(self, region:Region) -> int:
        '''
        Walks the perimeter of a region, returning the number of sides

        This is done by initializing a walker at the top-left corner, and following the edge on the right.
        Any time the walker has to turn, we have a new side.
        '''
        print(f"Walking region id: {region.id}")
        sides:int = 0
        corner_loc:Loc = region.get_corner_loc()
        # We start one unit to the left of the corner
        start_loc:Loc = Loc.add(corner_loc,Direction.LEFT.value)
        walker:Walker = Walker(start_loc,Direction.UP)
        
        # We're at the top left corner so let's kick off by moving up and turning
        walker.walk()
        walker.turn_right()
        sides+=1

        while walker.loc != start_loc:
        # for i in range(20):
            # as we walk, we need to check first if we'll walk into the region.
            projected_value:str = self.peek_grid_value(walker.loc,walker.dir)
            
            if projected_value == region.id:
                # this means we're in an inside corner and should turn left
                walker.turn_left()
                # walker.walk()
                sides+=1
                continue # move to the next iteration of the loop.
            
            # we can now move forward safely.
            else:
                walker.walk()
                
                # Check if the wall is still to our right
                wall_dir:Direction = Direction.rotate_right(walker.dir)
                # wall_loc:Loc = Loc.add(walker.loc, wall_dir.value)
                if self.peek_grid_value(walker.loc,wall_dir) == region.id:
                    continue # we're still on a side
                
                # if our region id isn't to the right anymore, we need to rotate to follow it
                walker.turn_right()
                # walker.walk()
                sides+=1
        
        return sides
            



        
    
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
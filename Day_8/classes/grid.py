from itertools import product, combinations
from .helper import Loc, Antenna


class Grid:
    def __init__(self, grid:list[list[str]]) -> None:
        self.grid:list[list[str]] = grid
        self.antinodes:set[tuple[int, int]] = set()
        self.antennas:dict[str,list[Antenna]] = self._init_antennas()

    '''
    Strategy:
        - For all antennas of the same freq:
            - For each pair 'combination':
                - Subtract a from b, add antinode at a+dist, b+(-dist).
                - Make sure antinodes are all in the set.
    '''
    def solve_part_1(self) -> int:
        antenna_list:list[Antenna]
        a:Antenna
        b:Antenna
        for antenna_list in self.antennas.values():
            for a,b in combinations(antenna_list,2):
                dist:Loc = Loc.sub(a.loc, b.loc) # distance between them
                antinode1:Loc = Loc.add(dist,a.loc) # find first antinode
                dist = Loc.mult(dist, -1) # flip direction of distance vector
                antinode2:Loc = Loc.add(dist, b.loc)
                antinode:Loc
                for antinode in (antinode1,antinode2):
                    if self.loc_in_grid(antinode):
                        self.antinodes.add(antinode.as_tuple()) # need the tuple because it's immutable (yay python)
                        self.grid[antinode.x][antinode.y] = '#' # just for visualization purposes. not needed for calculation

        return len(self.antinodes)
    
    '''
    Strategy:
        - Similar to part 1, except instead of 2 antinodes per pair it's ALL of them.
        - This actually simplifies things on our end! For each pair:
            - Get the distance, and choose one of the antennas.
            - Cast a 'ray' outward in multiples of that distance until we leave the grid.
            - Flip the distance vector, do the same.
            - Don't forget to also add the locations of both antennas to the set.
    '''
    def solve_part_2(self) -> int:
        antenna_list:list[Antenna]
        a:Antenna
        b:Antenna
        for antenna_list in self.antennas.values():
            for a,b in combinations(antenna_list,2):
                dist:Loc = Loc.sub(a.loc, b.loc) # distance between them
                # cast a 'ray' from antenna 'a'
                self.cast_ray(a.loc, dist)
                self.cast_ray(a.loc, Loc.mult(dist, -1))

        return len(self.antinodes)

    '''
    Cast a 'ray' from the start, saving each location visited until we leave the grid.
    '''
    def cast_ray(self, start:Loc, dist:Loc) -> None:
        new_loc:Loc = start
        while self.loc_in_grid(new_loc):
            self.antinodes.add(new_loc.as_tuple())
            if self.grid[new_loc.x][new_loc.y] == '.':
                self.grid[new_loc.x][new_loc.y] = '#'
            new_loc = Loc.add(new_loc, dist)
    
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
    Returns the value in the grid at this location
    '''
    def get_grid_value(self,loc:Loc) -> str:
        return self.grid[loc.x][loc.y]

    def _init_antennas(self) -> dict[str,list[Antenna]]:
        antennas:dict[str,list[Antenna]] = {}
        for i,j in product(range(len(self.grid)),range(len(self.grid))):
            if self.grid[i][j] == '.':
               continue
            antenna:Antenna = Antenna(Loc(i,j),self.grid[i][j])
            if antenna.freq in antennas:
                antennas[antenna.freq].append(antenna)
            else:
                antennas[antenna.freq] = [antenna]

        return antennas
    
    def __str__(self) -> str:
        return '\n'+'\n'.join([''.join(_) for _ in self.grid])
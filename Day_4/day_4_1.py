from enum import Enum
from itertools import product

Grid = list[list[str]]
DIRS:list[tuple[int, int]] = [(x,y) for x in range(-1,2) for y in range(-1,2) if ((x,y)!=(0,0))]

class Letter(Enum):
    X = "M"
    M = "A"
    A = "S"
    S = "X"

    def next(self) -> 'Letter':
        return Letter[self.value]

'''
Here's the plan:
    - start at [0,0], scan until we hit an X.
    - Split 8 ways and try to form "XMAS"
'''
def solve(grid:Grid) -> int:
    total:int = 0
    i:int
    j:int
    dir:tuple[int, int]
    for i,j in product(range(len(grid)),range(len(grid))):
        if not Letter[grid[i][j]] == Letter.X:
            continue
        # We have an X. Cast rays in all 8 directions
        for dir in DIRS:
            total += castRay(grid, (i,j), dir)
    return total

'''
Given a ray direction, start looking around 
'''
def castRay(grid:Grid, loc:tuple[int, int], dir:tuple[int, int]) -> int:
    current_letter:Letter = Letter.X
    next_letter:Letter
    i:int = loc[0]
    j:int = loc[1]
    for _ in range(3):
        i += dir[0]
        j += dir[1]
        if i < 0 or i >= len(grid):
            return 0
        if j < 0 or j >= len(grid):
            return 0
        next_letter = Letter[grid[i][j]]
        if next_letter == current_letter.next():
            current_letter = next_letter
        else:
            return 0
    # if we haven't broken out of the loop, we've found XMAS
    return 1

if __name__ == '__main__':
    # build the grid
    grid:Grid =  [list(_.rstrip()) for _ in open("input.txt",'r').readlines()]
    total = solve(grid)
    print(total)
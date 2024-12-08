from enum import Enum
from itertools import product

Grid = list[list[str]]
DIRS:list[tuple[int, int]] = [(-1,-1),(-1,1),(1,1),(1,-1)]
VALID_CORNERS:list[str] = [
"MMSS",
"MSSM",
"SSMM",
"SMMS"]

'''
Here's the plan:
    - start at [0,0], scan until we hit an A.
    - We're looking for an 'X' shape
    - There are only 4 possible combinations of that shape, clockwise from top left:
        - M,M,S,S
        - M,S,S,M
        - S,S,M,M
        - S,M,M,S
    If we create a set that contains those combos we should be good
'''
def solve(grid:Grid) -> int:
    total:int = 0
    i:int
    j:int
    dir:tuple[int, int]
    for i,j in product(range(len(grid)),range(len(grid))):
        if not grid[i][j] == 'A':
            continue
        # We have an A. Check the 4 corners
        total += checkCorners(grid, (i,j))
    return total

def checkCorners(grid:Grid, loc:tuple[int, int]) -> int:
    builder:str = ''
    dir:tuple
    for dir in DIRS:
        i:int = loc[0]+dir[0]
        j:int = loc[1]+dir[1]
        # Bounds checking
        if i < 0 or i >= len(grid):
            return 0
        if j < 0 or j >= len(grid):
            return 0
        
        # Ignore other characters
        if grid[i][j] not in ["M","S"]:
            return 0
        
        builder += grid[i][j]
        
    # We've built the corners, check if they're valid
    return 1 if builder in VALID_CORNERS else 0

if __name__ == '__main__':
    # build the grid
    grid:Grid =  [list(_.rstrip()) for _ in open("input.txt",'r').readlines()]
    total = solve(grid)
    print(total)
from enum import Enum
from itertools import product

from classes.maze import Grid,Maze

def solve(grid:Grid) -> int:
    maze:Maze = Maze(grid)
    total:int = maze.solve_part_1()
    return total



if __name__ == '__main__':
    # build the grid
    grid:Grid =  [list(_.rstrip()) for _ in open("input.txt",'r').readlines()]
    total:int = solve(grid)
    print(total)
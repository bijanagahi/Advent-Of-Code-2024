from classes.grid import Node, Grid
from classes.helper import Loc, Direction

def solve(lines:list[list[str]]) -> int:
    garden:Grid = Grid(lines)
    # print(garden.garden)
    total:int = garden.solve_part_1()
    return total

if __name__ == '__main__':
    grid:list[list[str]] =  [list(_.rstrip()) for _ in open("input.txt",'r').readlines()]
    total:int = solve(grid)
    print(total)
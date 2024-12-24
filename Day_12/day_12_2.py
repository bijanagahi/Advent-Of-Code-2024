from classes.grid import Node, Grid
from classes.helper import Loc, Direction

def solve(lines:list[list[str]]) -> int:
    garden:Grid = Grid(lines)
    total:int = garden.solve_part_2()
    # print(garden.garden)

    return total

if __name__ == '__main__':
    grid:list[list[str]] =  [list(_.rstrip()) for _ in open("test_small.txt",'r').readlines()]
    total:int = solve(grid)
    print(total)
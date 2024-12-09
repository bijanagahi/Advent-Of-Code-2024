from classes.grid import Grid
from classes.helper import Loc, Antenna

def solve(lines:list[list[str]]) -> int:
    grid:Grid = Grid(lines)
    return grid.solve_part_2()


if __name__ == '__main__':
    lines:list[list[str]] =  [list(_.rstrip()) for _ in open("input.txt",'r').readlines()]
    total:int = solve(lines)
    print(total)
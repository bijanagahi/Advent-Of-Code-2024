import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from classes.maze import Maze
from utils.loc import Loc
test:bool = True
width:int
height:int

def solve(lines:list[str]) -> int:
    # Init the maze
    maze:Maze = Maze([list(x) for x in lines])
    total = maze.solve_part_1()
    print(total)
    
    return 0
        


if __name__ == '__main__':
    test = len(sys.argv) < 2
    input_file:str = 'test.txt' if test else 'input.txt'
    lines:list[str] =  [_.rstrip() for _ in open(input_file,'r').readlines()]
    total:int = solve(lines)
    print(total)
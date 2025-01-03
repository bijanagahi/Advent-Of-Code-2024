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
    # Setup, create the empty maze, start adding the walls
    empty_grid:list[list[str]] = [list('.'*width) for i in range(height)]
    maze:Maze = Maze(empty_grid)
    for line in lines[:1024]:
        # print(maze.grid)
        # swap the given coords because in this case the first number is the x axis
        loc:Loc = Loc(int(line.split(',')[1]),int(line.split(',')[0]))
        maze.set_loc(loc,'#')
    start:Loc = Loc(0,0)
    end:Loc = Loc(width-1, height-1)
    path:list[Loc] = maze.find_shortest_path(start,end,['#'])
    for node in path:
        maze.set_loc(node, '0')
    print(maze)
    
    return len(path)-1 # first loc doesn't count as a 'step'
        


if __name__ == '__main__':
    test = len(sys.argv) < 2
    width = 7 if test else 71
    height = 7 if test else 71
    input_file:str = 'test.txt' if test else 'input.txt'
    lines:list[str] =  [_.rstrip() for _ in open(input_file,'r').readlines()]
    total:int = solve(lines)
    print(total)
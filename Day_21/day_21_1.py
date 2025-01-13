import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from classes.maze import Maze
from utils.loc import Loc
from enum import Enum, auto
from itertools import product
from consts import KEYPAD_KEYS,NUMPAD_KEYS

class Direction(Enum):
    U   = '^'
    R   = '>'
    D   = 'v'
    L   = '<'
    A   = 'A'

class Move:
    def __init__(self, start:str, end:str) -> None:
        self.start:str = start
        self.end:str = end
        self.cost:int = 0

def solve(lines:list[str]) -> int:
    # start with 1 keypad, dictionary of tuples of start and end locs, with values being the cost
    # keypad:dict[tuple[str,str],int] = {}

    total_complexity:int = 0
    for line in lines:
        prev_num:str = 'A'
        prev_key:str = 'A'
        prev_2_key:str = 'A'
        prev_3_key:str = 'A'
        full_path:list[Direction] = []
        for numpad_key in line:
            path_to_num:str = NUMPAD_KEYS[(prev_num,numpad_key)][0]
            # print(f'Going from {prev_num}->{numpad_key}. Path is [{path_to_num}]')
            prev_num = numpad_key
            
            # now we need to check the keypad path
            for keypad_key in path_to_num:
                path_to_key:str = KEYPAD_KEYS[(prev_key,keypad_key)][0]
                # print(f'\tGoing from {prev_key}->{keypad_key}. Path is [{path_to_key}]')
                prev_key = keypad_key
                
                # do it again
                for keypad_2_key in path_to_key:
                    path_2_key:str = KEYPAD_KEYS[(prev_2_key,keypad_2_key)][0]
                    # print(f'\t\tGoing from {prev_2_key}->{keypad_2_key}. Path is [{path_2_key}]')
                    prev_2_key = keypad_2_key
                    full_path.extend([Direction[x] for x in path_2_key])
        complexity:int = int(line[:-1]) * len(full_path)
        print(f"{line}:{''.join([x.value for x in full_path])}||{len(full_path)}")
        total_complexity += int(line[:-1]) * len(full_path)

            


    # # for segment in full_path:
    # print(''.join([x.value for x in full_path]))


    
    return total_complexity

def precalculate_costs(num_keypads:int) -> None:
    '''
    Given a number of keypads, precalculate the minimum cost for any numpad press.
    '''
    keypad_costs:dict[tuple[str,str],int] = {}
    keypad_keys:str = 'LDURA'
    numpad_keys:str = '0123456789A'
    for pair in [(x,y) for x,y in product(keypad_keys,keypad_keys)]:
        keypad_costs[pair] = 1 # set initial cost to 1
    
    


if __name__ == '__main__':
    lines:list[str] =  [_.rstrip() for _ in open("test.txt",'r').readlines()]
    # Use "029A" to test
    # total:int = solve(["029A"])
    total:int = solve(lines)
    print(total)
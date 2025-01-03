from enum import Enum
from itertools import product

KEYPAD_KEYS:dict[tuple[str,str],list[str]] = {
('U', 'U'):['A'],
('U', 'L'):['DLA'],
('U', 'D'):['DA'],
('U', 'R'):['DRA'],
('U', 'A'):['RA'],
('L', 'U'):['RUA'],
('L', 'L'):['A'],
('L', 'D'):['RA'],
('L', 'R'):['RRA'],
('L', 'A'):['RRUA'],
('D', 'U'):['UA'],
('D', 'L'):['LA'],
('D', 'D'):['A'],
('D', 'R'):['RA'],
('D', 'A'):['URA'],
('R', 'U'):['LUA'],
('R', 'L'):['LLA'],
('R', 'D'):['LA'],
('R', 'R'):['A'],
('R', 'A'):['UA'],
('A', 'U'):['LA'],
('A', 'L'):['DLLA'],
('A', 'D'):['DLA'],
('A', 'R'):['DA'],
('A', 'A'):['A']}

NUMPAD_KEYS:list[str] = ['A','0','1','2','3','4','5','6','7','8','9']


class Move:
    def __init__(self, start:str, end:str) -> None:
        self.start:str = start
        self.end:str = end
        self.cost:int = 0

def solve(lines:list[str]) -> int:
    # start with 1 keypad, dictionary of tuples of start and end locs, with values being the cost
    keypad:dict[tuple[str,str],int] = {}

    
    return 0

if __name__ == '__main__':
    # lines:list[str] =  [_.rstrip() for _ in open("test.txt",'r').readlines()]
    # Use "029A" to test
    total:int = solve(["029A"])
    print(total)
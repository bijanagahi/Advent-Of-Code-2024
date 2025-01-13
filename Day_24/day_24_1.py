from typing import Callable
from enum import Enum, auto

class GateType(Enum):
    AND = lambda a,b : a & b
    OR  = lambda a,b : a | b
    XOR = lambda a,b : a ^ b

class Gate:
    def __init__(self,id:str, type:GateType) -> None:
        self.id:str = id
        self.type:GateType = type

    def set_input(self, input:bool) -> None:
        pass

def solve(lines:list[str]) -> int:
    AND:Callable[[bool,bool],bool] = lambda a,b : a & b
    print(AND(1,1))
    return 0

if __name__ == '__main__':
    lines:list[str] =  [_.rstrip() for _ in open("test.txt",'r').readlines()]
    total:int = solve(lines)
    print(total)
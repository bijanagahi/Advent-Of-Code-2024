from enum import Enum

class Loc:
    def __init__(self,x:int, y:int) -> None:
        self.x:int = x
        self.y:int = y
    
    '''
    Adds two Locs, useful for shifting a Loc by a direction
    '''
    @staticmethod
    def add(a:'Loc', b:'Loc') -> 'Loc':
        return Loc(a.x + b.x, a.y + b.y)
    
    '''
    Subtracts two Locs, useful for getting a vector pointing from b->a
    '''
    @staticmethod
    def sub(a:'Loc', b:'Loc') -> 'Loc':
        return Loc(a.x - b.x, a.y - b.y)
    
    '''
    Multiplies a Loc by a scalar. useful for flipping the direction if multiplied by -1
    '''
    @staticmethod
    def mult(loc:'Loc', s:int) -> 'Loc':
        return Loc(loc.x*s, loc.y*s)

    
    def as_tuple(self)->tuple[int, int]:
        return (self.x, self.y)
    
    def __str__(self) -> str:
        return f"{(self.x, self.y)}"
    
    def __repr__(self) -> str:
        return self.__str__()
    

class Antenna:
    def __init__(self, loc:Loc, freq:str) -> None:
        self.loc:Loc = loc
        self.freq:str = freq

    def __str__(self) -> str:
        return f"Antenna '{self.freq}' at {self.loc}"
    
    def __repr__(self) -> str:
        return f"Antenna '{self.freq}' at {self.loc}"
from enum import Enum

class Loc:
    def __init__(self,x:int, y:int) -> None:
        self.x:int = x
        self.y:int = y
    
    @staticmethod
    def add(loc_1:'Loc', loc_2:'Loc') -> 'Loc':
        return Loc(loc_1.x+loc_2.x,loc_1.y+loc_2.y)
    
    def as_tuple(self)->tuple[int, int]:
        return (self.x, self.y)
    
    def __str__(self) -> str:
        return f"{(self.x, self.y)}"
    

class Direction(Enum):
    UP = Loc(-1,0)
    RIGHT = Loc(0,1)
    DOWN = Loc(1,0)
    LEFT = Loc(0,-1)

class Player:
    def __init__(self, loc:Loc, dir:Direction) -> None:
        self.loc:Loc = loc
        self.dir:Direction = dir
    
    '''
    Walks the player in the direction they are facing and updates their location
    (Location not guarenteed to be valid)
    '''
    def walk(self) -> None:
        self.loc = Loc.add(self.loc, self.dir.value)

    '''
    Turns the player 90 degrees to the right.
    '''
    def turn(self) -> None:
        match self.dir:
            case Direction.UP:
                self.dir = Direction.RIGHT
            case Direction.RIGHT:
                self.dir = Direction.DOWN
            case Direction.DOWN:
                self.dir = Direction.LEFT
            case Direction.LEFT:
                self.dir = Direction.UP
        

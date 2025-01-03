from .loc import Loc
from .direction import Direction

class Walker:
    def __init__(self, loc:Loc, dir:Direction) -> None:
        self.loc:Loc = loc
        self.dir:Direction = dir
    
    '''
    Walks the walker in the direction they are facing and updates their location
    (Location not guarenteed to be valid)
    '''
    def walk(self) -> None:
        print(f"Walker moving from {self.loc} to {Loc.add(self.loc, self.dir.value)}. Facing {self.dir.name}")
        self.loc = Loc.add(self.loc, self.dir.value)

    def turn_right(self) -> None:
        '''
        Turns the walker 90 degrees to the right.
        '''
        self.dir = Direction.rotate_right(self.dir)

    def turn_left(self) -> None:
        '''
        Turns the walker 90 degrees to the left.
        '''
        self.dir = Direction.rotate_left(self.dir)
        

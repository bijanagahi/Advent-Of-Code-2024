class Loc:
    def __init__(self,x:int, y:int) -> None:
        self.x:int = x
        self.y:int = y
    
    @staticmethod
    def add(loc_1:'Loc', loc_2:'Loc') -> 'Loc':
        return Loc(loc_1.x+loc_2.x,loc_1.y+loc_2.y)
    
    @staticmethod
    def sub(loc_1:'Loc', loc_2:'Loc') -> 'Loc':
        return Loc(loc_1.x-loc_2.x,loc_1.y-loc_2.y)
    
    def as_tuple(self)->tuple[int, int]:
        return (self.x, self.y)
    
    # internal 
    def __str__(self) -> str:
        return f"{(self.x, self.y)}"
    def __repr__(self) -> str:
        return self.__str__()
    def __eq__(self, value: 'Loc') -> bool:
        return self.as_tuple() == value.as_tuple()
    def __lt__(self, other:'Loc') -> bool:
        return self.x <= other.x and self.y <= other.y
    def __gt__(self, other:'Loc') -> bool:
        return self.x > other.x and self.y > other.y
    
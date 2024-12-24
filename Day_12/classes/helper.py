from enum import Enum

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
    

class Direction(Enum):
    UP      = Loc(-1,0)
    RIGHT   = Loc(0,1)
    DOWN    = Loc(1,0)
    LEFT    = Loc(0,-1)

    @classmethod
    def rotate_right(cls, current_dir:'Direction') -> 'Direction':
        match current_dir:
            case Direction.UP:
                return Direction.RIGHT
            case Direction.RIGHT:
                return Direction.DOWN
            case Direction.DOWN:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.UP
        # default
        return current_dir
    
    @classmethod
    def rotate_left(cls, current_dir:'Direction') -> 'Direction':
        match current_dir:
            case Direction.UP:
                return Direction.LEFT
            case Direction.RIGHT:
                return Direction.UP
            case Direction.DOWN:
                return Direction.RIGHT
            case Direction.LEFT:
                return Direction.DOWN
        # default
        return current_dir

    
class Node:
    def __init__(self, loc:Loc, value:str) -> None:
        self.loc:Loc = loc # Location within the grid
        self.value:str = value # Letter value of this node (plant)
        self.neighbors:list['Node'] = [] # List of same-value neighbors
        self.is_internal:bool = False # is this node fully contained within a region
        self.open_sides:int = 4 # How many non same value neighbors exits

    def add_neighbor(self, neighbor:'Node') -> None:
        # Sanity check
        if len(self.neighbors) >= 4:
            raise ValueError(f"Node {self} has too many neighbors!")
        if neighbor in self.neighbors:
            return # skip, we've already seen this one.
        if neighbor.value != self.value:
            return # skip, it's not part of our region
        self.neighbors.append(neighbor)

        # Update the current node based on this new information.
        # Is it now an internal node? Does it have open sides still?
        direction:Loc = Loc.sub(neighbor.loc,self.loc)
        if direction in [d.value for d in Direction]:
            self.open_sides -= 1
            # If we're at no more open sides, this is now an internal node.
            if self.open_sides == 0:
                self.is_internal = True
            
    def __str__(self) -> str:
        return f"Node[{self.value}]@{self.loc} with {len(self.neighbors)} neighbors\n"
    def __repr__(self) -> str:
        return self.__str__()
    def __eq__(self, value: 'Node') -> bool:
        return self.loc == value.loc and self.value == value.value

class Region:
    def __init__(self, id:str) -> None:
        self.id:str = id
        self.nodes:list[Node] = []
        self._node_set:set[tuple[int,int]] = set()
    
    def add(self, node:Node) ->None:
        if node.loc.as_tuple() in self._node_set:
            return
        if node.value != self.id:
            raise ValueError(f"Region {self.id} attemtped to add invalid node: {node}")
        self._node_set.add(node.loc.as_tuple())
        self.nodes.append(node)
    
    def inside(self, node:Node) -> bool:
        return node.loc.as_tuple() in self._node_set
    
    def get_corner_loc(self) -> Loc:
        '''Returns the top-left corner of  this region'''
        corner:Node = self.nodes[0]
        for node in self.nodes:
            if node.loc < corner.loc:
                corner = node
        return corner.loc

    def __str__(self) -> str:
        return f"Region[{self.id}] contains {len(self.nodes)} nodes"


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
        

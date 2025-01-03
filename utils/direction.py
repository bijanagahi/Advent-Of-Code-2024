from enum import Enum
from .loc import Loc

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

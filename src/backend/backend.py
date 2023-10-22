from enum import Enum

class Direction(Enum):
    NORTH   = 0
    EAST    = 1
    SOUTH   = 2
    WEST    = 3

class Square(Enum):
    FLOOR           = 0
    WALL            = 1
    WALL_VISITED    = 2
    BORDER          = 3
    EXIT            = 10
    CHEST           = 20
    TRAP            = 30
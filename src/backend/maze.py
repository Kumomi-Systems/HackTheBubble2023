from backend.backend import Square, Direction
from random import choice as rchoice
from time import sleep

MAZE_HEIGHT = 15
MAZE_WIDTH  = 15
COORDDELTAS_CARDINAL = [
    (-1, 0),
    ( 0,-1),
    ( 0, 1),
    ( 1, 0)
]
COORDDELTAS_DIAGONAL = [
    (-1,-1),
    (-1, 1),
    ( 1,-1),
    ( 1, 1)
]
COORDDELTAS_FULL = COORDDELTAS_CARDINAL + COORDDELTAS_DIAGONAL

Maze = [[Square.WALL for x in range(int(MAZE_WIDTH+2))] for y in range(int(MAZE_HEIGHT+2))]

def GenerateMaze():
    Wilson()
    return Maze

def PopulateMaze():
    Maze = [[Square.WALL for x in range(int(MAZE_WIDTH+2))] for y in range(int(MAZE_HEIGHT+2))]
    # add borders
    for x in range(MAZE_WIDTH+2):
        Maze[0][x]              = Square.BORDER
        Maze[MAZE_HEIGHT+1][x]  = Square.BORDER

    for y in range(MAZE_HEIGHT+2):
        Maze[y][0]              = Square.BORDER
        Maze[y][MAZE_WIDTH+1]   = Square.BORDER

def Wilson():
    PopulateMaze()
    exit = (MAZE_HEIGHT, MAZE_WIDTH)
    Maze[1][1] = Square.FLOOR
    ret = 99
    while(ret == 99):
        ret = RandomWalk(5, 5)
    
    if(type(ret) == list):
        for coord in ret:
            Maze[coord[0]][coord[1]] = Square.FLOOR

    points = [(y,x) for x in range(1, MAZE_WIDTH, 2) for y in range(1, MAZE_HEIGHT, 2) if Maze[y][x] == Square.WALL]
    print(points)

    Maze[5][5] = Square.EXIT
    

def RandomWalk(y, x):
    directions = [
        Direction.NORTH,
        Direction.SOUTH,
        Direction.EAST,
        Direction.WEST
    ]

    Maze[y][x] = Square.FLOOR
    origin = (y,x)
    path = [origin]
    directionsfree = directions.copy()

    while(True):
        if(len(directionsfree)) == 0:
            return 99
        direction = rchoice(directionsfree)
        directionsfree.remove(direction)
        
        if(direction == Direction.NORTH):
            if(y-2 < 1):
                continue
            if((y-2,x) in path):
                continue
            else:
                path.append((y-1,x))
                path.append((y-2,x))
                directionsfree = directions.copy()
                if(Maze[y-2][x] == Square.FLOOR):
                    return path
        
        elif(direction == Direction.SOUTH):
            if(y+2 > MAZE_HEIGHT):
                continue
            if((y+2,x) in path):
                    continue
            else:
                path.append((y+1,x))
                path.append((y+2,x))
                directionsfree = directions.copy()
                if(Maze[y+2][x] == Square.FLOOR):
                    return path

        elif(direction == Direction.EAST):
            if(x+2 > MAZE_WIDTH):
                continue
            if((y,x+2) in path):
                    continue
            else:
                path.append((y,x+1))
                path.append((y,x+2))
                directionsfree = directions.copy()
                if(Maze[y][x+2] == Square.FLOOR):
                    return path

        elif(direction == Direction.WEST):
            if(x-2 < 1):
                continue
            if((y,x-2) in path):
                    continue
            else:
                path.append((y,x-1))
                path.append((y,x-2))
                directionsfree = directions.copy()
                if(Maze[y][x-2] == Square.FLOOR):
                    return path

        y = path[-1][0]
        x = path[-1][1]

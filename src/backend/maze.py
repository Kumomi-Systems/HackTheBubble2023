from backend.backend import Square, Direction
from random import choice as rchoice
from time import sleep

MAZE_HEIGHT = 63
MAZE_WIDTH  = 63
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

# use iterative randomised Prim's algorithm for maze gen
Maze = [[Square.WALL for x in range(int(MAZE_WIDTH+2))] for y in range(int(MAZE_HEIGHT+2))]
Walls = []

def GenerateMaze():
    # add borders
    for x in range(MAZE_WIDTH+2):
        Maze[0][x]              = Square.BORDER
        Maze[MAZE_HEIGHT+1][x]  = Square.BORDER

    for y in range(MAZE_HEIGHT+2):
        Maze[y][0]              = Square.BORDER
        Maze[y][MAZE_WIDTH+1]   = Square.BORDER
    
    Prim()
    return Maze

def RandomWalk(y, x):
    directions = [
        Direction.NORTH,
        Direction.SOUTH,
        Direction.EAST,
        Direction.WEST
    ]
    directionbinds = {
        Direction.NORTH : (-1, 0),
        Direction.SOUTH : ( 1, 0),
        Direction.EAST  : ( 0, 1),
        Direction.WEST  : ( 0,-1)
    }

    Maze[y][x] = Square.FLOOR
    path = [(y,x)]

    for m in range(100):
        direction = rchoice(directions)
        delta = directionbinds[direction]
        Dy = y + delta[0]
        Dx = x + delta[1]

        if((Dy, Dx) in path):
            continue

        if(Maze[Dy][Dx] in [Square.BORDER, Square.WALL_VISITED]):
            continue

        if(Maze[Dy][Dx] == Square.FLOOR and (Dy,Dx) not in path):
            return
        
        # wall not yet visited
        causesLoop = False
        for dir in directions:
            if dir != direction:
                fd = directionbinds[dir]
                if((y+fd[0],x+fd[1]) in path):
                    causesLoop = True

        if(causesLoop):
            continue

        Maze[Dy][Dx] = Square.FLOOR
        path.append((Dy,Dx))
        if(direction in [Direction.NORTH, Direction.SOUTH]):
            wdeltas = [Direction.EAST, Direction.WEST]
        elif(direction in [Direction.EAST, Direction.WEST]):
            wdeltas = [Direction.NORTH, Direction.SOUTH]
        for wdelta in wdeltas:
            wd = directionbinds[wdelta]
            if(Maze[y+wd[0]][x+wd[1]] == Square.WALL):
                Maze[y+wd[0]][x+wd[1]] = Square.WALL_VISITED
        y = Dy
        x = Dx
        
def Wilson():
    exit = (MAZE_HEIGHT, MAZE_WIDTH)
    Maze[1][1] = Square.FLOOR
    RandomWalk(5, 5)
    Maze[5][5] = Square.EXIT


def AllocateSquareAsFloor(y, x):
    Maze[y][x] = Square.FLOOR
    for coorddelta in COORDDELTAS_FULL:
        try:
            if(Maze[y+coorddelta[1]][x+coorddelta[0]] in [Square.WALL, Square.WALL_VISITED]):
                Walls.append((y+coorddelta[1], x+coorddelta[0]))
        except IndexError:
            continue

def Prim():
    AllocateSquareAsFloor(1,1)

    lastcoords = (0,0)
    while(len(Walls) > 0):
        coords = rchoice(Walls)
        adjacentvisits = 0
        for coorddelta in COORDDELTAS_FULL:
            if(adjacentvisits > 3):
                break
            if(coorddelta in COORDDELTAS_DIAGONAL and Maze[coords[0]+coorddelta[0]][coords[1]+coorddelta[1]] == Square.FLOOR):
                break
            elif(Maze[coords[0]+coorddelta[0]][coords[1]+coorddelta[1]] in [Square.FLOOR, Square.WALL_VISITED]):
                adjacentvisits += 1
            
        if(adjacentvisits == 1):
            AllocateSquareAsFloor(coords[0], coords[1])
        
        Walls.remove(coords)
        lastcoords = coords
        # print(Walls)
            
    Maze[lastcoords[0]][lastcoords[1]] = Square.EXIT
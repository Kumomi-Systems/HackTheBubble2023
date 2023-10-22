from backend.backend import Square
from random import choice as rchoice

MAZE_HEIGHT = 63
MAZE_WIDTH  = 63
COORDDELTAS = [(-1,0), (0,1), (1,0), (0,-1)]

# use iterative randomised Prim's algorithm for maze gen
Maze = [[Square.WALL for x in range(int(MAZE_WIDTH+2))] for y in range(int(MAZE_HEIGHT+2))]
Walls = []

def AllocateSquareAsFloor(y, x):
    Maze[y][x] = Square.FLOOR
    for coorddelta in COORDDELTAS:
        try:
            if(Maze[y+coorddelta[1]][x+coorddelta[0]] in [Square.WALL, Square.WALL_VISTED]):
                Walls.append((y+coorddelta[1], x+coorddelta[0]))
        except IndexError:
            continue

def GenerateMaze():
    # add borders
    for x in range(MAZE_WIDTH+2):
        Maze[0][x]              = Square.BORDER
        Maze[MAZE_HEIGHT+1][x]  = Square.BORDER

    for y in range(MAZE_HEIGHT+2):
        Maze[y][0]              = Square.BORDER
        Maze[y][MAZE_WIDTH+1]   = Square.BORDER

    AllocateSquareAsFloor(1,1)

    while(len(Walls) > 0):
        coords = rchoice(Walls)
        adjacentfloors = 0
        for coorddelta in COORDDELTAS:
            if(adjacentfloors > 1):
                break
            if(Maze[coords[0]+coorddelta[0]][coords[1]+coorddelta[1]] == Square.FLOOR):
                adjacentfloors += 1
            
        if(adjacentfloors == 1):
            AllocateSquareAsFloor(coords[0], coords[1])
        
        Walls.remove(coords)
            
    
    return Maze
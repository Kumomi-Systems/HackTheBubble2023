from backend.backend import Square

MAZE_HEIGHT = 63
MAZE_WIDTH  = 63

def GenerateMaze():
    # use iterative randomised Prim's algorithm for maze gen
    Maze = [[Square.WALL for x in range(int(MAZE_WIDTH+2))] for y in range(int(MAZE_HEIGHT+2))]

    # add borders
    for x in range(MAZE_WIDTH+2):
        Maze[0][x]              = Square.BORDER
        Maze[MAZE_HEIGHT+1][x]  = Square.BORDER

    for y in range(MAZE_HEIGHT+2):
        Maze[y][0]              = Square.BORDER
        Maze[y][MAZE_WIDTH+1]   = Square.BORDER

    Maze[1][1] = Square.FLOOR
    
    return Maze
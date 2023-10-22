import backend

MAZE_HEIGHT = 63
MAZE_WIDTH  = 63


def GenerateMaze():
    # use iterative randomised Prim's algorithm for maze gen
    Maze = [[Square.WALL for x in range(int(MAZE_WIDTH+2))] for y in range(int(MAZE_HEIGHT+2))]

    Maze[1][1] = Square.FLOOR
    
    return Maze
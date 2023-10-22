import backend

MAZE_HEIGHT = 63
MAZE_WIDTH  = 63

class Node:
    def __init__(self):
        self.north  = 0
        self.south  = 0
        self.east   = 0
        self.west   = 0

    def BindToNode(self, node, direction):
        if(direction == Direction.NORTH):
            self.north = node
            node.south = self
        elif(direction == Direction.SOUTH):
            self.south = node
            node.north = self
        elif(direction == Direction.EAST):
            self.east = node
            node.west = self
        elif(direction == Direction.WEST):
            self.west = node
            node.east = self

        else:
            raise Exception("Invalid node-bind direction")

def GenerateMaze():
    NodeMap = [[Node() for x in range(int((MAZE_WIDTH-1)/2))] for y in range(int((MAZE_HEIGHT-1)/2))]

    # Add a border 1 unit thick around the maze
    Maze = [[0 for x in range(int(MAZE_WIDTH+2))] for y in range(int(MAZE_HEIGHT+2))]
    
    # top and bottom border
    for x in range(MAZE_WIDTH+2):
        Maze[0][x]                                          = 1
        Maze[MAZE_HEIGHT+1][x]                              = 1
        NodeMap[0][int((x-3)/2)].north                      = None
        NodeMap[int((MAZE_HEIGHT-3)/2)][int((x-3)/2)].south = None

    # left and right border
    for y in range(MAZE_HEIGHT+2):
        Maze[y][0]                                          = 1
        Maze[y][MAZE_WIDTH+1]                               = 1
        NodeMap[int((y-3)/2)][0].west                       = None
        NodeMap[int((y-3)/2)][int((MAZE_WIDTH-3)/2)]        = None
    
    return Maze
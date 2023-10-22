import backend

MAZE_HEIGHT = 255
MAZE_WIDTH  = 255

class Node:
    def __init__(self):
        self.north  = Node()
        self.south  = Node()
        self.east   = Node()
        self.west   = Node()

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
    NodeMap = [[Node() for x in range((MAZE_WIDTH-1)/2)] for y in range((MAZE_HEIGHT-1)/2)]

    # Add a border 1 unit thick around the maze
    Maze = [[0 for x in range(MAZE_WIDTH+2)] for y in range(MAZE_HEIGHT+2)]
    
    # top and bottom border
    for x in range(MAZE_WIDTH+2):
        Maze[0][x]                              = 1
        Maze[MAZE_HEIGHT+1][x]                  = 1
        NodeMap[0][(x-2)/2].north               = None
        NodeMap[MAZE_HEIGHT+1][(x-2)/2].south   = None

    # left and right border
    for y in range(MAZE_HEIGHT+2):
        Maze[y][0]                              = 1
        Maze[y][MAZE_WIDTH+1]                   = 1
        ModeMap[y][0].west                      = None
        NodeMap[y][(MAZE_WIDTH-3)/2]            = None
    
    return Maze
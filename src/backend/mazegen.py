import backend

MAZE_HEIGHT = 256
MAZE_WIDTH  = 256

class Node:
    def __init__(self):
        self.north  = Node()
        self.south  = Node()
        self.east   = Node()
        self.west   = Node()

    def BindToNode(node: Node, direction: Direction):
        if(direction == Direction.NORTH):
            self.north = node
        elif(direction == Direction.SOUTH):
            self.south = node
        elif(direction == Direction.EAST):
            self.east = node
        elif(direction == Direction.WEST):
            self.west = node

        else:
            raise Exception("Invalid node-bind direction")
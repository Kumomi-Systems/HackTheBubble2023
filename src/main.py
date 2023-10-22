import pygame, sys
from backend.maze import GenerateMaze
from backend.backend import Square
import time

from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)

pygame.init()

pixW=640
pixH=480
a = [[0,0,0,0],[1,1,0,0],[0,1,0,0],[1,0,0,0]]
#a = GenerateMaze()
dispW=len(a[0])
dispH=len(a)
squareSize=min(int(pixW/dispW), int(pixH/dispH))

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("AMAZEingly Scary Maze")

wall = pygame.image.load("assets/Wall.png").convert()
floor = pygame.image.load("assets/Floor.png").convert()
player = pygame.image.load("assets/Player2_Transparent.png").convert()
wall = pygame.transform.scale(wall, (squareSize, squareSize))
floor = pygame.transform.scale(floor, (squareSize, squareSize))
player = pygame.transform.scale(player, (squareSize, squareSize))

playerPos = (0,0)
newPos = (0,0)
timeOfLast = 0
timeGap = 0.2
canMove = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

    
    

    if timeOfLast +timeGap < time.time():
        canMove = True
    else:
        canMove = False
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_LEFT] and canMove:
        newPos = (playerPos[0], playerPos[1] - 1)
        timeOfLast = time.time()
    if pressed_keys[K_RIGHT] and canMove:
        newPos = (playerPos[0], playerPos[1] + 1)
        timeOfLast = time.time()
    if pressed_keys[K_UP] and canMove:
        newPos = (playerPos[0] - 1, playerPos[1])
        timeOfLast = time.time()
    if pressed_keys[K_DOWN] and canMove:
        newPos = (playerPos[0] + 1, playerPos[1])
        timeOfLast = time.time()  

    if a[newPos[1]][newPos[0]] not in [1,2,3]:
        playerPos = newPos
    
    screen.fill((0, 0, 0))

    for y in range(dispH):
        for x in range(dispW):

            if a[y][x] in [Square.WALL, Square.WALL_VISTED, Square.BORDER]:
                screen.blit(wall, ((x)*squareSize, (y)*squareSize))
            if a[y][x] == Square.FLOOR:
                screen.blit(floor, ((x)*squareSize, (y)*squareSize))
            if (y,x) == playerPos:
                screen.blit(player, ((x)*squareSize, (y)*squareSize))
            
    
    
    pygame.display.flip()

#FRAMETIMING
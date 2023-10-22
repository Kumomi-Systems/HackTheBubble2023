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
pixH=640
a = GenerateMaze()

for y in range(len(a)):
    for x in range(len(a[y])):
        if a[y][x] == 0:
            a[y][x] == Square.FLOOR
        elif a[y][x] == 1:
            a[y][x] == Square.WALL


#a = GenerateMaze()
dispW=len(a[0])
dispH=len(a)
squareSize=30

screen = pygame.display.set_mode((pixW, pixH))
pygame.display.set_caption("AMAZEingly Scary Maze")

wall = pygame.image.load("assets/Wall.png").convert()
floor = pygame.image.load("assets/Floor.png").convert()
player1 = pygame.image.load("assets/Player1New.png").convert_alpha()
player2 = pygame.image.load("assets/Player2New.png").convert_alpha()
vignette = pygame.image.load("assets/vignette3.png").convert_alpha()
wall = pygame.transform.scale(wall, (squareSize, squareSize))
floor = pygame.transform.scale(floor, (squareSize, squareSize))
player1 = pygame.transform.scale(player1, (squareSize, squareSize))
player2 = pygame.transform.scale(player2, (squareSize, squareSize))
vignette = pygame.transform.scale(vignette, (pixW, pixH))
playeranim = True


playerPos = (1,1)
newPos = (1,1)
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
        playeranim = (playeranim == False)
    if pressed_keys[K_RIGHT] and canMove:
        newPos = (playerPos[0], playerPos[1] + 1)
        timeOfLast = time.time()
        playeranim = (playeranim == False)
    if pressed_keys[K_UP] and canMove:
        newPos = (playerPos[0] - 1, playerPos[1])
        timeOfLast = time.time()
        playeranim = (playeranim == False)
    if pressed_keys[K_DOWN] and canMove:
        newPos = (playerPos[0] + 1, playerPos[1])
        timeOfLast = time.time()  
        playeranim = (playeranim == False)
    

    if a[newPos[0]][newPos[1]] not in [Square.WALL, Square.WALL_VISITED, Square.BORDER, 1]:
        playerPos = newPos
    
    screen.fill((0, 0, 0))

    for y in range(dispH):
        for x in range(dispW):
            pos = ((x)*squareSize - (playerPos[1]+ 0.5) *squareSize + pixW/2, (y)*squareSize - (playerPos[0]+ 0.5) *squareSize + pixH/2)
            if a[y][x] in [Square.WALL, Square.WALL_VISITED, Square.BORDER, 1]:
                screen.blit(wall, pos)
            if a[y][x] in [Square.FLOOR, 0]:
                screen.blit(floor, pos)
            if (y,x) == playerPos:
                if playeranim:
                    screen.blit(player1, pos)
                else:
                    screen.blit(player2, pos)
            
    
    screen.blit(vignette, (0,0))
    pygame.display.flip()
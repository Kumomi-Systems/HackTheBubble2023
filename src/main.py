import pygame, sys
from backend.maze import GenerateMaze
from backend.backend import Square
from backend.enemies import Goblin, Karen
import time
import random

from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)
#s = """
pygame.init()
pygame.mixer.music.load("assets/gameJamCombined.wav")
pygame.mixer.music.play(-1)
#"""
pixW=640
pixH=640
a = GenerateMaze()

# for y in range(len(a)):
#     for x in range(len(a[y])):
#         if a[y][x] == 0:
#             a[y][x] == Square.FLOOR
#         elif a[y][x] == 1:
#             a[y][x] == Square.WALL


#a = GenerateMaze()
dispW=len(a[0])
dispH=len(a)
squareSize=30

screen = pygame.display.set_mode((pixW, pixH))
pygame.display.set_caption("AMAZEingly Scary Maze")

wall = pygame.image.load("assets/Wall.png").convert()
floor = pygame.image.load("assets/Floor.png").convert()
exit = pygame.image.load("assets/Exit.png").convert()
life = pygame.image.load("assets/Heart.png").convert()
chest = pygame.image.load("assets/Chest.png").convert()
# trap = pygame.image.load("assets/Floor.png").convert()
player1 = pygame.image.load("assets/Player1New.png").convert_alpha()
player2 = pygame.image.load("assets/Player2New.png").convert_alpha()
vignette = pygame.image.load("assets/Vignette.png").convert_alpha()
karen = pygame.image.load("assets/karen.png").convert()
wall = pygame.transform.scale(wall, (squareSize, squareSize))
floor = pygame.transform.scale(floor, (squareSize, squareSize))
player1 = pygame.transform.scale(player1, (squareSize, squareSize))
player2 = pygame.transform.scale(player2, (squareSize, squareSize))
vignette = pygame.transform.scale(vignette, (pixW, pixH))
karen = pygame.transform.scale(karen, (squareSize, squareSize))
playeranim = True


playerPos = (1,1)
newPos = (1,1)
timeOfLast = 0
timeGap = 0.2
canMove = True
bullets = []
enemies = []

karencount = 30
for i in range(karencount):
    found = False
    while not found:
        x = random.randrange(dispW)
        y = random.randrange(dispH)
        if a[y][x] in [Square.FLOOR, 0]:
            found = True
    #Make karen object
    #Add to enemies list

goblincount = 30
for i in range(goblincount):
    found = False
    while not found:
        x = random.randrange(dispW)
        y = random.randrange(dispH)
        if a[y][x] in [Square.FLOOR, 0]:
            found = True
    g =  Goblin([y,x])
    #Add to enemies list




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                timeOfLast = 0
            if event.key == pygame.K_DOWN:
                timeOfLast = 0
            if event.key == pygame.K_RIGHT:
                timeOfLast = 0
            if event.key == pygame.K_LEFT:
                timeOfLast = 0
            

    
    

    if timeOfLast +timeGap < time.time():
        canMove = True
    else:
        canMove = False
    pressed_keys = pygame.key.get_pressed()
    prevplayeranim = playeranim
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
    

    if a[newPos[0]][newPos[1]] not in [Square.WALL, Square.BORDER]:
        playerPos = newPos

    if playeranim != prevplayeranim:
        for enemy in enemies:
            if enemy.name == "G":
                bullets = enemy.timestep(a, health, playerPos, bullets)    
            else:
                enemy.timestep(a, health, playerPos)    
        for bullet in bullets:
            bullet.timestep()
            pos = bullet.coordOverlap
            if a[pos[0]][pos[1]]:
                pass

    screen.fill((0, 0, 0))

    for y in range(dispH):
        for x in range(dispW):
            pos = ((x)*squareSize - (playerPos[1]+ 0.5) *squareSize + pixW/2, (y)*squareSize - (playerPos[0]+ 0.5) *squareSize + pixH/2)
            if a[y][x] in [Square.WALL, Square.BORDER]:
                screen.blit(wall, pos)
            elif a[y][x] == Square.FLOOR:
                screen.blit(floor, pos)
            elif a[y][x] == Square.EXIT:
                screen.blit(exit, pos)
            elif a[y][x] == Square.LIFE:
                screen.blit(life, pos)
            elif a[y][x] == Square.TRAP:
                pass

            if (y,x) == playerPos:
                if playeranim:
                    screen.blit(player1, pos)
                else:
                    screen.blit(player2, pos)
    for enemy in enemies:
        pos = enemy.coord
        x = pos[1]
        y = pos[0]
        pos = ((x)*squareSize - (playerPos[1]+ 0.5) *squareSize + pixW/2, (y)*squareSize - (playerPos[0]+ 0.5) *squareSize + pixH/2)
        if enemy.name == "G":
            screen.blit(goblin, pos)
    for bullet in bullets:
        screen.blit(goblin, pos)
            

            
    
    screen.blit(vignette, (0,0))
    pygame.display.flip()


'''
changes made for testing
'''
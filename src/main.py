import pygame, sys
from backend.maze import GenerateMaze
from backend.backend import Square
import time
import random
from backend.button import Button
from playsound import playsound

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

success = pygame.image.load("assets/LeveSuccess.png")
nextlevel = pygame.image.load("assets/nextLevel.png")
wall = pygame.image.load("assets/Wall.png").convert()
floor = pygame.image.load("assets/Floor.png").convert()
exit = pygame.image.load("assets/Exit.png").convert()
life = pygame.image.load("assets/Heart.png").convert_alpha()
chest = pygame.image.load("assets/Chest.png").convert()
trap = pygame.image.load("assets/Trap.png").convert()
splash = pygame.image.load("assets/SplashScreen.png").convert()
player1 = pygame.image.load("assets/Player1New.png").convert_alpha()
player2 = pygame.image.load("assets/Player2New.png").convert_alpha()
vignette = pygame.image.load("assets/Vignette.png").convert_alpha()
playButton = pygame.image.load("assets/play.png").convert_alpha()
#karen = pygame.image.load("assets/karen.png").convert()
wall = pygame.transform.scale(wall, (squareSize, squareSize))
floor = pygame.transform.scale(floor, (squareSize, squareSize))
player1 = pygame.transform.scale(player1, (squareSize, squareSize))
player2 = pygame.transform.scale(player2, (squareSize, squareSize))
vignette = pygame.transform.scale(vignette, (pixW, pixH))
#karen = pygame.transform.scale(karen, (squareSize, squareSize))
exit = pygame.transform.scale(exit, (squareSize, squareSize))
life = pygame.transform.scale(life, (squareSize, squareSize))
trap = pygame.transform.scale(trap, (squareSize, squareSize))
deathscreen = pygame.image.load("assets/deathScreen.png").convert()
invertedMoves=0
playeranim = True

state = 1
inverted = 1

playB = Button(playButton, (320,500))

playerPos = (1,1)
newPos = (1,1)
health = 4
blindnessturns = 0
upHealthNextTurn = False
doDamageNextTurn = False
invertControlsNextTurn = False
timeOfLast = 0
timeGap = 0.2
canMove = True
#bullets = []
#enemies = []
s = """
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
    #Add to enemies list"""

startTime=time.time()
endTime = startTime + 5


while True:
    if(health <= 0):
        state = 2

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
            
    if state == 0:
        if timeOfLast +timeGap < time.time():
            canMove = True
        else:
            canMove = False
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and canMove:
            newPos = (playerPos[0], playerPos[1] - (1*inverted))
            timeOfLast = time.time()
            playeranim = (playeranim == False)
            blindnessturns -= 1
            invertedMoves -= 1
            diceroll = 0
            if(upHealthNextTurn):
                health += 1
                upHealthNextTurn = False
        if pressed_keys[K_RIGHT] and canMove:
            newPos = (playerPos[0], playerPos[1] + (1*inverted) )
            timeOfLast = time.time()
            playeranim = (playeranim == False)
            blindnessturns -= 1
            invertedMoves -= 1
            diceroll = 0
            if(upHealthNextTurn):
                health += 1
                upHealthNextTurn = False
        if pressed_keys[K_UP] and canMove:
            newPos = (playerPos[0] - (1*inverted), playerPos[1])
            timeOfLast = time.time()
            playeranim = (playeranim == False)
            blindnessturns -= 1
            invertedMoves -= 1
            diceroll = 0
            if(upHealthNextTurn):
                health += 1
                upHealthNextTurn = False
        if pressed_keys[K_DOWN] and canMove:
            newPos = (playerPos[0] + (1*inverted), playerPos[1])
            timeOfLast = time.time()  
            playeranim = (playeranim == False)
            blindnessturns -= 1
            invertedMoves -= 1
            diceroll = 0
            if(upHealthNextTurn):
                health += 1
                upHealthNextTurn = False
        

        if a[newPos[0]][newPos[1]] not in [Square.WALL, Square.BORDER]:
            playerPos = newPos

        if a[playerPos[0]][playerPos[1]] == Square.LIFE:
            upHealthNextTurn = True
        elif a[playerPos[0]][playerPos[1]] == Square.TRAP:
            if(diceroll == 0):
                diceroll = random.randint(1,7)
                if(diceroll == 1):
                    blindnessturns = random.randint(3,7)
                elif(diceroll == 2):
                        inverted = -1
                        invertedMoves = 5
                        invertControlsNextTurn = False
                elif(diceroll >= 3):
                    health -= random.randint(1,3)
                # elif(diceroll == 3):
                #     #terror
                #     # playsound("assets/Scary.mp3")
                #     pass

                # if(upHealthNextTurn):
                #     health += 1
                #     upHealthNextTurn = False
                # elif(doDamageNextTurn):
                #     health -= random.randint(1,3)
                #     doDamageNextTurn = False
                # elif(invertControlsNextTurn):
                #     inverted = -1
                #     invertedMoves = 5
                #     invertControlsNextTurn = False


        elif a[playerPos[0]][playerPos[1]] == Square.EXIT:
            a = GenerateMaze()
            playerPos = (1,1)
            state = 3
        s = """
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
                    pass"""

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
                    screen.blit(floor, pos)
                    screen.blit(life, pos)
                elif a[y][x] == Square.TRAP:
                    screen.blit(trap, pos)

                if (y,x) == playerPos:
                    if playeranim:
                        screen.blit(player1, pos)
                    else:
                        screen.blit(player2, pos)
        s = """
        for enemy in enemies:
            pos = enemy.coord
            x = pos[1]
            y = pos[0]
            pos = ((x)*squareSize - (playerPos[1]+ 0.5) *squareSize + pixW/2, (y)*squareSize - (playerPos[0]+ 0.5) *squareSize + pixH/2)
            if enemy.name == "G":
                screen.blit(goblin, pos)
        for bullet in bullets:
            screen.blit(goblin, pos)"""
                

                
        
        screen.blit(vignette, (0,0))
        if(blindnessturns > 0):
            screen.fill(pygame.Color(100, 0, 0, 50))
        if(invertedMoves <= 0):
            inverted = 1

        print(blindnessturns, health)
        pygame.display.flip()

    elif state == 1:
        screen.fill((0, 0, 0))
        screen.blit(splash, (0,0))
        playB.update(screen)
        #screen.blit(vignette, (0,0))
        
        if playB.checkForInput( pygame.mouse.get_pos()) and  pygame.mouse.get_pressed()[0] == True:
            state = 0
        pygame.display.flip()
    elif state == 2:
        screen.fill((0, 0, 0))
        screen.blit(splash, (0,0))
        playB.update(screen)
        #screen.blit(vignette, (0,0))
        
        if playB.checkForInput( pygame.mouse.get_pos()) and  pygame.mouse.get_pressed()[0] == True:
            state = 0
            a = GenerateMaze()
        pygame.display.flip()

    elif state == 3:
        screen.fill(0,0,0)
        screen.blit(success, (0,0))
        nextB = Button(nextlevel, (320,500))
        nextB.update(screen)
        if nextB.checkForInput( pygame.mouse.get_pos()) and  pygame.mouse.get_pressed()[0] == True:
            state = 0
        pygame.display.flip()

'''
changes made for testing
'''
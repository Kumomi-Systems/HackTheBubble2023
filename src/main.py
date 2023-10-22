import pygame, sys
from backend.maze import GenerateMaze
pygame.init()

pixW=640
pixH=480
a = [[0,1,0],[1,1,0],[0,1,0]]
a= GenerateMaze()
dispW=len(a[0])
dispH=len(a)
squareSize=min(int(pixW/dispW), int(pixH/dispH))

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("AMAZEingly Scary Maze")

wall = pygame.image.load("assets/Wall.png").convert()
floor = pygame.image.load("assets/Floor.png").convert()
wall = pygame.transform.scale(wall, (squareSize, squareSize))
floor = pygame.transform.scale(floor, (squareSize, squareSize))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))

    for y in range(dispH):
        for x in range(dispW):
            if a[y][x] == 1:
                #pygame.draw.circle(screen, (0, 0, 255), , squareSize/2)
                screen.blit(wall, ((x)*squareSize, (y)*squareSize))
            if a[y][x] == 0:
                #pygame.draw.circle(screen, (0, 255, 0), ((x+1/2)*squareSize, (y+1/2)*squareSize), squareSize/2)
                screen.blit(floor, ((x)*squareSize, (y)*squareSize))
            
    
    
    pygame.display.flip()

#FRAMETIMING
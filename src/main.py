import pygame, sys
pygame.init()

pixW=640
pixH=480
a = [[0,1,0],[1,1,0],[0,1,0]]
dispW=len(a[0])
dispH=len(a)
squareSize=min(int(pixW/dispW), int(pixH/dispH))
w=0
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Spooky Maze")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    w+=1
    for y in range(dispH):
        for x in range(dispW):
            pass
    pygame.draw.circle(screen, (0, 0, 255), (250+w, 250), 75)

    pygame.display.flip()
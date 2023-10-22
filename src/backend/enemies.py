import sys
import time

class Karen:
    isFollowing = False
    def __init__(self, listCoord):
        self.listCoord = listCoord

    def moveKaren(self,varChange,varAxis):
        """
        varChange is external value passed to tell the listCoord how to change
        can be '+ve' or '-ve' 
        varAxis tells program which axis the movement is made on 
        """
        if isFollowing:
            if varAxis == 'y':
                if varChange == '+ve':
                    listCoord[1]+=1
                elif varChange == '-ve':
                    listCoord[1]-=1
                else:
                    print("Invalid changer.")
                    sys.exit(1)
            
            elif varAxis == 'x':
                if varChange == '+ve':
                    listCoord[0]+=1
                elif varChange == '-ve':
                    listCoord[0]-=1
                else:
                    print("Invalid changer.")
                    sys.exit(1)

            else:
                print("Invalid axis.")
                sys.exit(1)
    
    def checkProximity(self,playerCoord,proximal):
        '''
        checks for proximity of player
        if Karen is within a distance defined by 'proximal' parameter, changes the value of isFollowing to True if not already True
        '''
        if not self.isFollowing:
            
        else:
            pass



class Goblin:
    def __init__(self, coord):
        self.coord = coord
        self.lastshot = 1
        self.gap = 1    
    def timestep(self, a, health, playerPos, bullets):
        if self.lastshot > self.gap:
            if abs(self.coord[0] - playerPos[0]) > abs(self.coord[1] - playerPos[1]):
                if self.coord[0] - playerPos[0] > 0:
                    direction = 3
                else:
                    direction = 1
            elif abs(self.coord[0] - playerPos[0]) < abs(self.coord[1] - playerPos[1]):
                if self.coord[1] - playerPos[1] > 0:
                    direction = 4
                else:
                    direction = 2
            else:
                direction = randrange(4)
            b = Bullet(self.coord, direction)
            bullets.append(b)
            self.lastshot = 0
        self.lastshot += 1

class Bullet:
    def __init__(self, coord, direction):
        self.coord = coord
        self.direction = direction
    
    def timestep(self):
        if direction == 0:
            coord[1] += 1
        elif direction == 1:
            coord[0] += 1
        elif direction == 2:
            coord[1] -= 1
        elif direction == 3:
            coord[0] -= 1


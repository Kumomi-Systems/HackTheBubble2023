import sys
import time
import random
from backend.backend import Square
class Karen:
    isFollowing = False
    def __init__(self, listCoord):
        self.listCoord = listCoord

    
    def checkProximity(self,playerCoord,proximal):
        '''
        checks for proximity of player
        if Karen is within a distance defined by 'proximal' parameter, changes the value of isFollowing to True if not already True
        #temp - working
        '''

        if not self.isFollowing:
            if abs(playerCoord[0]-self.listCoord[0]) <= proximal or abs(playerCoord[1]-self.listCoord[1]):
                self.isFollowing = True
        
        else:
            pass
    
    def shout(self,fileName):
        print(functional.randomAction(fileName))

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

    def karenAction(self, playerCoord, proximal, varChange, varAxis):
        """
        check for tile overlap, if yes, destroy and return damage code
        ->check for movement
        -> move
        -> shout 
        -> check for tile
        """
        if playerCoord == listCoord:
            #go poof
            pass
        else:
            pass
    
        self.checkProximity(playerCoord,listCoord)
        if isFollowing:
            self.moveKaren(varChange, varAxis)
        else: 
            pass
        
        if playerCoord == listCoord:
            #go poof
            pass
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
                direction = random.randrange(4)
            b = Bullet(self.coord, direction)
            bullets.append(b)
            self.lastshot = 0
        self.lastshot += 1
        return bullets

class Bullet:
    def __init__(self, coord, direction):
        self.coord = coord
        self.direction = direction
    
    def timestep(self, a):
        direction = self.direction
        if direction == 1:
            self.coord[1] += 1
        elif direction == 2:
            self.coord[0] += 1
        elif direction == 3:
            self.coord[1] -= 1
        elif direction == 4:
            self.coord[0] -= 1


class Player:
    def __init__(self, playerCoord, playerHealth):
        self.playerCoord = playerCoord
        self.playerHealth = playerHealth

    #GETTER FOR PLAYER COORDS
    def get_location(self):
        return self.playerCoord

    def doDamage(self, damager):
        #reduces health
        self.playerHealth-=damager
    
    def movePlayer(self,varAxis,changer):
        if 
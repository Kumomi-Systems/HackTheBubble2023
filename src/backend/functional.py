#import pygame
from sys import path as p
from random import randint
import os

path = os.path.abspath("assets")
p.append(path)

def checkOverlap(tupBox,tupPlayer,widthBox = 1,widthPlayer = 1):
    """
    Checks for overlap of Player in Box
    tupBox is centre of Box
    tupPlayer is centre of Player 
    """

    if tupPlayer[0]-(widthPlayer/2) < tupBox[0]+(widthBox/2):
        return True
    elif tupBox[0]-(widthBox/2) < tupPlayer[0]+(widthPlayer/2):
        return True
    elif tupBox[1]+(widthPlayer/2) > tupPlayer[1]-(widthPlayer/2):
        return True
    elif tupBox[1]-(widthBox/2) < tupPlayer[1]+(widthPlayer/2):
        return True
    else:
        return False



def randomAction(fileName):
    """
    actions for enemies
    returns action to be made
    support for adding more enemies in future    
    """


    with open(fileName,"r") as file1:
        listActions = file1.readlines()
        numActions = len(listActions)
        numIndex = randint(0,numActions-1)

    return listActions[numIndex]

def characterDeath(health):
    pass
def characterDamage(playerCoord, bulletCoord):
    if playerCoord == bulletCoord:
        pass
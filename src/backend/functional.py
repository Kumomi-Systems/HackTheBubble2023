import pygame

def checkOverlap(tupBox,tupPlayer,widthBox = 1,widthPlayer = 1):
    """
    Checks for overlap of Player in Box
    tupBox is centre of Box
    tupPlayer is centre of Player 
    """

    if '''check rBox against lPlay''' tupPlayer[0]-(widthPlayer/2)'''lPlayer''' < tupBox[0]+(widthBox/2)'''rBox''':
        return True
    elif '''check lBox against rPlay''' tupBox[0]-(widthBox/2)'''lBox''' < tupPlayer[0]+(widthPlayer/2)'''rPlay''':
        return True
    elif '''tBox against bPlay''' tupBox[1]+(widthPlayer/2)'''tBox''' > tupPlayer[1]-(widthPlayer/2)'''bPlay''':
        return True
    elif '''bBox against tPlay''' tupBox[1]-(widthBox/2)'''bBox''' < tupPlayer[1]+(widthPlayer/2)'''tPlay''':
        return True
    else:
        return False
import sys

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
    pass
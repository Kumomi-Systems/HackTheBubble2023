import sys

class Karen:
    isFollowing = False
    def __init__(self, listCoord):
        self.listCoord = listCoord

    def method1(self,varChange,varAxis):
        """
        varChange is external value passed to tell the listCoord how to change
        can be '+ve' or '-ve' 
        varAxis tells program which axis the movement is made on 
        """
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
        


        
    

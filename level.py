from walls import Walls
class Level():
    
    def __init__(self, level_number):
        #set wall
        self.walls = []
        
        if level_number == 1:                                          
            walls_color = (50,50,50)          
            wall_number = 7
            walls_x =      [    0,  300,  375,  450,  525,  600,    0]
            walls_y =      [  -75, -150, -300, -150, -225, -150, -500]
            walls_width =  [10000,   75,   75,   75,   75,   75,   75]
            walls_height = [   75,   75,   75,   75,  150,   75,  450]
            
            if wall_number * 4 == len(walls_x) + len(walls_y) +len(walls_width) + len(walls_height):  #? So gross mais ça marche (en gros check si la liste des walls est bien construite)
                for i in range(wall_number):
                    self.walls.append(Walls(walls_x[i], walls_y[i], walls_width[i], walls_height[i], walls_color ))
            else:
                print("[Walls 1] [-]   Walls' list isn't in the good shape ")
    
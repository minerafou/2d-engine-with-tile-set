from walls import Walls

def SetLevel(level_number):
    #set level walls
    walls = []
    if level_number == 1:
        #base color
        color = (120, 120, 120)
        walls_x =      [    0,  300,  375,  450,  525,  600,    0,  225,   75]
        walls_y =      [  -75, -150, -300, -150, -225, -150, -525, -375, -450]
        walls_width =  [10000,   75,   75,   75,   75,   75,   75,   75,   75]
        walls_height = [   75,   75,   75,   75,  150,   75,  450,   75,   75]
        walls_color =  [color,color,color,color,color,color,color,color,color]
        walls_tag   =  [ None, None, None, None, None, None, None, None, None]
        for i in range(len(walls_x)):
            walls.append(Walls(walls_x[i], walls_y[i], walls_width[i], walls_height[i], walls_color[i], walls_tag[i]))
    return walls
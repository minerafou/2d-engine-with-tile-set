import pygame

def SetWalls():
    #set level walls
    walls = []
    walls_x =      [    0,  300,  375,  450,  525,  600,    0,  225,   75]
    walls_y =      [  -75, -150, -300, -150, -225, -150, -525, -375, -450]
    walls_width =  [10000,   75,   75,   75,   75,   75,   75,   75,   75]
    walls_height = [   75,   75,   75,   75,  150,   75,  450,   75,   75]
    for i in range(len(walls_x)):
        walls.append(Walls(walls_x[i], walls_y[i], walls_width[i], walls_height[i]))
    return walls

class Walls():
    def __init__(self, x, y, width, height):
        #init coord
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def DrawWall(self, screen, screen_height, camera_x, camera_y):
        #set rect
        wall_rect = pygame.Rect(self.x - camera_x, self.y + screen_height - camera_y, self.width, self.height)
        #draw rect
        pygame.draw.rect(screen, (50, 50, 50), wall_rect)
    def GetRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
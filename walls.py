import pygame

def SetWalls():
    #set level walls
    walls = []
    walls.append(Walls(0, 50, 1000, 50))
    walls.append(Walls(300, 300, 100, 250))
    return walls

class Walls():
    def __init__(self, x, y, width, height):
        #init coord
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def DrawWall(self, screen, screen_width, screen_height):
        #set rect
        wall_rect = pygame.Rect(self.x, screen_height - self.y, self.width, self.height)
        #draw rect
        pygame.draw.rect(screen, (50, 50, 50), wall_rect)
    def GetRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
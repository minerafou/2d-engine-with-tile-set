import pygame

class Walls():
    def __init__(self, x, y, width, height, color, tag):
        #init coord
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.tag = tag
    def DrawWall(self, screen, screen_height, camera_x, camera_y):
        #set rect
        wall_rect = pygame.Rect(self.x - camera_x, self.y + screen_height - camera_y, self.width, self.height)
        #draw rect
        pygame.draw.rect(screen, self.color, wall_rect)
    def GetRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
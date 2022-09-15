import pygame

class Walls():
    def __init__(self, block):
        #init coord
        self.block = block
        

    def DrawWall(self, screen, screen_height, camera_x, camera_y, x, y, number_of_height, level, tile, tile_size):
        screen.blit(tile, ((x * tile_size) - camera_x, (y * tile_size) - camera_y - (number_of_height * tile_size) + screen_height))
    
    def GetRect(self, y, x, number_of_height, tile_size):
        return pygame.Rect(x * tile_size, y * tile_size - (number_of_height) * tile_size, tile_size, tile_size)
    
    def GetBlock(self):
        return self.block


 
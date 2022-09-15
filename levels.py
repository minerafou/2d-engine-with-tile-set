from walls import Walls
import pygame
from tile_dict import GetDict

class Level():
    def __init__(self, level_num):

        self.level_num = level_num
        self.tile_size = 40

        self.tile_dict = GetDict()
        self.level, self.tile_level = self.SetLevel(level_num)

    def SetLevel(self, level_number):
        #set level walls
        level = []
        if level_number == 1:
            #set text
            level_file_name = "level_" + str(level_number) + ".txt"
            text_file = open(level_file_name, "r")
            line = text_file.readline()
            while line:
                line_list = [i for i in line]
                if line_list[len(line_list) - 1] == "\n":
                    line_list.pop()
                class_line_list = []
                for i in line_list:
                    class_line_list.append(Walls(i))
                level.append(class_line_list)
                line = text_file.readline()
        
        tile_level = []
        for y in range(len(level)):
            for x in range(len(level[y])):
                #check for surounding tile
                change_surounding = [[-1, -1], [0, -1], [1, -1],[-1, 0], [1, 0],[-1, 1], [0, 1], [1, 1]]
                surounding_tiles = []
                for i in change_surounding:
                    new_x = x + i[0]
                    new_y = y + i[1]
                    #check if block is out of screen
                    if new_y > len(level) - 1:
                        target_block = level[y][x].GetBlock()
                    elif new_y < 0:
                        target_block = level[y][x].GetBlock()
                    elif new_x > len(level[0]) - 1:
                        target_block = level[y][x].GetBlock()
                    elif new_x < 0:
                        target_block = level[y][x].GetBlock()
                    elif level[new_y][new_x].GetBlock() == "1":
                        target_block = 1
                    else:
                        target_block = 0
                    surounding_tiles.append(int(target_block))
                
                #set image
                tile_tbd = self.CheckForTile(surounding_tiles, level[y][x].GetBlock())
                #image_tbd = self.CheckForTile()
                #resize image
                tile_tbd = pygame.transform.scale(tile_tbd, (self.tile_size, self.tile_size))
                tile_level.append(tile_tbd)

        return level, tile_level
        
    
    def DrawLevel(self, screen, screen_height, camera_x, camera_y):
        
        #draw walls   
        for y in range(len(self.level)):
            for x in range(len(self.level[y])):
                
                index = y * len(self.level[y]) + x
                #draw image
                tile_tbd = self.tile_level[index]
                walls_class = self.level[y][x]
                walls_class.DrawWall(screen, screen_height, camera_x, camera_y, x, y, len(self.level), self.level, tile_tbd, self.tile_size)
        
    def GetLevel(self):
        return self.level
    
    def GetTileSize(self):
        return self.tile_size

    def CheckForTile(self, surounding_tile, current_tile):

        tile = self.tile_dict.get(str(surounding_tile), ".png")
        if current_tile == "0":
            return (pygame.image.load("tile set game/air.png").convert())
        elif current_tile == "1":
            prefix = "tile set game/dirt_"
        return (pygame.image.load(prefix + tile).convert())
    
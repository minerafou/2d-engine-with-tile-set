import pygame

class Player:
    def __init__(self, x, y):
        #init le player
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25 

        self.velocity_x = 0
        self.velocity_y = 0

        self.right_pressed = False
        self.left_pressed = False

        self.jumpable = False
    
    def SetPressedKey(self, dir):
        if dir == "right":
            self.right_pressed = True
        if dir == "left":
            self.left_pressed = True


    #? à mettre dans SetPressedKey()
    def Jump(self):
        #jump le player
        #check if player can jump
        if self.jumpable:
            self.velocity_y = -10

    def Draw(self, screen, screen_height, camera_x, camera_y):
        #set rect
        player_rect = pygame.Rect(self.x - camera_x, self.y + screen_height - camera_y, self.width, self.height)
        pygame.draw.rect(screen, (0, 50, 50), player_rect)

    def UpdatePos(self, walls):
        
        #? au lieu de mettre la variable en False pendant le saut, checker dans Jump() si il peut
        #set the jump statut to false
        self.jumpable = False

        #? mettre la velocity sous forme velocity = [x,y] au lieu de 2 variable distincte 
        #update velocity_y
        self.velocity_y += 0.5

        #cap velovity_y
        if self.velocity_y > 15:
            self.velocity_y = 15

        #update coords y
        self.y += self.velocity_y

        #? Je sais pas comment dire mais Mehhh.
        #check colide and addapt position
        if self.velocity_y > 0:
            self.x, self.y = self.CheckCollid(self.x, self.y, walls, "down")
        else:
            self.x, self.y = self.CheckCollid(self.x, self.y, walls, "up")


        #?  !??? redondance avec SetPressedKey ???!
        #set and update velocity_x
        if self.left_pressed:
            self.velocity_x -= 1
        elif self.right_pressed:
            self.velocity_x += 1
        else:
            if self.velocity_x > 0:
                self.velocity_x -= 1
            elif self.velocity_x < 0:
                self.velocity_x += 1
        
        
        #?detection de la velocity (tag ou variable) pour des applications plus pousser 
        #cap velovity_x
        if self.velocity_x > 7:
            self.velocity_x = 7
        elif self.velocity_x < -7:
            self.velocity_x = -7
        
        #update coords x
        self.x += self.velocity_x / 2

        #check collition left right
        if self.velocity_x > 0:
            self.x, self.y = self.CheckCollid(self.x, self.y, walls, "right")
        else:
            self.x, self.y = self.CheckCollid(self.x, self.y, walls, "left")

        #reset pressed keys
        self.right_pressed = False
        self.left_pressed = False

    def CheckCollid(self, x, y, walls, dir):
        #set player rect
        temp_player_rect = pygame.Rect(x, y, self.width, self.height)

        #set default variable
        collid = False

        #check collition
        for i in walls:
            if temp_player_rect.colliderect(i.GetRect()):
                collid = True
                if dir == "up" or dir == "down":
                    self.velocity_y = 0
                elif dir == "left" or dir == "right":
                    self.velocity_x = 0
                #check if player can jump
                if dir == "down":
                    self.jumpable = True
        if collid:
            #do recurtion to sitck perfect to the block
            if dir == "down":
                x, y = self.CheckCollid(x, (y - 0.5), walls, dir)
            elif dir == "up":
                x, y = self.CheckCollid(x, (y + 0.5), walls, dir)
            elif dir == "right":
                x, y = self.CheckCollid((x - 0.5), y, walls, dir)
            elif dir == "left":
                x, y = self.CheckCollid((x + 0.5), y, walls, dir)
        return x, y
    def GetPos(self):
        return self.x, self.y
import pygame

class Player:
    def __init__(self, x, y):
        #init le player
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10

        self.velocity_x = 0
        self.velocity_y = 0

        self.right_pressed = False
        self.left_pressed = False
    
    def SetPressedKey(self, dir):
        if dir == "right":
            self.right_pressed = True
        if dir == "left":
            self.left_pressed = True

    def Jump(self):
        #jump le player
        self.velocity_y = 10

    def Draw(self, screen, screen_width, screen_height):
        #set rect
        player_rect = pygame.Rect(self.x, screen_height - self.y - self.height, self.width, self.height)
        pygame.draw.rect(screen, (50, 50, 50), player_rect)

    def UpdatePos(self, walls):
        #update velocity_y
        self.velocity_y -= 0.5

        #cap velovity_y
        if self.velocity_y < -7:
            self.velocity_y = -7

        #update coords y
        self.y += self.velocity_y

        #check colide and addapt position
        self.y = self.CheckYCollid(self.x, self.y, walls)

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
        
        #cap velovity_x
        if self.velocity_x > 7:
            self.velocity_x = 7
        elif self.velocity_x < -7:
            self.velocity_x = -7
        
        #update coords x
        self.x += self.velocity_x / 2

        #reset pressed keys
        self.right_pressed = False
        self.left_pressed = False

    def CheckYCollid(self, x, y, walls):
        temp_player_rect = pygame.Rect(x, y, self.width, self.height)
        collid = False
        for i in walls:
            if i.GetRect().colliderect(temp_player_rect):
                collid = True
                self.velocity_y = 0
        if collid:
            y = self.CheckYCollid(x, (y + 0.5), walls)
        return y

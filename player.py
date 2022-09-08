import pygame

class Player:
    def __init__(self, x, y):
        #init le player
        self.x = x
        self.y = y

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
        pass

    def Draw(self, screen):
        #set rect
        player_rect = pygame.Rect(self.x, self.y, 10, 10)
        pygame.draw.rect(screen, (50, 50, 50), player_rect)

    def UpdatePos(self):
        #set and update velocity
        if self.left_pressed:
            self.velocity_x -= 1
        elif self.right_pressed:
            self.velocity_x += 1
        else:
            if self.velocity_x > 0:
                self.velocity_x -= 1
            elif self.velocity_x < 0:
                self.velocity_x += 1
        
        #cap velovity
        if self.velocity_x > 7:
            self.velocity_x = 7
        elif self.velocity_x < -7:
            self.velocity_x = -7
        print(self.velocity_x)

        #update coords
        self.x += self.velocity_x

        #reset pressed keys
        self.right_pressed = False
        self.left_pressed = False

    

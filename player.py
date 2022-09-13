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

        self.is_in_air = True

        self.velocity_x_cap = 8
        self.velocity_y_cap = 15

        self.number_of_jump = 2
        self.jump_left = 0
    
    def SetPressedKey(self, dir):
        if dir == "right":
            self.right_pressed = True
        if dir == "left":
            self.left_pressed = True

    def Jump(self, space_state):
        #jump le player
        #check if player can jump
        if space_state:
            #check if can jump
            if self.jump_left > 0:
                #check if first jump
                if self.jump_left == self.number_of_jump:
                    self.jump_left -= 1
                    self.velocity_y = -10
                else:
                    if not self.previous_state:
                        self.jump_left -= 1
                        self.velocity_y = -10

        self.previous_state = space_state

    def Draw(self, screen, screen_height, camera_x, camera_y):
        #set rect
        player_rect = pygame.Rect(self.x - camera_x, self.y + screen_height - camera_y, self.width, self.height)
        pygame.draw.rect(screen, (0, 50, 50), player_rect)

    def UpdatePos(self, walls):
        #set the jump statut to false
        self.is_in_air = True

        #update velocity_y
        self.velocity_y += 0.5

        #cap velovity_y
        if self.velocity_y > self.velocity_y_cap:
            self.velocity_y = self.velocity_y_cap

        #update coords y
        self.y += self.velocity_y

        #check colide and addapt position
        if self.velocity_y > 0:
            self.x, self.y = self.CheckCollid(self.x, self.y, walls, "down")
        else:
            self.x, self.y = self.CheckCollid(self.x, self.y, walls, "up")
        
        #reset jump_count
        if not self.is_in_air:
            self.jump_left = self.number_of_jump

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
        if self.velocity_x > self.velocity_x_cap:
            self.velocity_x = self.velocity_x_cap
        elif self.velocity_x < -self.velocity_x_cap:
            self.velocity_x = -self.velocity_x_cap
        
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
                    collided_wall = i.GetRect()
                elif dir == "left" or dir == "right":
                    self.velocity_x = 0
                    collided_wall = i.GetRect()
                #check if player can jump
                if dir == "down":
                    self.is_in_air = False
        if collid:
            #do recurtion to sitck perfect to the block
            if dir == "down":
                x, y = x, collided_wall[1] - self.height
            elif dir == "up":
                x, y = x, collided_wall[1] + collided_wall[3]
            elif dir == "right":
                x, y = collided_wall[0] - self.width, y
            elif dir == "left":
                x, y = collided_wall[0] + collided_wall[2], y
        return x, y
    def GetPos(self):
        return self.x, self.y
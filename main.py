#pygame import and init pygame
import pygame
pygame.init()

#import external class and function
from player import Player
from levels import Level

#classs pricipal
class Game():
    def __init__(self, screen, screen_width, screen_height):
        #set screen related variable
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        #set variable pour le jeu
        self.running = True
        self.game_screen = "play_scene"

        #init une clock
        self.main_clock = pygame.time.Clock()

        #set player
        self.player = Player(100, -200, (0, 50, 50)) 

        #set level
        self.level_num = 1
        self.current_level = Level(self.level_num)
        self.level = self.current_level.GetLevel()

        #variable camera
        self.camera_x = 0
        self.camera_y = 0

    def Run(self):
        while self.running:
            self.HandleEvent()
            self.Update()
            self.Refresh()
            self.main_clock.tick(60)
    
    def HandleEvent(self):
        #verifie les evenement pygame
        for event in pygame.event.get():
            #check des input joueur
            #input de la croix rouge (en haut a droite de la fenetre)
            if event.type == pygame.QUIT:
                self.running = False

            #check le temps
            if event.type == pygame.USEREVENT:
                self.EveryTenMilliSecAction()
            
            #input de la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #left button
                    pass

                elif event.button == 3:
                    #right button
                    pass
                
                elif event.button == 2:
                    #middle button
                    pass
            
            #check input clavier
            if self.game_screen == "play_scene":
                #check for 1 input key
                if event.type == pygame.KEYDOWN:

                    #quit the game
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    
                #check for long press
                #move player
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q] or keys[pygame.K_d]:
                    self.player.SetPressedKey(keys)
                
                #jump player
                self.player.Jump(keys[pygame.K_SPACE])

    def Update(self):
        #update screen size
        self.screen_width, self.screen_height = self.screen.get_size()

        if self.game_screen == "play_scene":
            #delete tous sur l'ecran
            self.screen.fill((240, 240, 240))

            #update player pos
            self.player.UpdatePos(self.level, self.current_level.GetTileSize())

            #draw level
            self.current_level.DrawLevel(self.screen, self.screen_height, self.camera_x, self.camera_y)

            #draw player
            self.player.Draw(self.screen, self.screen_height, self.camera_x, self.camera_y)

            #check for camera
            self.camera_x, self.camera_y = self.CheckCamera(self.camera_x, self.camera_y)
    
    def Refresh(self):
        pygame.display.flip()
    
    def EveryTenMilliSecAction(self):
        pass

    def CheckCamera(self, camera_x, camera_y):
        #get player pos
        player_x, player_y = self.player.GetPos()

        #move camera x
        if player_x > self.screen_width + camera_x - 200:
            camera_x = player_x - (self.screen_width - 200)
        if player_x < camera_x + 200:
            camera_x = player_x - 200
        
        #move camera y
        if player_y < -1 * self.screen_height + camera_y + 100:
            camera_y = player_y - (-1 * self.screen_height + 100)
        if player_y > camera_y - 200:
            camera_y = player_y + 200

        #cap camera
        if camera_x < 0:
            camera_x = 0
        if camera_y > 0:
            camera_y = 0


        return camera_x, camera_y

#start un event toute les 10 milli sec
pygame.time.set_timer(pygame.USEREVENT, 10)

#set taille fenetre
screen_width = 800

screen_height = 600

#set la fenetre
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Test Python Game")

#cree le jeu a partir le l'objet 'game'
game1 = Game(screen, screen_width, screen_height)

#lance la boucle global
game1.Run()

#quitte pygame
pygame.quit()


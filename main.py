#pygame import and init pygame
import pygame
pygame.init()

#import external class and function
from player import Player
from walls import Walls, SetWalls

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
        self.player = Player(100, 100) 

        #set wall
        self.walls = SetWalls()


    def Run(self):
        while self.running:
            self.HandleEvent()
            self.Update()
            self.Refresh()
            self.main_clock.tick(2)
    
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
                    
                    #move player
                    if event.key == pygame.K_SPACE:
                        self.player.Jump()

                #check for long press
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    self.player.SetPressedKey("left")
                if keys[pygame.K_d]:
                    self.player.SetPressedKey("right")

    def Update(self):
        #update screen size
        self.screen_width, self.screen_height = self.screen.get_size()

        if self.game_screen == "play_scene":
            #delete tous sur l'ecran
            self.screen.fill((240, 240, 240))

            #update player pos
            self.player.UpdatePos(self.walls)

            #draw player
            self.player.Draw(self.screen, self.screen_width, self.screen_height)

            #draw walls
            for i in self.walls:
                i.DrawWall(self.screen, self.screen_width, self.screen_height)
    
    def Refresh(self):
        pygame.display.flip()
    
    def EveryTenMilliSecAction(self):
        pass

#start un event toute les 10 milli sec
pygame.time.set_timer(pygame.USEREVENT, 10)

#set taille fenetre
screen_width = 1200

screen_height = 800

#set la fenetre
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Test Python Game")

#cree le jeu a partir le l'objet 'game'
game1 = Game(screen, screen_width, screen_height)

#lance la boucle global
game1.Run()

#quitte pygame
pygame.quit()


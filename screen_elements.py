import pygame
import sys

from settings import Settings
from rect_config import *

class InicialScreen:
    def __init__(self, ai_game):
        """Inicializa las características del tutorial inicial"""
        pygame.init()

        self.ai_game = ai_game
        self.ai_event = ai_game.key_pressed
        self.pantalla = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/pantalla_inicial.bmp')
        self.screen_rect = ai_game.screen.get_rect()
        self.rect = self.image.get_rect()

        #Coloca la imagen en su sitio correspondiente
        if ai_game.formato_pantalla.upper() == 'COMPLETO':
            self.rect.midtop = self.screen_rect.midtop
            self.rect = self.rect.midtop
        elif ai_game.formato_pantalla.upper() == 'VENTANA':
            self.rect.midtop = self.screen_rect.midtop
    
    def image_show(self):
        if self.ai_event == False:
            self.pantalla.blit(self.image, self.rect)

class LivesCounter:
    def __init__(self, ai_game):
        """Clase para crear un contador de vidas"""
        pygame.init()
        self.ai_game = ai_game
        self.lives = ai_game.number_lives
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings= ai_game.settings

        #Carga las diferentes imágenes
        self.image_live = pygame.image.load('images/live.bmp')
        self.image_death = pygame.image.load('images/death.bmp')
        self.game_over_image = pygame.image.load('images/game_over.bmp')
        #Carga los rects de las diferentes imágenes
        self.image_live_rect = self.image_live.get_rect()
        self.image_death_rect = self.image_death.get_rect()
        self.game_over_image_rect = self.game_over_image.get_rect()

        #Configura el corazón correspondiente a cada una de las vidas/muertes.
        #Configura las imágenes de las VIDAS
        self.image_live_1 = self.image_live
        self.image_live_2 = self.image_live
        self.image_live_3 = self.image_live
        #Configura las imágenes de las MUERTES
        self.image_death_1 = self.image_death
        self.image_death_2 = self.image_death
        self.imgae_death_3 = self.image_death

        #Configura los rects de cada unas de las VIDAS.
        self.live_1_rect = self.image_live_rect.copy()
        self.live_2_rect = self.image_live_rect.copy()
        self.live_3_rect = self.image_live_rect.copy()
        #Configura los rescts de cada una de las MUERTES.
        self.death_1_rect = self.image_death_rect.copy()
        self.death_2_rect = self.image_death_rect.copy()
        self.death_3_rect = self.image_death_rect.copy()

        #Determina el tamaño del rect de los corazones
        self.live_width, self.live_height = self.image_live.get_size() 
        self.death_width, self.death_height = self.image_death.get_size()

    def show_lives_number(self):
        """Muestra el número de vidas junto a un corazón"""
        if self.lives == 3:
            self.live_1_rect.center = config_position(self.image_live, self.ai_game, 1)

            self.live_2_rect.center = config_position(self.image_live, self.ai_game, 2)

            self.live_3_rect.center = config_position(self.image_live, self.ai_game, 3) 
       
            self.screen.blit(self.image_live_1, self.live_1_rect)
            self.screen.blit(self.image_live_2, self.live_2_rect)
            self.screen.blit(self.image_live_3, self.live_3_rect)

        if self.lives == 2:
            self.live_1_rect.center = config_position(self.image_live, self.ai_game, 1)

            self.live_2_rect.center = config_position(self.image_live, self.ai_game, 2)

            self.death_1_rect.center = config_position(self.image_death, self.ai_game, 3)

            self.screen.blit(self.image_live, self.live_1_rect)
            self.screen.blit(self.image_live, self.live_2_rect)
            self.screen.blit(self.image_death, self.death_1_rect)
        
        if self.lives == 1:
            self.live_1_rect.center = config_position(self.image_live, self.ai_game, 1)

            self.death_2_rect.center = config_position(self.image_death, self.ai_game, 2)

            self.death_1_rect.center = config_position(self.image_death, self.ai_game, 3)

            self.screen.blit(self.image_live, self.live_1_rect)
            self.screen.blit(self.image_death, self.death_2_rect)
            self.screen.blit(self.image_death, self.death_1_rect)

        if self.lives == 0:
            """Muestra una pantalla de game over junto a 3 corazones negros."""
            self.death_3_rect.center = config_position(self.image_death, self.ai_game, 1)

            self.death_2_rect.center = config_position(self.image_death, self.ai_game, 2)

            self.death_1_rect.center = config_position(self.image_death, self.ai_game, 3)

            self.screen.blit(self.game_over_image, self.config_game_over_show())
            self.screen.blit(self.image_death, self.death_3_rect)
            self.screen.blit(self.image_death, self.death_2_rect)
            self.screen.blit(self.image_death, self.death_1_rect)

    def config_game_over_show(self):
            """Prepara la pantalla de game over para ser mostrada"""
            if self.lives <= 0:
                self.game_over_image_rect = (self.screen_rect[0] // 2, self.screen_rect[1] // 2)
                
                return self.game_over_image_rect
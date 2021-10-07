from settings import Settings
import pygame
import sys

class Screen():
    def __init__(self, ai_game):
        """Inicializa las características de la pantalla principal"""
        pygame.init()

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

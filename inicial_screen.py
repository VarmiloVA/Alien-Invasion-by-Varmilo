from alien_invasion.settings import Settings
import pygame

class Screen:
    def __init__(self, ai_game):
        """Inicializa las características de la pantalla principal"""
        pygame.init()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/pantalla_inicial.bmp")
        self.rect = self.image.get_rect()

        #Coloca la imagen en su sitio correspondiente
        self.rect.midtop = self.screen_rect.midtop
    
    def image_show(self):
        self.screen.blit(self.image, self.rect)

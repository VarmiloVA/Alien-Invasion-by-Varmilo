import pygame
from pygame.sprite import Sprite

class Ufo(Sprite):
    """Una clase para representar un solo alien en la flota."""
    def __init__(self, ai_game):
        """Inicializa el ovni y configura su posición"""
        super().__init__()
        self.screen = ai_game.screen
    
        #Carga la imagen del enemigo y obtiene su rect.
        self.image = pygame.image.load('images/ovnis.bmp')
        self.rect = self.image.get_rect()

        #Coloca en el centro de la parte superior la pantalla
        #nueva.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Guarda la posición horizontal del alien
        self.x = float(self.rect.x)
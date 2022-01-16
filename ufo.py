import pygame
from pygame.sprite import Sprite

class Ufo(Sprite):
    """Una clase para representar un solo alien en la flota."""
    def __init__(self, ai_game):
        """Inicializa el ovni y configura su posición"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Carga la imagen del enemigo y obtiene su rect.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        #Coloca en el centro de la parte superior la pantalla
        #nueva.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Guarda la posición horizontal del alien
        self.x = float(self.rect.x)

        #Configuración del alien.
        self.alien_speed = self.settings.alien_speed

    def check_edges(self):
        """Devuelve True si el alien está en el borde de la pantalla"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Mueve los aliens hacia la derecha"""
        self.x += (self.settings.alien_speed *
                self.settings.fleet_direction)
        self.rect.x = self.x
        
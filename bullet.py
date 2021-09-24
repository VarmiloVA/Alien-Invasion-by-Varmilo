import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Una clase para gestionar las balas disparadas desde la nave"""

    def __init__(self, ai_game):
        """Crea un objeto para la bala en la posición actual de la nave."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        #Crea un rectángulo para la bala en (0,0) y luego establece la 
        #posición correcta.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Guarda la posición de la bala como valor decimal.
        selfy = float(self.rect.y)
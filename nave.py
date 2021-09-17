import pygame

class Ship:
    """Una clase para gestionar la nave."""

    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load('images/ship.bmp')

        self.rect = self.image.get_rect()

        # Coloca en el centro de la parte inferior de la pantalla cada nave
        # nueva.
        self.rect.midbottom = self.screen_rect.midbottom

        #Bandera de movimiento
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Actualiza la posición de la nave en función de la bandera"""
        if self.moving_right:
            self.rect.x += 1
            
        elif self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Dibuja la nave en su ubicación actual"""
        self.screen.blit(self.image, self.rect)
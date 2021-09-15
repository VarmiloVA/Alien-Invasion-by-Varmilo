import pygame

class Ship:
    """Una clase para gestionar la nave."""

    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Carga la imagen de la nave y  obtiene su rect.
        route = 'C:/Users/Dani/Desktop/fondos de pantalla/nave_espacial.bpm'
        self.image = pygame.image.load(route)

        self.rect = self.image.get_rect()

        # Coloca en el centro de la parte inferior de la pantalla cada nave
        # nueva.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Dibuja la nave en su ubicación actual"""
        self.screen.blit(self.image, self.rect)
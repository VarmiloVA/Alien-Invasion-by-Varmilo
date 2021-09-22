import pygame

class Ship:
    """Una clase para gestionar la nave."""

    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load('images/ship.bmp')

        self.rect = self.image.get_rect()

        # Coloca en el centro de la parte inferior de la pantalla cada nave
        # nueva.
        self.rect.midbottom = self.screen_rect.midbottom

        #Bandera de movimiento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #Guarda un valor decimal de la posición x de la nave
        self.x = float(self.rect.x)
    
    def update(self):
        #Actualiza el valor de x
        if self.moving_right:
            self.x += self.settings.ship_horizontal_speed

        elif self.moving_left:
            self.x -= self.settings.ship_horizontal_speed
        
        #Actualiza el objeto rect de self.x
        self.rect.x = self.x

        #Actualiza el valor de y
        if self.moving_up:
            self.y += self.settings.ship_vertical_speed

        elif self.moving.down:
            self.y -= self.settings.ship_vertical_speed



    def blitme(self):
        """Dibuja la nave en su ubicación actual"""
        self.screen.blit(self.image, self.rect)
import pygame

class Ship:
    """Una clase para gestionar la nave."""

    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.settings = ai_game.settings

        #Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self._center_ship()

        #Bandera de movimiento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #Guarda un valor decimal de la posición x de la nave
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def _center_ship(self):
        """Coloca la nave en el lugar inicial/de reaparición"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y) - 10
        
    def update(self):
        """Actualiza la posición de la nave en función de las banderas de 
        movimiento"""

        #Actualiza el valor x de la nave, no el rect.
        if self.moving_right and self.rect.right < self.screen_rect.right + 15:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > -15:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.centery + 150:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom + 15:
            self.y += self.settings.ship_speed

        # Actualiza el objeto rect de self.x
        self.rect.x = self.x
        # Actualiza el objeto rect de self.y
        self.rect.y = self.y

    def blitme(self):
        """Dibuja la nave en su ubicación actual"""
        self.screen.blit(self.image, self.rect)
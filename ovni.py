import pygame

class Ufo:
    """Una clase para gestionar los enemigos"""
    def __init__(self, ai_game):
        """Inicializa el ovni y configura su posición"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
    
        #Carga la imagen del enemigo y obtiene su rect.
        self.image = pygame.image.load('images/ovnis.bmp')
        self.image_2 = self.image

        self.rect = self.image.get_rect()

        #Coloca en el centro de la parte superior la pantalla
        #nueva.
        self.rect.midtop = self.screen_rect.midtop
    
    def blitme(self):
        """Dibuja la nave en su ubicación actual"""
        self.screen.blit(self.image, self.rect)
import sys
import pygame

from settings import Settings
from nave import Ship

class AlienInvasion:
    'Clase general para gestionar los recursos y el comportamiento del juego.'

    def __init__(self):
        """Inicializa el juego y crea recursos."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.setting_width, self.settings.setting_height)
            )

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Configura el color de fondo
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Inicia el bucle principal para el juego."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        """Actualiza la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    #Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
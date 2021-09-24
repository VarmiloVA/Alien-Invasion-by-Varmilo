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
        """Comprueba los eventos y responde a ellos"""
        for event in pygame.event.get():
            #Comprueba si el usuario ha cerrado la ventana
            if event.type == pygame.QUIT:
                sys.exit()
            #Comprueba los eventos de tipo keydown
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            #Comprueba los eventos de tipo keyup
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)
    
    def _keydown_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True               
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True              
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True

    def _keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False            
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False  

    def _update_screen(self):
        """Actualiza la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    #Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
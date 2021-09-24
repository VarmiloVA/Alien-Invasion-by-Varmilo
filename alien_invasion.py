import sys
import pygame

from settings import Settings
from nave import Ship

class AlienInvasion:
    'Clase general para gestionar los recursos y el comportamiento del juego.'

    def __init__(self, modo_pantalla):
        """Inicializa el juego y crea recursos."""
        pygame.init()

        self.settings = Settings()
        self.formato_pantalla = modo_pantalla

        if self.formato_pantalla == 'COMPLETO':
            # El juego se abre en pantalla completa
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        elif self.formato_pantalla == 'VENTANA':
            # El juego se abre en una ventana
            self.screen = pygame.display.set_mode(
                (self.settings.setting_width, self.settings.setting_height)
            )
        self.ship = Ship(self)

        # Configura el color de fondo
        self.bg_color = self.settings.bg_color

        # Variable que hace que el usuario tenga de darle dos veces a esc para 
        # salir
        self.escape = 0

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
            self.escape = 0
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True      
            self.escape = 0         
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True  
            self.escape = 0            
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True
            self.escape = 0
        elif event.key == pygame.K_ESCAPE and self.escape < 1:   
            self.escape += 1
        elif event.key == pygame.K_ESCAPE and self.escape == 1:
            sys.exit()

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
    try:
        ai = AlienInvasion('fdas')
        ai.run_game()
    except AttributeError:
        print('atributos mal introducidos')
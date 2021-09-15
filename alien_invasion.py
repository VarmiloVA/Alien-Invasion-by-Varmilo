import sys
import pygame

from settings import Settings

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

        # Configura el color de fondo
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Inicia el bucle principal para el juego."""
        while True:
            #Busca eventos de teclado y ratón
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redibuja la pantalla en cada paso por el bucle
            self.screen.fill(self.bg_color)
            
            #Hace visible la última pantalla dibujada.
            pygame.display.flip()

if __name__ == '__main__':
    #Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
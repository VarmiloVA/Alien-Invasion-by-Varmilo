import sys
import pygame
from pygame.sprite import Sprite

from settings import Settings
from inicial_screen import Screen
from nave import Ship
from bullet import Bullet
from ufo import Ufo

class AlienInvasion:
    'Clase general para gestionar los recursos y el comportamiento del juego.'

    def __init__(self, modo_pantalla, screen):
        """Inicializa el juego y crea recursos."""
        pygame.init()

        self.settings = Settings()
        self.formato_pantalla = modo_pantalla
        self.key_pressed = False

        screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
            )

        self.screen = screen

        self.inicial_screen = Screen(self)
        
        if self.formato_pantalla.upper() == 'COMPLETO':
            #El juego se abre en pantalla completa
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        elif self.formato_pantalla.upper() == 'VENTANA':
            # El juego se abre en una ventana
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
            )

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Configura el color de fondo
        self.bg_color = self.settings.bg_color

        #Variable que hace que el usuario tenga de darle dos veces a esc para 
        #salir
        self.escape = 0

    def run_game(self):
        """Inicia el bucle principal para el juego."""
        while True:
            if self.key_pressed == False:
                self._check_events()
                self._update_inicial_screen()
            elif self.key_pressed:
                self._check_events()
                self.ship.update()
                self._update_bullets()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._mouse_down_events(event)
    
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
        elif event.key == pygame.K_SPACE:
            self.key_pressed = True
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

    def _mouse_down_events(self, event):
        if event.button == 1:
            self._fire_bullet()
            self.escape = 0

    def _fire_bullet(self):
        """Crea  una bala nueva y la añade al grupo de balas."""
        if len(self.bullets) < self.settings.max_bullet_num:    
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    def _update_bullets(self):
        """Actualiza la posición de las balas y se deshace de las viejas"""
        #Actuliza las posiciones de las balas
        self.bullets.update()

        #Se deshaze de las balas que han desaparecido
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _create_fleet(self):
        """Crea una flota de aliens"""
        #Crea un alien y halla el número de aliens en una fila
        #El espacio entre aliens es igual a la anchura de 1 alien
        alien = Ufo(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determina el número de filas de aliens que caben en pantalla.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                            (4.5 * alien_height) - ship_height)

        #Crea la primera fila de aliens.
        for alien_number in range(number_aliens_x):
            #Crea un alien y lo coloca en la fila.
            self._create_alien(alien_number)
    
    def _create_alien(self, alien_number):
        """Crea un alien y lo coloca en la fila."""
        alien = Ufo(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)


    def _update_screen(self):
        """Actualiza la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()
    
    def _update_inicial_screen(self):
        """Actualiza la pantalla mientras el usuario no haya presionado"""
        """ninguna tecla o boton del mouse."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.inicial_screen.image_show()

        pygame.display.flip()

if __name__ == '__main__':
    #Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion('VENTANA', 'patata')
    ai.run_game()
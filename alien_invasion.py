import sys
import pygame
import json
import itertools
from pygame.sprite import Sprite
from time import sleep

from settings import Settings
from screen_elements import *
from nave import Ship
from bullet import Bullet
from ufo import Ufo

class AlienInvasion:
    'Clase general para gestionar los recursos y el comportamiento del juego.'

    def __init__(self, modo_pantalla, user_name, key_pressed=False):
        """Inicializa el juego y crea recursos."""
        pygame.init()

        self.leaderboard_archive = 'leaderboard.json'
        self.user_name = user_name
        self.settings = Settings()
        self.formato_pantalla = modo_pantalla
        self.key_pressed = key_pressed
        self.number_lives = self.settings.number_lives

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
            )
        self.screen_rect = self.screen.get_rect()

        self.inicial_screen = InicialScreen(self)
        self.lives = LivesCounter(self)
        self.level_number = 1
        self.level = Level(self)
        self.game_over_screen = self.lives.game_over_screen
        self.points = Points(self)
        self.restart_button = ResetButton(self)
        self.leaderboard = LeaderBoard(self)

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
        """Inicia el bucle para el juego."""
        self.points.reset_points()
        self.stop_game = False

        while self.stop_game == False:
            if not self.key_pressed:
                self._check_events()
                self._update_inicial_screen()
                self._check_score()
            elif self.key_pressed:
                self._check_events()
                self._update_aliens()
                self.ship.update()
                self._update_bullets()
                self._update_screen()
                self._check_score()

        while self.stop_game:
            self._update_screen()
            self._check_events()       

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
        if self.stop_game == False:
            if event.button == 1:
                self._fire_bullet()
                self.escape = 0
        elif self.stop_game == True:
            mouse_pos = pygame.mouse.get_pos()
            self._check_restart_button(mouse_pos)

    def _fire_bullet(self):
        """Crea  una bala nueva y la añade al grupo de balas."""
        if len(self.bullets) < self.settings.max_bullet_num:    
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    def _update_bullets(self):
        """Actualiza la posición de las balas y se deshace de las viejas"""
        #Actuliza las posiciones de las balas
        self.bullets.update()
        self._bullets_collisions()
        
    def _bullets_collisions(self):
        """Responde a las colisiones de las balas."""
        #Se deshace de las balas que han desaparecido.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        #Retira todas las balas y aliens que han chocado.
        if pygame.sprite.groupcollide(self.bullets, self.aliens, True, True):
            self.points.points += 1

        if not self.aliens and self.stop_game == False:
            # Destruye las balas existentes y crea una flota nueva.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.level_number += 1
    
    def _create_fleet(self):
        """Crea una flota de aliens"""
        #Crea un alien y halla el número de aliens en una fila
        #El espacio entre aliens es igual a la anchura de 1 alien
        alien = Ufo(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determina el número de filas de aliens que caben en pantalla.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                            (4 * ship_height))
        number_rows = int((available_space_y // (3 * alien_height)) // 1.5)

        #Crea la flota completa de aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        """Crea un alien y lo coloca en la fila."""
        alien = Ufo(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = (2* alien.rect.height + 2* alien.rect.height)* row_number
        alien.rect.y += 25
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Responde adecuadamente si algún alien ha llegado a un borde."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Baja toda la flota y cambia su dirección."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Si un alien toca el borde inferior de la pantalla el jugador pierde una vida"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._ship_hit()
                break
    
    def _update_aliens(self):
        """
        Comprueba si la flota está en un borde, después actualiza las 
        posiciones de todos los aliens de la flota.
        """
        self._check_fleet_edges()
        self._check_aliens_bottom()
        self.aliens.update()

        #Busca colisiones alien-nave.
        if pygame.sprite.spritecollideany(self.ship ,self.aliens):
            self._ship_hit()
    
    def _ship_hit(self):
        """Responde al impacto de un alien en la nave."""
        self.number_lives -= 1

        self.aliens.empty()
        self.bullets.empty()

        if self.number_lives >= 1:
            self._create_fleet()
            self.ship._center_ship()
            sleep(0.2)
        elif self.number_lives == 0:
            sleep(0.3)
            self.stop_game = True

    def _check_restart_button(self, mouse_pos):
        """Reinicia el juego cuando el jugador hace click en 'Restart'"""
        if self.restart_button.rect.collidepoint(mouse_pos):
            self.instancia = AlienInvasion('VENTANA',self.user_name, True)
            x = self.instancia.run_game()
            self.stop_game = False
            self.lives.number_lives = self.settings.number_lives 
            self.settings.initialize_dynamic_settings()
            self.level_number = self.level.reset_level()
            
            return x, self.stop_game
    
    def _check_score(self):       
        if self.stop_game:
            with open(self.leaderboard_archive, "r+") as f:
                dic = json.loads(f.read())
                leaderboard_dic = dic["leaderboard"]
                scores = self.leaderboard.get_scores()
                flag = True

                if self.stop_game:
                    for i in scores:
                        if self.points.points > i and flag == True:
                            leaderboard_dic[user_name] = str(self.points.points)
                            f.seek(0)
                            json.dump(dic, f)

    def _update_screen(self):
        """Actualiza la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        self.lives.show_lives_number()
        self.level.show_level()
        self.points.show_points()
        if self.stop_game:
            self.leaderboard.show_leaderboard()

        pygame.display.flip()
        
    def _update_inicial_screen(self):
        """Actualiza la pantalla mientras el usuario no haya presionado"""
        """ninguna tecla o boton del mouse."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.inicial_screen.image_show()

        pygame.display.flip()

if __name__ == '__main__':
    #Crea una lista con los username ya existentes:
    json_file = 'leaderboard.json'
    with open(json_file, 'r') as leaderboard_file:
        read = leaderboard_file.read()
    
    dic = json.loads(read)
    leaderboard_dic = dic['leaderboard']

    #Sacar los usuarios del dict
    users = []
    for k,v in dic.items():
        users.append(k)

    #Antes de ejecutar pregunta el nombre del usuario.
    while True:
        user_name = input('Username: ')

        if user_name not in users:
            break
        elif user_name in users:
            print('This username has been used before, try a different one')
            continue

    #Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion('VENTANA', user_name)
    ai.run_game()
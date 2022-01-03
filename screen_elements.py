import pygame
import pygame.font
import sys

from settings import Settings
from rect_config import *
class InicialScreen:
    def __init__(self, ai_game):
        """Inicializa las características del tutorial inicial"""
        pygame.init()

        self.ai_game = ai_game
        self.ai_event = ai_game.key_pressed
        self.pantalla = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/pantalla_inicial.bmp')
        self.screen_rect = ai_game.screen.get_rect()
        self.rect = self.image.get_rect()

        #Coloca la imagen en su sitio correspondiente
        if ai_game.formato_pantalla.upper() == 'COMPLETO':
            self.rect.midtop = self.screen_rect.midtop
            self.rect = self.rect.midtop
        elif ai_game.formato_pantalla.upper() == 'VENTANA':
            self.rect.midtop = self.screen_rect.midtop
    
    def image_show(self):
        if self.ai_event == False:
            self.pantalla.blit(self.image, self.rect)

class LivesCounter:
    def __init__(self, ai_game):
        """Clase para crear un contador de vidas"""
        pygame.init()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings= ai_game.settings
        self.game_over_screen = False

        #Carga las diferentes imágenes
        self.image_live = pygame.image.load('images/live.bmp')
        self.image_death = pygame.image.load('images/death.bmp')
        self.game_over_image = pygame.image.load('images/game_over.bmp')
        #Carga los rects de las diferentes imágenes
        self.image_live_rect = self.image_live.get_rect()
        self.image_death_rect = self.image_death.get_rect()
        self.game_over_image_rect = self.game_over_image.get_rect()

        #Configura el corazón correspondiente a cada una de las vidas/muertes.
        #Configura las imágenes de las VIDAS
        self.image_live_1 = self.image_live
        self.image_live_2 = self.image_live
        self.image_live_3 = self.image_live
        #Configura las imágenes de las MUERTES
        self.image_death_1 = self.image_death
        self.image_death_2 = self.image_death
        self.imgae_death_3 = self.image_death

        #Configura los rects de cada unas de las VIDAS.
        self.live_1_rect = self.image_live_rect.copy()
        self.live_2_rect = self.image_live_rect.copy()
        self.live_3_rect = self.image_live_rect.copy()
        #Configura los rescts de cada una de las MUERTES.
        self.death_1_rect = self.image_death_rect.copy()
        self.death_2_rect = self.image_death_rect.copy()
        self.death_3_rect = self.image_death_rect.copy()

        #Determina el tamaño del rect de los corazones
        self.live_width, self.live_height = self.image_live.get_size() 
        self.death_width, self.death_height = self.image_death.get_size()
    
    def reset_lives(self):
        self.ai_game.number_lives = self.settings.number_lives

    def show_lives_number(self):
        """Muestra el número de vidas junto a un corazón"""
        if self.ai_game.number_lives == 3:
            self.live_1_rect.center = config_position_lives(self.image_live, self.ai_game, 1)
            self.live_2_rect.center = config_position_lives(self.image_live, self.ai_game, 2)
            self.live_3_rect.center = config_position_lives(self.image_live, self.ai_game, 3) 
       
            self.screen.blit(self.image_live_1, self.live_1_rect)
            self.screen.blit(self.image_live_2, self.live_2_rect)
            self.screen.blit(self.image_live_3, self.live_3_rect)

            game_over_screen = False

        if self.ai_game.number_lives == 2:
            self.live_1_rect.center = config_position_lives(self.image_live, self.ai_game, 1)
            self.live_2_rect.center = config_position_lives(self.image_live, self.ai_game, 2)
            self.death_1_rect.center = config_position_lives(self.image_death, self.ai_game, 3)

            self.screen.blit(self.image_live, self.live_1_rect)
            self.screen.blit(self.image_live, self.live_2_rect)
            self.screen.blit(self.image_death, self.death_1_rect)

            game_over_screen = False
        
        if self.ai_game.number_lives == 1:
            self.live_1_rect.center = config_position_lives(self.image_live, self.ai_game, 1)
            self.death_2_rect.center = config_position_lives(self.image_death, self.ai_game, 2)
            self.death_1_rect.center = config_position_lives(self.image_death, self.ai_game, 3)

            self.screen.blit(self.image_live, self.live_1_rect)
            self.screen.blit(self.image_death, self.death_2_rect)
            self.screen.blit(self.image_death, self.death_1_rect)

            game_over_screen = False

        if self.ai_game.number_lives <= 0:
            self._show_game_over()
    
    def _show_game_over(self):
        """Muestra una pantalla de game over junto a 3 corazones negros."""
        self.death_3_rect.center = config_position_lives(self.image_death, self.ai_game, 1)
        self.death_2_rect.center = config_position_lives(self.image_death, self.ai_game, 2)
        self.death_1_rect.center = config_position_lives(self.image_death, self.ai_game, 3)

        self.screen.blit(self.game_over_image, self.config_game_over_show())
        self.screen.blit(self.image_death, self.death_3_rect)
        self.screen.blit(self.image_death, self.death_2_rect)
        self.screen.blit(self.image_death, self.death_1_rect)

        game_over_screen = True
            
        restart_button = ResetButton(self.ai_game)
        restart_button.draw_button()

    def config_game_over_show(self):
            """Prepara la pantalla de game over para ser mostrada"""
            if self.ai_game.number_lives <= 0:
                self.game_over_image_rect = (self.screen_rect[0] // 2, self.screen_rect[1] // 2)

                return self.game_over_image_rect


class ResetButton():
    def __init__(self, ai_game):
        """Crea el boton de reset para cuando el jugador pierde"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect

        self.message = 'Restart'

        #Configura las dimensiones y propiedades del botón
        self.width, self.height = 200, 50
        self.button_color = (20, 150, 200)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 40)

        #Crea el objeto rect del botón y lo centra.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (550, 650)

        #Prepara el mensaje del botón
        self._prep_msg(self.message)
    
    def _prep_msg(self, message):
        """Convierte mensaje en una imagen renderizada y centra el texto en el botón."""
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        #Dibuja un botón en blanco y luego el mensaje.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
    
class Points:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.points = 0

        #Cargar las diferentes imágenes y sus rects
        self.number_zero = pygame.image.load('images/number0.bmp')
        self.number_one = pygame.image.load('images/number1.bmp')
        self.number_five = pygame.image.load('images/number5.bmp')

        self.number_zero_rect = self.number_zero.get_rect()
        self.number_one_rect = self.number_one.get_rect()
        self.number_five_rect = self.number_five.get_rect()

        self.config_points = ConfigPoints(self.ai_game)

    def reset_points(self):
        """Reinicia las estadísticas cuando se empieza una nueva partida"""
        self.points = 0
    
    def show_points(self):
        if self.points == 5:
            self.config_points.config_points(self.number_five, 1)

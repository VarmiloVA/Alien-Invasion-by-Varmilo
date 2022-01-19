import pygame
import pygame.font
import sys
import json

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

            self.game_over_screen = False

        if self.ai_game.number_lives == 2:
            self.live_1_rect.center = config_position_lives(self.image_live, self.ai_game, 1)
            self.live_2_rect.center = config_position_lives(self.image_live, self.ai_game, 2)
            self.death_1_rect.center = config_position_lives(self.image_death, self.ai_game, 3)

            self.screen.blit(self.image_live, self.live_1_rect)
            self.screen.blit(self.image_live, self.live_2_rect)
            self.screen.blit(self.image_death, self.death_1_rect)

            self.game_over_screen = False
        
        if self.ai_game.number_lives == 1:
            self.live_1_rect.center = config_position_lives(self.image_live, self.ai_game, 1)
            self.death_2_rect.center = config_position_lives(self.image_death, self.ai_game, 2)
            self.death_1_rect.center = config_position_lives(self.image_death, self.ai_game, 3)

            self.screen.blit(self.image_live, self.live_1_rect)
            self.screen.blit(self.image_death, self.death_2_rect)
            self.screen.blit(self.image_death, self.death_1_rect)

            self.game_over_screen = False

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
        print(self.image_death.get_size())

        self.game_over_screen = True
            
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
        self.font = pygame.font.SysFont('Calibri', 40)

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
        self.screen_rect = ai_game.screen_rect
        self.points = 0

        #Configura el rect en el que se va a representar el número de puntos.
        self.width, self.height = 1, 1
        self.rect_color = (93, 118, 142)
        self.number_color = (0,0,0)
        self.font = pygame.font.SysFont('Calibri', 30)

        #Crea el rect donde se van a representar los puntos.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen_rect.topright

    def _prep_num(self, points):
        """Convierte los números en una imagen renderizada"""
        self.num_image = self.font.render(points, True, self.number_color, self.rect_color)
        self.num_image_rect = self.num_image.get_rect()
        self.num_image_rect.topright = self.rect.topright

    def reset_points(self):
        """Reinicia las estadísticas cuando se empieza una nueva partida"""
        self.points = 0
    
    def show_points(self):
        #Prepara los números que van a aparecer en el botón
        self._prep_num(str(self.points))

        self.screen.blit(self.num_image, self.num_image_rect)

class LeaderBoard():
    def __init__(self, ai_game):
        self.json_file = "leaderboard.json"
        self.screen = ai_game.screen
        #Leer los datos contenidos en el archivo json.
        with open(self.json_file, "r") as leaderboard_file:
            read = leaderboard_file.read()

        dic = json.loads(read)
        self.leaderboard_dic = dic["leaderboard"]

    def get_best_scores(self):
        #Se meten en una lista las 3 mejores puntuaciones:
        self.scores = []
        for i in self.leaderboard_dic.keys():
            if self.leaderboard_dic[i] != None and self.leaderboard_dic[i] not in self.scores:
                self.leaderboard_dic[i] = int(self.leaderboard_dic[i]) 
                    
                self.scores.append(self.leaderboard_dic[i])

        return self.scores
            
    def get_users(self):
        #Saca una lista con los 3 jugadores con mejor puntuación.
        users = []
        for i in range(3):
            if self._get_key(self.scores[i]) not in users and len(self.scores) == 3:
                user = self._get_key(self.scores[i])
                users.append(user)
        return print(users)
    
    def _get_key(self, score):
        #Busca las llaves correspondientes con los 3 mejores scores
        try:
            for k,v in self.leaderboard_dic.items():
                if score == v:
                   return k

        except KeyError:
            print(self.leaderboard_dic)
            print("ha  llegado al keyerror de _get_key")

    def create_lb_dict(self):
        self.lb = {}
        scores = self.get_best_scores()
        users = self.get_users()
        try:
            self.lb = {
                'Varmilo': scores[0],
                "Psylo": scores[1],
                'S4vitar': scores[2]
            }
        except IndexError:
            print(f'{IndexError} en el dict inicial de create_lb_dict')
        except TypeError:
            print(f"{TypeError} en la línea 251")
        except:
            print(' ')

        if len(self.lb.values()) == 3:
            lb_sorted_values = sorted(self.lb.values(), reverse=True)
            self.lb_sorted = {}

            #Crear un diccionario con orden de mayor a menor segun los scores.
            for i in lb_sorted_values:
                for k in self.lb.keys():
                    if self.lb[k] == i:
                        self.lb_sorted[k] = self.lb[k]
            
            return self.lb_sorted
            
        elif len(self.lb.values()) > 3 or len(self.lb.values()) < 3:
           return print("Error, el len(dict leaderboard) > 3") 

    def show_leaderboard(self):
        """shows the leaderboard"""
        #Obtiene el diccionario con la leaderboard ordenada
        lb_dict = self.create_lb_dict()
        #Define diferentes parámetros referidos a mostrar la leaderboard
        width, height = 150, 20
        rect_bg_color = (93, 118, 142)
        text_color = (0, 0, 0)
        lb_font = pygame.font.SysFont('Corbel', 20)

        #Crea el rect donde se va a encontrar la leaderboard y lo coloca
        rect_leaderboard = pygame.Rect(0, 30, width, height)
        if lb_dict is not None:
            position = 1
            for user, points in lb_dict.items():
                if position == 1:
                    text = f"{position}.-{user}: {points}"
                    position += 1
                elif position == 2:
                    text2 = f"{position}.-{user}: {points}"
                    position += 1
                elif position == 3:
                    text3 = f"{position}.-{user}: {points}"

        elif lb_dict is None:
            text = "El dict es nonetype"

        text_image = lb_font.render(text, True, text_color, rect_bg_color)
        text_image_rect = text_image.get_rect()
        text_image_rect.center = rect_leaderboard.center
        self.screen.blit(text_image, text_image_rect)

        text2_image = lb_font.render(text2, True, text_color, rect_bg_color)
        text2_image_rect = text2_image.get_rect()
        text2_image_rect.center = (rect_leaderboard.center[0], rect_leaderboard.center[1] + text_image_rect[1])
        self.screen.blit(text2_image, text2_image_rect)

        text3_image = lb_font.render(text3, True, text_color, rect_bg_color)
        text3_image_rect = text3_image.get_rect()
        text3_image_rect.center = (rect_leaderboard.center[0], rect_leaderboard.center[1] + 2*text_image_rect[1])
        self.screen.blit(text3_image, text3_image_rect)
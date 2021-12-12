import pygame

from screen_elements import *

def config_position(image, rect, ai_game, position):
    #Configura la imagen de vida o muerte en la posición correcta.
    if position == 1:
        flag = 0
    elif position == 2:
        flag = 1
    elif position == 3:
        flag = 2

    image_width, image_height = image.get_size()
    screen = ai_game.screen
    screen_rect = screen.get_rect()
    rect_clone = image.get_rect()
    rect_clone.center = screen_rect.bottomright
    tuple_rect_value = (rect_clone[0] - (flag * image_width), rect_clone[1])
    rect.center = tuple_rect_value

    return rect.center
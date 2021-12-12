import pygame

from screen_elements import *

def config_position(image, ai_game, position):
    #Configura la imagen de vida o muerte en la posición correcta.

    image_width, image_height = image.get_size()
    screen = ai_game.screen
    screen_rect = screen.get_rect()
    rect_clone = image.get_rect()
    rect_clone.center = screen_rect.bottomright
    tuple_rect_value = (rect_clone[0] - (position -1 )*image_width, rect_clone[1])

    return tuple_rect_value
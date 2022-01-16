import pygame

def config_position_lives(image, ai_game, position):
    #Configura la imagen de vida o muerte en la posición correcta.

    image_width, image_height = image.get_size()
    screen_rect = ai_game.screen.get_rect()
    rect_clone = image.get_rect()
    rect_clone.center = screen_rect.bottomright
    tuple_rect_value = (rect_clone[0] - (position -1 )*image_width, rect_clone[1])

    return tuple_rect_value

class ConfigPoints:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

    def _position(self, image, position):
        image_width, image_height = image.get_size()
        rect_clone = image.get_rect()
        rect_clone.center = self.screen_rect.bottomleft
        tuple_rect_value = (rect_clone[0] + (position + 1)*image_width, rect_clone[1] - 10)

        return tuple_rect_value

    def config_points(self, image, position):
        image_rect = image.get_rect()
        image_rect.center = self._position(image, position)
        x = self.screen.blit(image, image_rect)

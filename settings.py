class Settings:
    """Una clase para guardar toda la configuración de alien invasion"""

    def __init__(self):
        """Inicializa la configuración del juego"""
        #Configuración de la pantalla
        #1100x700
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (93, 118, 142)

        #Apaño termporal para la velocidad que hay que cambiar
        self.ship_speed = 2
        self.ship_horizontal_speed = self.ship_speed
        self.ship_vertical_speed = self.ship_speed

        #Velocidad enemigos
        self.alien_speed = 5
        self.fleet_drop_speed = 8

        #fleet_direction de 1 representa derecha; -1 representa izquierda
        self.fleet_direction = 1

        #Configuración de las balas
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 6
        self.max_bullet_num = 20

        #Amarillo estándart: 255, 233, 0
        #Amarillo fosforito: 204, 255, 0
        self.bullet_color = (204, 254, 0)

        #Número de vidas.
        self.number_lives = 3
class Settings:
    """Una clase para guardar toda la configuración de alien invasion"""

    def __init__(self):
        """Inicializa la configuración del juego"""
        #Configuración de la pantalla
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (93, 118, 142)

        #Apaño termporal para la velocidad que hay que cambiar
        self.ship_speed = 0.8
        self.ship_horizontal_speed = self.ship_speed
        self.ship_vertical_speed = self.ship_speed

        #Configuración de las balas
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 6
        self.max_bullet_num = 4

        #Amarillo estándart: 255, 233, 0
        #Amarillo fosforito: 204, 255, 0
        self.bullet_color = (204, 254, 0)
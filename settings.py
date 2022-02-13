class Settings:
    """Una clase para guardar toda la configuración de alien invasion"""

    def __init__(self):
        """Inicializa la configuración del juego"""
        #Configuración de la pantalla
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (93, 118, 142)

        #Velocidad enemigos
        self.fleet_drop_speed = 10

        #Configuración de las balas
        self.bullet_width = 3
        self.bullet_height = 6
        self.max_bullet_num = 5

        #Amarillo estándart: 255, 233, 0
        #Amarillo fosforito: 204, 255, 0
        self.bullet_color = (204, 254, 0)

        #Número de vidas.
        self.number_lives = 1

        #Ritmo con el que incrementa la velocidad del juego.
        self.speedup_scale = 1.3
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
            """Inicializa los valores para los atributos que tengan que cambiar durante el juego"""
            self.ship_speed = 2.3
            self.bullet_speed = 4.0
            self.alien_speed = 4.0

            #fleet_direction de 1 representa derecha; -1 representa izquierda 
            self.fleet_direction = 1

    def increase_speed(self):
            self.ship_speed *= self.speedup_scale
            self.bullet_speed *= self.speedup_scale
            self.alien_speed *= self.speedup_scale
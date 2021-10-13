class Settings:
    """Una clase para guardar toda la configuración de alien invasion"""

    def __init__(self):
        """Inicializa la configuraciónd el juego"""
        #Configuración de la pantalla
        self.setting_width = 1100
        self.setting_height = 700
        self.bg_color = (93, 118, 142)
        #Apaño termporal para la velocidad que hay que cambiar
        self.ship_speed = 0.4
        self.ship_horizontal_speed = self.ship_speed
        self.ship_vertical_speed = self.ship_speed
        #Configuración de las balas
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 3
        #Amarillo estándart: 255, 233, 0
        #Amarillo fosforito: 204, 255, 0
        self.bullet_color = (255, 233, 0)
class Settings:
    """Una clase para guardar toda la configuración de alien invasion"""

    def __init__(self):
        """Inicializa la configuraciónd el juego"""
        self.setting_width = 1100
        self.setting_height = 700
        self.bg_color = (93, 118, 142)
        #Apaño termporal para la velocidad que hay que cambiar
        self.ship_speed = 0.4
        self.ship_horizontal_speed = self.ship_speed
        self.ship_vertical_speed = self.ship_speed
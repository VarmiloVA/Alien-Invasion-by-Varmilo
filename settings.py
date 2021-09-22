class Settings:
    """Una clase para guardar toda la configuración de alien invasion"""

    def __init__(self):
        """Inicializa la configuraciónd el juego"""
        self.setting_width = 1100
        self.setting_height = 700
        self.bg_color = (93, 118, 142)
        self.ship_horizontal_speed = 0.5
        self.ship_vertical_speed = 0.25
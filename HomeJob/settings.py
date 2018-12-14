class Settings():
    """
    Начальные установки
    """
    def __init__(self):
        # Параметры дисплея
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,110,255)

        # Параметры пули
        self.bullet_width = 10
        self.bullet_height = 2
        self.bullet_color = (255,0,0)
        self.bullet_speed_factor = 3

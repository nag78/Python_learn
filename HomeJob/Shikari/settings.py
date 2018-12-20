class Settings():
    """
    Начальные установки
    """
    def __init__(self):
        # Параметры дисплея
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (49, 178, 15)

        # Параметры мяча
        self.ball_width = 50
        self.ball_height = 50
        self.ball_color = (0, 0, 0)
        self.ball_speed = 10

class Settings():
    """Класс для хранения всех настроек"""
    def __init__(self):
        """Инициализируем настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 100, 230)

        # Параметры капли
        self.drop_speed = 1

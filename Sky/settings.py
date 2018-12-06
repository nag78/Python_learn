class Settings():
    """
    Класс для хранения настроек
    """
    def __init__(self):
        """
        Инициализация настроек
        """
        #Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (143,110,255)

        #Параметры ракеты
        self.rocket_speed_factor = 1.5
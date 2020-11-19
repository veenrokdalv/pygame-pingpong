import pygame as pg


class Platform:
    """
    Класс платформы.
    Описан весь функционал платформы платформы.
    """

    def __init__(self, WINDOW, start_pos_y):
        """Инициализация главных настроек платформы"""

        # Ссылка на окно
        self.WINDOW = WINDOW

        # Параметры поверхности
        self.WIDTH = 130
        self.HEIGHT = 20
        self.pos_x = pg.display.get_window_size()[0] // 2 - self.WIDTH // 2
        self.pos_y = start_pos_y + 50 - self.HEIGHT
        self.color = (102, 51, 0)
        self.rect = (self.pos_x, self.pos_y, self.WIDTH, self.HEIGHT)
        self.speed = 20

        # Колличество очков
        self.score = 0


    def draw(self):
        """
        Отрисовывает платформу
        в координатах self.pos_x, self.pos_y,
        с цветом self.color,
        и размерами self.WIDTH, self.HEIGH
        """
        pg.draw.rect(self.WINDOW, self.color, self.rect)
    
    def move_left(self):
      """Передвигает платформу в лево"""

      self.pos_x - self.speed
    
    def move_right(self):
      """Передвигает платформу в право"""

      self.pos_x + self.speed
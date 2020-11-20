import random
import pygame as pg


class Ball:
    """
    Класс шарика.
    Описан весь функционал шарика.
    """

    def __init__(self, WINDOW):
        """Инициализация главных настроек мячика."""

        # Окно
        self.WINDOW = WINDOW

        # Начальное положение
        self.pos_x = pg.display.get_window_size()[0] // 2
        self.pos_y = pg.display.get_window_size()[1] // 2

        # Начально направление
        self.speed_x = random.choice([-6, -8, -10, 6, 8, 10])
        self.speed_y = random.choice([-6, -8, -10, 6, 8, 10])

        # Характеристики
        self.RADIUS = 25
        self.speed = 5
        self.color = (255, 0, 51)

    def draw(self):
        """Отрисовывает мячик в координатах self.pos_x, self.pos_y, цветом self.color, радиусом self.radius"""
        pg.draw.circle(self.WINDOW, self.color, (self.pos_x, self.pos_y), self.RADIUS)

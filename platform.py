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
        self.WIDTH = 150
        self.HEIGHT = 20
        self.pos_x = pg.display.get_window_size()[0] // 2 - self.WIDTH // 2
        self.pos_y = start_pos_y + 50 - self.HEIGHT
        self.color = (102, 51, 0)
        self.speed = 10

        # Колличество очков
        self.score = 0

    def draw(self):
        """
        Отрисовывает платформу
        в координатах self.pos_x, self.pos_y,
        с цветом self.color,
        и размерами self.WIDTH, self.HEIGH
        """
        pg.draw.rect(self.WINDOW, self.color, (self.pos_x,
                                               self.pos_y, self.WIDTH, self.HEIGHT))

    @property
    def collision_wall(self) -> bool:
        """
        Прозводится расчет, пересечет ли платформа следующим шагом стенку.
        :return : True - если пересечет, иначе False
        """
        return (self.pos_x - self.speed < 0), (self.pos_x + self.speed + self.WIDTH > pg.display.get_window_size()[0])

    def move_left(self):
        """Передвигает платформу в лево"""
        if not self.collision_wall[0]:
            self.pos_x -= self.speed

    def move_right(self):
        """Передвигает платформу в право"""
        if not self.collision_wall[1]:
            self.pos_x += self.speed

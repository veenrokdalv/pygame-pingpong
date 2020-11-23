import random
import pygame as pg


class Ball:
    """
    Класс шарика.
    Описан весь функционал шарика.
    """

    def __init__(self, WINDOW, PLATFORM_TOP, PLATFORM_BOTTOM):
        """Инициализация главных настроек мячика."""

        # Окно
        self.WINDOW = WINDOW

        # Платформы
        self.PLATFORM_TOP = PLATFORM_TOP
        self.PLATFORM_BOTTOM = PLATFORM_BOTTOM

        # Начальное положение
        self.pos_x = pg.display.get_window_size()[0] // 2
        self.pos_y = pg.display.get_window_size()[1] // 2

        # Начально направление
        self.speed_x = random.choice([-4, -5, -6, 4, 5, 6])
        self.speed_y = random.choice([-4, -5, -6, 4, 5, 6])

        # Характеристики
        self.RADIUS = 20
        self.color = (255, 0, 51)

    def draw(self):
        """Отрисовывает мячик в координатах self.pos_x, self.pos_y, цветом self.color, радиусом self.radius"""
        pg.draw.circle(self.WINDOW, self.color,
                       (self.pos_x, self.pos_y), self.RADIUS)

    def move(self):
        """Изменяет координаты self.pos_x, self.pos_y"""
        self.collision_wall()
        self.collision_platform()
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

    def collision_wall(self):
        """Проверяет на столкновение с границами экрана"""
        if self.pos_x - self.RADIUS < 0 or self.pos_x + self.RADIUS + self.speed_x > pg.display.get_window_size()[0]:
            self.speed_x = -self.speed_x
        elif self.pos_y - self.RADIUS < 0 or self.pos_y + self.RADIUS + self.speed_y > pg.display.get_window_size()[1]:
            self.set_start_position()
            self.set_random_speed()
   
   
    def collision_platform(self):
        """Проверка на столкновение c платформой"""
        # Нижняя сторона шарика с верхней стороной нижней доски
        if self.pos_y + self.RADIUS > self.PLATFORM_BOTTOM.pos_y:
            # Нижняя леваая сторона шарика с верхней правой стороной нижней доски
            if self.pos_x - self.RADIUS < self.PLATFORM_BOTTOM.pos_x + self.PLATFORM_BOTTOM.WIDTH:
                # Нижняя правая сторона шарика с верхней левой стороной нижней доски
                if self.pos_x + self.RADIUS > self.PLATFORM_BOTTOM.pos_x:
                    self.speed_y = - self.speed_y   
        
        # Верхняя сторона шарика с нижней стороной верхней доски
        if self.pos_y - self.RADIUS < self.PLATFORM_TOP.pos_y + self.PLATFORM_TOP.HEIGHT:
            # Верхняя леваая сторона шарика с нижней левой стороной верхней доски
            if self.pos_x - self.RADIUS < self.PLATFORM_TOP.pos_x + self.PLATFORM_TOP.WIDTH:
                # Верхняя правая сторона шарика с нижней правой стороной верхней доски
                if self.pos_x + self.RADIUS > self.PLATFORM_TOP.pos_x:
                    self.speed_y = - self.speed_y 

    def set_start_position(self):
        """Возвращает мячик в центр экрана"""
        self.pos_x = pg.display.get_window_size()[0] // 2
        self.pos_y = pg.display.get_window_size()[1] // 2

    def set_random_speed(self):
        """Устанавливает новые параметры скоростей для обеих осей"""
        self.speed_x = random.choice([-4, -5, -6, 4, 5, 6])
        self.speed_y = random.choice([-4, -5, -6, 4, 5, 6])

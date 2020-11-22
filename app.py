import pygame as pg
import platform
import ball


class App:
    """
    Класс приложения.
    Управляет всеми процессами приложения.
    """

    def __init__(self):
        """Инициализация главных настроек приложения"""

        # Настройки окна.
        self.WIDTH = 600
        self.HEIGHT = 900
        self.TITLE = "Ping Pong"
        self.ICON = pg.image.load('images/icon_app.png')
        self.WINDOW = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self._color = (0, 102, 51)
        pg.display.set_caption(self.TITLE)
        pg.display.set_icon(self.ICON)

        # Настройки производительности
        self._CLOCK = pg.time.Clock()
        self._fps = 75

        # Инициализация платформ
        self.PLATFORM_TOP = platform.Platform(self.WINDOW, 0)
        self.PLATFORM_BOTTOM = platform.Platform(
            self.WINDOW, self.HEIGHT - 80)

        # Инициализация мячика
        self._BALL = ball.Ball(self.WINDOW, self.PLATFORM_TOP, self.PLATFORM_BOTTOM)

    def run(self):
        """Запуск основного цикла программы"""
        while True:
            self.check_events()
            self.move()
            self.draw()
            self._CLOCK.tick(self._fps)

    def quit(self):
        """Завершение программы"""
        print('Правильное завершение программы')
        pg.quit()
        quit()

    def check_events(self):
        """Отслеживает все события программы"""

        # Выход из программы путем нажатия крестика
        [self.quit() for event in pg.event.get() if event.type == pg.QUIT]

        # Все события с клавиатуры
        keys = pg.key.get_pressed()

        # Завершение программы нажатием ESCAPE
        if keys[pg.K_ESCAPE]:
            self.quit()

        # Обработка клавиш управления self.PLATFORM_TOP
        if keys[pg.K_a]:
            self.PLATFORM_TOP.move_left()
        if keys[pg.K_d]:
            self.PLATFORM_TOP.move_right()

        # Обработка клавиш управления self.PLATFORM_BOTTOM
        if keys[pg.K_LEFT]:
            self.PLATFORM_BOTTOM.move_left()
        if keys[pg.K_RIGHT]:
            self.PLATFORM_BOTTOM.move_right()

    def draw(self):
        """Отображает все объекты программы"""
        # Отрисовка фона
        self.WINDOW.fill(self._color)

        # Отрисовка поверхностей
        self.PLATFORM_TOP.draw()
        self.PLATFORM_BOTTOM.draw()
        self._BALL.draw()

        pg.display.update()
    
    def move(self):
        """Передвигает объеты приложения"""
        self._BALL.move()
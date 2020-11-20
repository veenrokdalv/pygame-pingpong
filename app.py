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
        self.HEIGHT = 800
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
        self._PLATFORM_TOP = platform.Platform(self.WINDOW, 0)
        self._PLATFORM_BOTTOM = platform.Platform(self.WINDOW, self.HEIGHT - 80)

        # Инициализация шарика
        self._BALL = ball.Ball()

    def run(self):
        """Запуск основного цикла программы"""
        while True:
            self.check_events()
            self.draw()
            self._CLOCK.tick(self._fps)

    def quit(self):
        """Завершение программы"""
        print('Правильное завершение программы')
        pg.quit()
        quit()

    def check_events(self):
        """Отлавливание всех событий программы"""

        # Выход из программы путем нажатия крестика
        [self.quit() for event in pg.event.get() if event.type == pg.QUIT]

        # Все события с клавиатуры
        keys = pg.key.get_pressed()

        # Завершение программы нажатием ESCAPE
        if keys[pg.K_ESCAPE]:
            self.quit()

        # Обработка клавиш управления self._PLATFORM_TOP
        if keys[pg.K_a]:
            self._PLATFORM_TOP.move_left()
        if keys[pg.K_d]:
            self._PLATFORM_TOP.move_right()

        # Обработка клавиш управления self._PLATFORM_BOTTOM
        if keys[pg.K_LEFT]:
            self._PLATFORM_BOTTOM.move_left()
        if keys[pg.K_RIGHT]:
            self._PLATFORM_BOTTOM.move_right()

    def draw(self):
        """Отрисовывает и отображает все объекты программы"""
        # Отрисовка фона
        self.WINDOW.fill(self._color)

        # Отрисовка поверхностей
        self._PLATFORM_TOP.draw()
        self._PLATFORM_BOTTOM.draw()

        pg.display.update()

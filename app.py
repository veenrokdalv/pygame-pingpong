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
        self._color = (20, 20 , 20)
        pg.display.set_caption(self.TITLE)
        pg.display.set_icon(self.ICON)

        # Настройки производительности
        self._CLOCK = pg.time.Clock()
        self._fps = 30

        # Инициализация платформ
        self._PLATFORM_TOP = platform.Platform()
        self._PLATFORM_BOTTOM = platform.Platform()

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
        if [pg.K_ESCAPE]:
          self.quit()

        # Обработка клавиш управления self._PLATFORM_TOP
        if keys[pg.K_a]:
          pass
        if keys[pg.K_d]:
          pass

        # Обработка клавиш управления self._PLATFORM_BOTTOM
        if keys[pg.K_RIGHT]:
          pass
        if keys[pg.K_LEFT]:
          pass
    def draw(self):
      """Отрисовывает и отображает все объекты программы"""
      # Отрисовка фона
      self.WINDOW.fill(self._color)

      pg.display.update()
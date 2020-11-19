import pygame as pg
class Platform:
  """
  Класс платформы.
  Описан весь функционал платформы платформы.
  """
  def __init__(self, window, start_pos_y):
    """Инициализация главных настроек платформы"""
    
    # Параметры поверхности
    self.WIDTH = 130
    self.HEIGHT = 40
    self.pos_x = pg.display.get_window_size()[0] // 2 - self.WIDTH // 2
    self.pos_y = start_pos_y + 50
    self.color = (102, 51, 0)
    
    # Колличество очков
    self.score = 0



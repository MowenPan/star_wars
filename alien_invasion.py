import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        # 监视鼠标和键盘事件
        gf.check_events()

        # 每次循环都重新绘制屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # 让绘制的屏幕可见
        pygame.display.flip()

run_game()

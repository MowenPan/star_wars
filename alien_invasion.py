import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建存储子弹和外星人的编组
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视鼠标和键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(bullets)

        # 每次循环都重新绘制屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()

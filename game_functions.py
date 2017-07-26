import sys
import pygame
from bullet import Bullet


def check_keydown_events(event,ai_settings, screen, ship, bullets):
    # print(event.key)
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        # print(event.key)
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        # print(event.key)
    elif event.key == pygame.K_UP:
        ship.moving_up = True
        # print(event.key)
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
        # print(event.key)
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    # print(event.key)
    """响应松开按键事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        # print(event.key)
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
        # print(event.key)
    elif event.key == pygame.K_UP:
        ship.moving_up = False
        # print(event.key)
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
        # print(event.key)


def check_events(ai_settings, screen, ship, bullets):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像并求换到新屏幕"""
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 在外星人和飞船后面绘制所有子弹
    for bullet in  bullets:
        bullet.draw_bullet()
    ship.blitme()
    # 让最新绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹位置并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有达到限制就发射子弹"""
    # 创建新子弹并加入到bullets编组中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
